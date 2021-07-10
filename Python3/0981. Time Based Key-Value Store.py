class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.kvmap = collections.defaultdict(list)
        self.ktmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvmap[key].append(value)
        self.ktmap[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        arr = self.ktmap[key]
        r = len(arr)
        m = -1
        
        while l < r:
            m = (l + r) // 2
            if(arr[m] <= timestamp):
                l = m + 1
            else:
                r = m
        
        return (self.kvmap[key][m] if arr[m] <= timestamp else "") if m != -1 else ""
