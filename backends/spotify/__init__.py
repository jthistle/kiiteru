
import os
import sys

from ..backend import *


class Spotify(Backend):
    def __init__(self):
        super().__init__("Spotify")

    def get_is_up(self):
        is_up = self.run_script(__file__, "scripts/get_info.sh", "checkup")[1]
        return is_up

    def get_current_metadata(self):
        if not self.is_up:
            return None
        
        raw_meta = self.run_script(__file__, "scripts/get_info.sh", "all")[1]

        metadata = {}
        for line in raw_meta.split("\n"):
            key, value = line.split(":", maxplit=1)
            metadata[key] = value 

        # validate metadata
        title = metadata["title"]
        artist = metadata["artist"]

        if title == "":
            # something is wrong with the metadata
            return None

        if artist == "":
            # this is probably a podcast 
            artist = metadata["album"]
            if artist == "":
                # something is wrong with the metadata
                return None
            
            # make correction to metadata
            metadata["artist"] = artist

        return metadata

