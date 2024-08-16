from threading import Lock, Condition


class BlockingQueue:
    def __init__(self, maxsize=0):
        self.queue = []
        self.maxsize = maxsize or float('inf')  # Use infinity if maxsize is 0 or None
        self.mutex = Lock()
        self.current_size = 0
        self.not_empty = Condition(self.mutex)
        self.not_full = Condition(self.mutex)

    def put(self, item):
        with self.mutex:
            while self.current_size >= self.maxsize:
                self.not_full.wait()
            self.queue.append(item)
            self.current_size = self.current_size + 1
            self.not_empty.notify()

    def get(self):
        with self.mutex:
            while not self.queue:
                # the Condition's wait releases its underlying mutex, allowing access to other threads
                self.not_empty.wait()
            item = self.queue.pop(0)
            return item

    def put_back(self, item):
        with self.mutex:
            self.queue.append(item)
            self.not_empty.notify()

    def delete(self, item):
        with self.mutex:
            print(f"Item {item} deleted from queue")
            self.current_size = self.current_size - 1
            self.not_full.notify()
