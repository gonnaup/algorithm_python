from time import time


class Stopwatch:
    """
    计时器
    """

    def __init__(self):
        self._start = time() * 1000
        self._end = 0

    def stop(self) -> int:
        self._end = time() * 1000
        return round(self._end - self._start)
