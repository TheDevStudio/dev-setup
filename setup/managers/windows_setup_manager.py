from . import SetupManager
from setup.tasks.windows import *


class WindowsSetupManager(SetupManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dev_setup(self):
        SetupChocolatey().perform()
        SetupVSCode().perform()
        SetupGit().perform()
        InitWorkspace().perform()
