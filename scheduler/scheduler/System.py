import datetime as dt

from Node import *
import Constants as csts

class System:
    def __init__(self):
        self.nodes = []
        for i in range(csts.NBR_NODES_CPU):
            self.nodes.append(Node(False))
        for i in range(csts.NBR_NODES_GPU):
            self.nodes.append(Node(True))

    def get_short_nodes(self):
        return self.nodes[csts.INDEX_NODES_SHORT:csts.INDEX_NODES_MEDIUM]

    def get_medium_nodes(self):
        return self.nodes[csts.INDEX_NODES_MEDIUM:csts.INDEX_NODES_LARGE]

    def get_large_nodes(self):
        return self.nodes[csts.INDEX_NODES_LARGE:csts.NBR_NODES_CPU]

    def get_gpu_nodes(self):
        return self.nodes[csts.NBR_NODES_CPU:]

    def next_cycle_end(self,timestamp):
        fromstartweek = dt.timedelta(days=timestamp.weekday(), hours=timestamp.hour)
        if dt.fromstartweek < dt.timedelta(hours=9):
            return timestamp - fromstartweek + dt.timedelta(hours=9)
        elif fromstartweek < dt.timedelta(days=4, hours=17):
            return timestamp - fromstartweek + dt.timedelta(days=4, hours=17)
        else:
            return timestamp - fromstartweek + dt.timedelta(days=7, hours=9)

    def is_week(self,timestamp):
        fromstartweek = dt.timedelta(days=timestamp.weekday(), hours=timestamp.hour)
        if dt.fromstartweek < dt.timedelta(hours=9):
            return False
        elif fromstartweek < dt.timedelta(days=4, hours=17):
            return True
        else:
            return False

    def get_actual_time(self):
        min = dt.MAXYEAR
        for node in self.nodes:
            if node.available_time < min:
                min = node.available_time
        return min

    def get_available_time(self):
        return self.next_cycle_end(self.get_actual_time()) - self.get_actual_time()

    def get_available_time(self, timestamp):
        min = dt.MAXYEAR
        for node in self.nodes:
            if min > node.available_time > timestamp:
                min = node.available_time
        return self.next_cycle_end(min) - min

    def get_available_nodes(self, timestamp):
        count = []
        for node in self.nodes:
            if node.available_time <= timestamp:
                count.append(node)
        return count

    def get_available_time_short(self):
        min = dt.MAXYEAR
        for node in self.get_short_nodes():
            if node.available_time < min:
                min = node.available_time
        return self.next_cycle_end(min) - min

    def get_available_time_short(self,timestamp):
        min = dt.MAXYEAR
        for node in self.get_short_nodes():
            if timestamp < node.available_time < min:
                min = node.available_time
        return self.next_cycle_end(min) - min

    def get_available_time_medium(self):
        min = dt.MAXYEAR
        for node in self.get_medium_nodes():
            if node.available_time < min:
                min = node.available_time
        return self.next_cycle_end(min) - min

    def get_available_time_medium(self, timestamp):
        min = dt.MAXYEAR
        for node in self.get_medium_nodes():
            if timestamp < node.available_time < min:
                min = node.available_time
        return self.next_cycle_end(min) - min

    def get_available_time_large(self):
        min = dt.MAXYEAR
        for node in self.get_large_nodes():
            if node.available_time < min:
                min = node.available_time
        return self.next_cycle_end(min) - min

    def get_available_time_large(self, timestamp):
        min = dt.MAXYEAR
        for node in self.get_large_nodes():
            if timestamp < node.available_time < min:
                min = node.available_time
        return self.next_cycle_end(min) - min

    def get_available_time_gpu(self):
        min = dt.MAXYEAR
        for node in self.get_gpu_nodes():
            if node.available_time < min:
                min = node.available_time
        return self.next_cycle_end(min) - min

    def get_available_time_gpu(self, timestamp):
        min = dt.MAXYEAR
        for node in self.get_gpu_nodes():
            if timestamp < node.available_time < min:
                min = node.available_time
        return self.next_cycle_end(min) - min

    def get_available_nodes_short(self, timestamp):
        count = []
        for node in self.get_short_nodes():
            if node.available_time <= timestamp:
                count.append(node)
        return count

    def get_available_nodes_medium(self, timestamp):
        count = []
        for node in self.get_medium_nodes():
            if node.available_time <= timestamp:
                count.append(node)
        return count

    def get_available_nodes_large(self, timestamp):
        count = []
        for node in self.get_large_nodes():
            if node.available_time <= timestamp:
                count.append(node)
        return count

    def get_available_nodes_gpu(self, timestamp):
        count = []
        for node in self.get_gpu_nodes():
            if node.available_time <= timestamp:
                count.append(node)
        return count

