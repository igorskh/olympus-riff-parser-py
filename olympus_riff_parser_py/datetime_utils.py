from datetime import datetime


def parse_olympus_timestamps(timestamp_str):
    """
    Parse timestamps from the 'olym' chunk.

    Args:
        timestamp_str: A 24-character string containing two timestamps in YYMMDDHHMMSS format

    Returns:
        tuple: (start_time, end_time) as datetime objects
    """
    if len(timestamp_str) != 24:
        raise ValueError("Timestamp string must be 24 characters long")

    # Split the string into two 12-character timestamps
    start_str = timestamp_str[:12]
    end_str = timestamp_str[12:]

    # Parse each timestamp
    def parse_timestamp(ts_str):
        year = int(ts_str[0:2]) + 2000  # Assuming 20xx format
        month = int(ts_str[2:4])
        day = int(ts_str[4:6])
        hour = int(ts_str[6:8])
        minute = int(ts_str[8:10])
        second = int(ts_str[10:12])

        return datetime(year, month, day, hour, minute, second)

    start_time = parse_timestamp(start_str)
    end_time = parse_timestamp(end_str)

    return start_time, end_time


def format_timestamps(timestamp_str):
    """
    Parse and format Olympus timestamps into human-readable strings.

    Args:
        timestamp_str: A 24-character string containing two timestamps

    Returns:
        tuple: (start_time_str, end_time_str) formatted as "YYYY-MM-DD HH:MM:SS"
    """
    start_time, end_time = parse_olympus_timestamps(timestamp_str)

    start_formatted = start_time.strftime("%Y-%m-%d %H:%M:%S")
    end_formatted = end_time.strftime("%Y-%m-%d %H:%M:%S")

    return start_formatted, end_formatted
