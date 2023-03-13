from . import SetupTask


class LinuxSetupTask(SetupTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
