
##
## Configuration
# Colours: colour of widget text corresponding to different playback states

# Whether or not to display song progress
SHOW_PROGRESS = True # default True

# The character to use at the start of the widget. Defaults to FontAwesome Spotify logo character.
START_CHAR = " " # default " "

# Maximum length of artist + song string. If set to None, no maximum.
# This will always completely remove the song title before truncating the artist.
MAX_LENGTH = 64 # default 64
##
##



class Configuration:
    def __init__(self):
        # TODO load this all from somewhere 
        self.base = {
            "color_playing":      "#1db954",
            "color_paused":       "#e3a600",
            "color_down":           "#ff0000",
            "color_unknown":      "#ffffff",
            "show_progress":      True,
            "marker_playing":    "⬤",
            "marker_paused":      "◯",
            "marker_stopped":      "■",
            "marker_down":        "",
        }

        self.overrides = {}

    def get_override_config(self, override_name):
        if override_name not in self.overrides:
            self.overrides[override_name] = {}
        return self.overrides[override_name]

    def set(self, key, value, backend_name = None):
        if key not in self.base:
            raise Exception(f"'{key}' is not a valid configuration key")
        
        if backend_name is None:
            self.base[key] = value        
            return
        
        self.get_override_config(backend_name)[key] = value

    def get(self, key, backend_name):
        overrides = self.get_override_config(backend_name)
        
        if key in overrides:
            return overrides[key]
        
        return self.base[key]

    def remove_override(self, key, backend_name):
        overrides = self.get_override_config(backend_name)
        overrides.pop(key)
            

