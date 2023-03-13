from setup.tasks.generic_task import GenericTask


class InitWorkspace(GenericTask):

    def perform(self):
        print("Initialising Workspace")
