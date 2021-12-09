import datetime as dt

class Node:

    def _get_next_day(self):
        year = dt.datetime.now().year
        month = dt.datetime.now().month
        day = dt.datetime.now().day
        return dt.datetime(year, month, day)+dt.timedelta(days=1)

    def __init__(self):
        self.is_gpu = False
        self.available_time = self._get_next_day()
        self.list_of_requests =[]

    def __init__(self, is_gpu):
        self.is_gpu = is_gpu
        self.available_time = self._get_next_day()
        self.list_of_requests =[]

    def add_request(self, request, actual_time):
        self.list_of_requests.append(request)
        self.available_time = actual_time + request.req_time