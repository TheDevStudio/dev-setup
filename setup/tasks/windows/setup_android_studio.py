from setup.tasks.windows_setup_task import WindowsSetupTask


class SetupAndroidStudio(WindowsSetupTask):

    def version_cmd(self):
        return "android-studio --version"

    def setup(self):
        self.execute("choco install androidstudio -y")
