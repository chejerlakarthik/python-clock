from datetime import datetime
import time

class Stopwatch(object):

    def __init__(self):
        self._start_time = None
        self._stop_time = None
        self._elapsed_time = 0

    def start(self):
        self._start_time = datetime.now()
        print('Starting stopwatch @ {}'.format(self._start_time.strftime('%H:%M:%S')))

    def stop(self):
        self._stop_time = datetime.now()
        print('Stopping stopwatch @ {}'.format(self._stop_time.strftime('%H:%M:%S')))
        self._elapsed_time = self._stop_time - self._start_time
        print('Elapsed time is ', int(self._elapsed_time.total_seconds()))

if __name__ == '__main__':
    s = Stopwatch()
    if input('Start Stopwatch? (Press Y)') == 'Y':
        s.start()
    if input('Stop Stopwatch? (Press Y)') == 'Y':
        s.stop()



