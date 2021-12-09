class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __int__(self, queue):
        self.queue = queue

    def push(self, request):
        self.queue.insert(0,request)

    def pop_priority(self, available_nodes, remaining):
        for i in range(len(self.queue)):
            if self.queue[len(self.queue)-1-i].get_req_time()<=remaining:
                if self.queue[len(self.queue)-1-i].get_req_nodes()<=available_nodes:
                    result = self.queue[len(self.queue)-1-i]
                    del self.queue[len(self.queue)-1-i]
                    return result
        return False
