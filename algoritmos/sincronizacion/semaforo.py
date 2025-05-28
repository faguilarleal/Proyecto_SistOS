
class Semaphore:
    def __init__(self, count):
        self.count = count
        self.queue = []

    def wait(self, pid):
        if self.count > 0:
            self.count -= 1
            return True
        self.queue.append(pid)
        return False

    def signal(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            self.count += 1
            return None
