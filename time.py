# 07.03.2017
# a little fun with timezones
# eventhough timezones aren't fun at all

from datetime import datetime
import pytz

TIMEZONES = [
    pytz.timezone("US/Eastern"),
    pytz.timezone("Pacific/Auckland"),
    pytz.timezone("Asia/Calcutta"),
    pytz.timezone("UTC"),
    pytz.timezone("Europe/Paris"),
    pytz.timezone("Africa/Khartoum")
]

fmt = '%Y-%m-%d %H:%M:%S %Z%z'

while True:
    date_input = input("""When is the meeting? Please use
MM/DD/YYYY HH:MM format\n""")
    try:
        local_date = datetime.strptime(date_input, "%m/%d/%Y %H:%M")
    except ValueError:
        print("{} is not a valid date and time".format(date_input))
    else:
        local_date = pytz.timezone("Europe/Berlin").localize(local_date)
        utc_date = local_date.astimezone(pytz.utc)

        output = []
        for timezone in TIMEZONES:
            output.append(utc_date.astimezone(timezone))
        for appointment in output:
            print(appointment.strftime(fmt))

        break
