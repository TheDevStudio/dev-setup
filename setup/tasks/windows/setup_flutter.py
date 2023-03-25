from setup.tasks.windows_setup_task import WindowsSetupTask


class SetupFlutter(WindowsSetupTask):

    def version_cmd(self):
        return "flutter --version"

    def setup(self):
        self.execute("choco install flutter -y")
