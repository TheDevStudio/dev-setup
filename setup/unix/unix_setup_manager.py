from setup.setup_manager import SetupManager

class UnixSetupManager(SetupManager):

    def __init__(self, *args, **kwargs):
        super().__init__()
        print("Unix init")

    def setup_terminal(self):
        print("Setting up zsh")