from subprocess import CalledProcessError
from setup.tasks.windows_setup_task import WindowsSetupTask


class SetupChocolatey(WindowsSetupTask):

    def version_cmd(self):
        return "choco -v"

    def setup(self):
        # TODO: check if need to run all in one shell
        self.execute("Set-ExecutionPolicy Bypass -Scope Process -Force;")
        self.execute(
            "[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;")
        self.execute(
            "iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")
