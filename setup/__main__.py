import platform

from setup.windows import WindowsSetupManager
from setup.unix.linux import LinuxSetupManager
from setup.unix.mac_os import MacOsSetupManager

if __name__ == "__main__":
    system = platform.system()
    # system = "Linux"
    # system = "Darwin"
    if system in ['Windows', 'Linux', 'Darwin']:
        print("Running " + __package__ + " for " + system)
        if system == 'Windows':
            WindowsSetupManager(system=system).dev_setup()
        elif system == 'Linux':
            LinuxSetupManager(system=system).dev_setup()
        elif system == 'Darwin':
            MacOsSetupManager(system=system).dev_setup()
    else: 
        print("Unsupported System:" + system)
        