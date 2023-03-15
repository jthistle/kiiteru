import os
import subprocess

from enum import Enum


class PlaybackStatus(Enum):
    UNKNOWN = 0
    PLAYING = 1
    PAUSED = 2
    STOPPED = 3

class OperationResult(Enum):
    SUCCESS = 0
    FAILURE = 1
    NOT_IMPLEMENTED = 2

class PlaybackCommand(Enum):
    PLAY = 0
    TOGGLE_PLAY = 1
    PAUSE = 2
    STOP = 3
    NEXT = 4
    PREV = 5
    VOLUME_UP = 6
    VOLUME_DOWN = 7


class Backend:
    def __init__(self, name):
        self.name = name

    def run_script(self, __file__, script_name, options = None):
        """Runs a script located at script_name relative to the file of the calling function.
        Requires __file__ to be passed by the calling function. options are the options that
        will be passed to the script. Returns (exit_code, output)."""

        script_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), script_name)

        process = subprocess.run(f"{script_path} {options or ''}", shell=True, stdout=subprocess.PIPE)

        output = process.stdout    
        decoded = output.decode("utf-8")
        return (process.returncode, decoded.strip())

    def get_is_up(self):
        return False

    def get_status(self):
        return PlaybackStatus.UNKNOWN

    def get_current_metadata(self):
        return None

    def send_command(self, command, data = None):
        return OperationResult.NOT_IMPLEMENTED

    
