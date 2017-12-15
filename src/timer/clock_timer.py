import time


def start_timer(duration=5):
    counting_seconds = 0
    print('Starting a timer for {} seconds'.format(duration))
    for i in range(duration):
        time.sleep(1)
        counting_seconds += 1
    return counting_seconds


if __name__ == '__main__':
    print('Timer ran for {} seconds'.format(start_timer(int(input('How many seconds? :')))))

