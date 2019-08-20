import datetime, time

def datetime_to_unix(datetime):
    """Convert python datetime to unix timestamp"""

    return time.mktime(datetime.timetuple())
