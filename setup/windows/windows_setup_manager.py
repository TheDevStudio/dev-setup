from setup.setup_manager import SetupManager

class WindowsSetupManager(SetupManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup_terminal(self):
        print("setting up windows terminal/wsl shell")