from datetime import datetime, timedelta


# funkcja obliczająca czas w sekundach do północy
def time_calc_to_midnight():
    # obecna data
    now = datetime.now()
    # data następnej północy
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    # różnica, czas w sekundach do północy
    seconds_to_midnight = (midnight - now).seconds
    return seconds_to_midnight

