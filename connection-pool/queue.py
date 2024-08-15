from threading import Lock, Condition


class BlockingQueue:
    def __init__(self, maxsize=0):
        self.queue = []
        self.maxsize = maxsize or float('inf')  # Use infinity if maxsize is 0 or None
        self.mutex = Lock()
        self.not_empty = Condition(self.mutex)

    def put(self, item):
        with self.mutex:
            if len(self.queue) < self.maxsize:
                self.queue.append(item)
                self.not_empty.notify()
            else:
                raise Exception("Max pool size reached.")

    def get(self):
        with self.mutex:
            while not self.queue:
                # the Condition's wait releases its underlying mutex, allowing access to other threads
                self.not_empty.wait()
                item = self.queue.pop(0)
            return item
