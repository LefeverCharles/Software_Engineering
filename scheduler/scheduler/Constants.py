NBR_NODES_SHORT: int = 12
NBR_NODES_MEDIUM: int = 36
NBR_NODES_LARGE: int = 72
NBR_NODES_GPU: int = 8
COST_HOUR_CPU: int = 60
COST_HOUR_GPU: int = 66

NBR_NODES_CPU: int = NBR_NODES_SHORT + NBR_NODES_MEDIUM + NBR_NODES_LARGE
INDEX_NODES_SHORT: int = 0
INDEX_NODES_MEDIUM: int = NBR_NODES_SHORT
INDEX_NODES_LARGE: int = INDEX_NODES_MEDIUM + NBR_NODES_MEDIUM