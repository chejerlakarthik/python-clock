import unittest
from src.timer import clock_timer
from src.stopwatch.clock_stopwatch import Stopwatch
from src.alarm import clock_alarm
import time
from datetime import datetime, timedelta


class TestClock(unittest.TestCase):

    def setUp(self):
        print('Setting this up...')

    def tearDown(self):
        print('Tearing this down...')

    def test_timer(self):
        self.assertEqual(clock_timer.start_timer(5), 5)
        self.assertEqual(clock_timer.start_timer(2), 2)

    def test_alarm(self):
        now = datetime.now() + timedelta(seconds=10)
        alarm_response = clock_alarm.set_alarm(now)
        duration = int((now - alarm_response[0]).total_seconds())
        self.assertEqual(duration, alarm_response[1])

    def test_stopwatch(self):
        delay = 10
        stopwatch = Stopwatch()
        stopwatch.start()
        time.sleep(delay)
        stopwatch.stop()
        self.assertEqual(stopwatch.elapsed_time(), delay)


if __name__ == '__main__':
    unittest.main()
