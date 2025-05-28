class Mutex:
    def __init__(self):
        self.locked = False
        self.owner = None

    def acquire(self, pid):
        if not self.locked:
            self.locked = True
            self.owner = pid
            return True
        return False

    def release(self, pid):
        if self.locked and self.owner == pid:
            self.locked = False
            self.owner = None
            return True
        return False

