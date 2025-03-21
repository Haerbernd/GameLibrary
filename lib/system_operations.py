import sys
from enum import Enum
import platform
from typing import List
from lib.customExceptions import UnsupportedOperatingSystemException
from lib import logging_handler


class OperatingSystem(Enum):
    WINDOWS = 1
    LINUX = 2
    UNIX = 3
    DARWIN = 4  # e.g. MacOS
    OTHER = 5


USER_OS: OperatingSystem | None = None
compatible_os: List[OperatingSystem] = [OperatingSystem.WINDOWS, OperatingSystem.LINUX]


def terminate_system(reason: Exception | str, log_msg: str = "",) -> None:
    if log_msg == "":
        log_msg = f"The system will be terminated because of {reason}"
    logging_handler.log(log_msg)

    sys.exit(0)


def determine_user_os() -> None:
    user_os: str = platform.system().lower()
    global USER_OS

    if user_os == "windows":
        USER_OS = OperatingSystem.WINDOWS
    elif user_os == "linux" or "linux2":
        USER_OS = OperatingSystem.LINUX
    elif user_os == "darwin":
        USER_OS = OperatingSystem.DARWIN
    elif user_os == "unix":
        USER_OS = OperatingSystem.UNIX
    else:
        USER_OS = OperatingSystem.OTHER


def check_os_compatibility(allow_unsupported_os: bool = False) -> bool | None:
    determine_user_os()
    if USER_OS in compatible_os:
        return True
    else:
        if allow_unsupported_os:
            return False
        else:
            terminate_system(UnsupportedOperatingSystemException(USER_OS))
