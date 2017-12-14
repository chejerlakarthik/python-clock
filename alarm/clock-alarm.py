from datetime import datetime, timedelta
import time

def start_alarm(stop_time):
    start_time = datetime.now()
    print('Alarm started at {}'.format(start_time.strftime('%H:%M:%S')))

    print('Alarm shall stop at {}'.format(stop_time.strftime('%H:%M:%S')))

    diff = int((stop_time - start_time).total_seconds())
    m, s = divmod(diff, 60)
    h, m = divmod(m, 60)
    print('Alarm duration: {}:{}:{}'.format(h,m,s))

    #Suspend for those many seconds
    time.sleep(diff)

    print('Wake Up !!!! Alarm is ringing.....!!!')

if __name__ == '__main__':
    print('Current time is ', datetime.now().time())
    user_stop_time = datetime.strptime(input('Alarm stop time HH:MM:SS?'),'%H:%M:%S')
    stop_time = datetime.now()
    stop_time = stop_time.replace(hour=user_stop_time.hour,
                                  minute=user_stop_time.minute,
                                  second=user_stop_time.second)
    start_alarm(stop_time)
