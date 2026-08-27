class TimeMap:

    def __init__(self):
        self.seen = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.seen:
            self.seen[key] = []
        self.seen[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        target = timestamp
        l = 0
        if key not in self.seen:
            return ""
        values = self.seen[key]
        h = len(values) - 1
        ans = ""

        while l <= h:
            mid = (l + h) // 2
            val, ts = values[mid]
            if ts == target:
                ans = val
                return ans
            elif ts < target:
                ans = val
                l = mid + 1
            else:
                h = mid - 1
        return ans
        
