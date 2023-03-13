from setup.tasks.windows_setup_task import WindowsSetupTask


class SetupVSCode(WindowsSetupTask):

    def version_cmd(self):
        return "code -v"

    def setup(self):
        self.execute("choco install vscode -y")
