import time
from datetime import datetime


def set_alarm(stop_time):
    start_time = datetime.now()
    start_time_formatted = start_time.strftime('%H:%M:%S')
    stop_time_formatted = stop_time.strftime('%H:%M:%S')

    print('Alarm started at {}'.format(start_time_formatted))
    print('Alarm shall stop at {}'.format(stop_time_formatted))

    diff = int((stop_time - start_time).total_seconds())
    m, s = divmod(diff, 60)
    h, m = divmod(m, 60)
    print('Alarm duration: {}:{}:{}'.format(h, m, s))

    # Suspend for those many seconds
    time.sleep(diff)
    print('Wake Up !!!! Alarm is ringing.....!!!')
    return start_time, diff


if __name__ == '__main__':
    user_stop_time = datetime.strptime(input('Alarm stop time HH:MM:SS?'), '%H:%M:%S')
    stop = datetime.now()
    stop = stop.replace(hour=user_stop_time.hour,
                        minute=user_stop_time.minute,
                        second=user_stop_time.second)
    set_alarm(stop)
