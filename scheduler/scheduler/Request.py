import Constants as csts
import datetime as dt

class Request:
    def __init__(self, user):
        self.nbr_nodes = 1
        self.req_time = dt.timedelta(hours=1)
        self.req_type = "short"
        self.user = user
        self.time_of_computation = None

    def __init__(self, nbr_nodes, req_time, req_type, user):
        self.nbr_nodes = nbr_nodes
        self.req_time = req_time
        self.req_type = req_type
        self.user = user
        self.time_of_computation = None

    def get_cost(self):
        if self.req_type == "gpu":
            return self.req_time * csts.COST_HOUR_GPU * self.nbr_nodes
        return self.req_time * csts.COST_HOUR_CPU * self.nbr_nodes
