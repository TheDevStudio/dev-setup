from setup.tasks.windows_setup_task import WindowsSetupTask


class SetupGit(WindowsSetupTask):

    def version_cmd(self):
        return "git --version"

    def setup(self):
        self.execute("choco install git.install -y")
