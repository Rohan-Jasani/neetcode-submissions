from bisect import bisect_right
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self._map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self._map[key]

        idx = bisect_right(values, timestamp, key=lambda x: x[0])

        if idx == 0:
            return ''

        return values[idx - 1][1]
