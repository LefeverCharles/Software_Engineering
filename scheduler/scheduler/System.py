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

