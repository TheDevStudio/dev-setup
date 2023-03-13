from . import SetupTask


class WindowsSetupTask(SetupTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, *cmd, **kwargs):
        cmd = ["powershell", "-Command", *cmd]
        return super().execute(*cmd, **kwargs)
