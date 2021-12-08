import Request
import Constants as csts


class User:
    def __init__(self, user_name, credit):
        self.user_name = user_name
        self.credit = credit

    def create_request(self, nbr_nodes: int, time: int, req_type: str) -> Request.Request:
        cost = 0
        if type == "gpu":
            cost += time * csts.COST_HOUR_GPU * nbr_nodes
        else:
            cost += time * csts.COST_HOUR_CPU * nbr_nodes
        if self.credit < cost:
            print(cost, "is above the remaining credit of the user.")
        if cost < 0:
            raise ValueError("Cost cannot be below 0.")
        self.credit -= cost
        return Request.Request(nbr_nodes, time, req_type, self)
