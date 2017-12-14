from datetime import datetime
import time

def start_timer(duration=5):

    print('Starting a timer for {} seconds'.format(duration))

    for i in range(duration):
        time.sleep(1)
        print(duration-i)


if __name__ == '__main__':
    duration = int(input('How many seconds? :'))
    start_timer(duration)
    print('Byeee')

