import os
from typing import Optional

from octo_pipeline_python.actions.action_result import ActionResultCode
from octo_pipeline_python.actions.action_type import ActionType
from octo_pipeline_python.backends.backend import Backend
from octo_pipeline_python.backends.backend_auth_details import \
    BackendAuthDetails
from octo_pipeline_python.backends.backend_description import \
    BackendDescription
from octo_pipeline_python.backends.backends_context import BackendsContext
from octo_pipeline_python.backends.docker.actions import DockerBuild
from octo_pipeline_python.backends.docker.models import DockerModel
from octo_pipeline_python.pipeline.pipeline_context import PipelineContext
from octo_pipeline_python.workspace.workspace_context import WorkspaceContext

TAG = "docker"


class DockerBackend(Backend):
    def __init__(self) -> None:
        self.__actions = {
            ActionType.Build: DockerBuild()
        }

    def initialize_backend(self,
                           backends_context: BackendsContext,
                           workspace_context: WorkspaceContext) -> bool:
        import docker
        from docker.client import DockerClient

        # Create the docker client
        client: DockerClient = docker.from_env()

        # Add the client to the context
        backends_context.add_attribute(TAG, "docker_client", client,
                                       exclude_from_db=True)

        return True

    def authenticate_backend(self,
                             auth_details: BackendAuthDetails,
                             backends_context: BackendsContext,
                             workspace_context: WorkspaceContext,
                             pipeline_context: Optional[PipelineContext]) -> ActionResultCode:
        return ActionResultCode.SUCCESS

    def cleanup_backend(self,
                        backends_context: BackendsContext,
                        workspace_context: WorkspaceContext) -> None:
        return None

    def describe_backend(self,
                         backends_context: BackendsContext,
                         workspace_context: WorkspaceContext) -> BackendDescription:
        return BackendDescription(name=TAG,
                                  working_dir=os.path.join(workspace_context.working_dir, TAG),
                                  actions=self.__actions,
                                  backend_model=DockerModel)

    @staticmethod
    def backend_name() -> str:
        return TAG
