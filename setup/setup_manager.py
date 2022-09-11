import inspect


class SetupManager:
    class SetupException(Exception):
        def __init__(self, system):
            super().__init__(
                "Couldnt find an implementation of {} for {}".format(
                    inspect.stack()[1].function,
                    system)
            )

    def __init__(self, *args, **kwargs):
        self.system = kwargs["system"]

    def dev_setup(self):
        self.setup_terminal()

    def setup_terminal(self):
        raise self.SetupException(self.system)
