from datetime import datetime
import time


def timestamp():
    # Get the current timestamp
    timestamp = datetime.now()

    # Format the timestamp as a string
    formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_timestamp


