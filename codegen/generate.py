"""Entry point for the code generator: `python -m codegen.generate [--python] [--csharp]`.

Builds the `Api` IR from the vendored spec once, then hands it to whichever emitter(s)
were requested. Emitters are imported lazily inside each branch so a missing or
not-yet-implemented emitter for one language never blocks generating the other.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
from collections import Counter
from pathlib import Path

from codegen.ir import Api
from codegen.spec import build_api, load

_IR_DUMP_PATH = "codegen/_ir_dump.json"


def _dump_ir_summary(api: Api) -> None:
    """Print IR counts and per-tag operation distribution, and dump the full IR as JSON."""
    print(f"models:     {len(api.models)}")
    print(f"enums:      {len(api.enums)}")
    print(f"operations: {len(api.operations)}")

    by_tag = Counter(op.tag for op in api.operations)
    print("operations per tag:")
    for tag, count in sorted(by_tag.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {tag or '(untagged)'}: {count}")

    dump_path = Path(_IR_DUMP_PATH)
    dump_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dump_path, "w", encoding="utf-8") as f:
        json.dump(dataclasses.asdict(api), f, indent=2)
    print(f"full IR dump written to {dump_path}")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Generate GetResponse API client libraries."
    )
    parser.add_argument("--python", action="store_true", help="emit the Python package")
    parser.add_argument("--csharp", action="store_true", help="emit the C# solution")
    parser.add_argument(
        "--typescript", action="store_true", help="emit the TypeScript/Node package"
    )
    parser.add_argument(
        "--dump-ir",
        action="store_true",
        help="print IR summary stats and write codegen/_ir_dump.json",
    )
    args = parser.parse_args(argv)

    api = build_api(load())

    if args.dump_ir:
        _dump_ir_summary(api)

    if args.python:
        try:
            from codegen import emit_python  # type: ignore[attr-defined]
        except ImportError:
            print("Python emitter not yet implemented.")
        else:
            emit_python.emit(api, out_dir="get-response-py")

    if args.csharp:
        try:
            from codegen import emit_csharp  # type: ignore[attr-defined]
        except ImportError:
            print("C# emitter not yet implemented.")
        else:
            emit_csharp.emit(api, out_dir="get-response-cs")

    if args.typescript:
        try:
            from codegen import emit_typescript  # type: ignore[attr-defined]
        except ImportError:
            print("TypeScript emitter not yet implemented.")
        else:
            emit_typescript.emit(api, out_dir="get-response-ts")

    if not (args.python or args.csharp or args.typescript or args.dump_ir):
        parser.print_help()


if __name__ == "__main__":
    main()
