from setup.unix.unix_setup_manager import UnixSetupManager

class LinuxSetupManager(UnixSetupManager):

    def __init__(self, *args, **kwargs):
        super().__init__()
