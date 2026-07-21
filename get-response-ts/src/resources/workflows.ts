/** Operations tagged 'Workflows' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class WorkflowsResource {
  constructor(private readonly core: Core) {}

  /** Get a single workflow by ID. */
  readonly getWorkflow = async (
    workflowId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Workflow> => {
    return this.core.request<M.Workflow>('GET', '/workflow/{workflowId}', {
      pathParams: { workflowId: workflowId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Get the list of workflows. */
  readonly getWorkflowList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
    },
    signal?: AbortSignal,
  ): Promise<M.Workflow[]> => {
    return this.core.request<M.Workflow[]>('GET', '/workflow', {
      query: params
        ? { fields: params.fields, perPage: params.perPage, page: params.page }
        : undefined,
      signal,
    });
  };

  /** Update single workflow. */
  readonly updateWorkflow = async (
    workflowId: string,
    body: M.UpdateWorkflow,
    signal?: AbortSignal,
  ): Promise<M.Workflow> => {
    return this.core.request<M.Workflow>('POST', '/workflow/{workflowId}', {
      pathParams: { workflowId: workflowId },
      body,
      signal,
    });
  };
}
