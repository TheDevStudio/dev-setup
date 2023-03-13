import time
from abc import abstractmethod
import subprocess
from . import GenericTask


class SetupTask(GenericTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO: decide and add the fixed args/kwargs say for eg. 'system'= windows or linux or darwin
        self.system = "system"

    def perform(self):
        resp = {}
        start_time = time.time()
        print("")
        try:
            # TODO: need to add instrumentation here to maybe time the method
            if self.required():
                print(f"Going to perform {self.__class__.__name__}")
                self.setup()
            else:
                print(f"Skipping {self.__class__.__name__}. "
                      f"Version {self.installed_version} already installed")
            resp['success'] = True
        except Exception as e:
            print(
                f"Failed to {self.__class__.__name__}.\n {e.__class__.__name__}: {str(e)}")
            resp['success'] = False
        end_time = time.time()
        resp['time'] = end_time - start_time
        # print(resp)
        return resp

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def version_cmd(self):
        pass

    def required(self):
        try:
            self.installed_version = self.execute(
                self.version_cmd(), raise_error=True).split("\n")[0]
            return False
        except subprocess.CalledProcessError as e:
            return True

    def execute(self, *cmd, raise_error=True):
        cmd_str = ' '.join(cmd)
        print("Going to run:", cmd_str)
        completed = subprocess.run(cmd_str,
                                   capture_output=True,
                                   check=raise_error,
                                   text=True)
        # TODO: try to integrate non blocking read on stdout https://stackoverflow.com/a/4896288/12910036
        print("Output:", completed.stdout.strip())
        return completed.stdout.strip()
