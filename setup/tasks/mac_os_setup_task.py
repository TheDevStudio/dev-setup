from . import SetupTask


class MacOsSetupTask(SetupTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
