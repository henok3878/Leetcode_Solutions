class SnapshotArray:

    def __init__(self, length: int):
        self.d_nums = defaultdict(int)
        self.d_snap = {}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.d_nums[index] = val

    def snap(self) -> int:
        self.d_snap[self.snap_id] = self.d_nums.copy()
        self.snap_id +=1
        return self.snap_id -1
        

    def get(self, index: int, snap_id: int) -> int:
        return self.d_snap[snap_id][index]       


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)