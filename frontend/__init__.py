from .configuration import Configuration


CONFIG = Configuration()


def seconds_to_time(timestamp):
    """Convert a number in seconds to a human-readable time string, e.g. 67 -> '1:07'."""
    timestamp = int(timestamp)
    secs = timestamp % 60
    mins = timestamp // 60
    return f"{mins:01}:{secs:02}"

def output_unknown():
    """Output for when metadata returns unexpected values."""
    print_line(f"{START_CHAR}...")
    print_line(COLOUR_UNKNOWN)


def generate_display(backend):
    
    if spotify_up == "0":
        # Spotify is not running
        print_line(f"{START_CHAR}down")
        print_line(COLOUR_DOWN)
    else:

        song_string = f"{artist} — {title}"

        # song string truncation
        if MAX_LENGTH is not None and len(song_string) > MAX_LENGTH:
            song_string = song_string[:MAX_LENGTH - 1] + "…"

        # song progress calculation
        if SHOW_PROGRESS:
            position = seconds_to_time(get_prop("position"))
            length = seconds_to_time(get_prop("length"))
            print_line(f"{START_CHAR}{song_string} ({position} / {length})")
        else:
            print_line(f"{START_CHAR}{song_string}")

        # play/pause status display
        status = get_prop("status")
        if status == "Playing":
            print_line(COLOUR_PLAYING)
        elif status == "Paused":
            print_line(COLOUR_PAUSED)


if __name__ == '__main__':
    main()
