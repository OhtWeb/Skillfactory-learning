class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
    def show_queue(self):
        print(*(self.items))