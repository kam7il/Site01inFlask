from datetime import datetime, timedelta, timezone


# function that calculates the time in seconds to midnight
def time_calc_to_midnight_utc():
    # current date
    now = datetime.now(timezone.utc)
    # next midnight date
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    # difference, time in seconds to midnight
    seconds_to_midnight = (midnight - now).seconds
    return seconds_to_midnight

