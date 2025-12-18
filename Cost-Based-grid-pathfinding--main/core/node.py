class Node:
    def __init__(self, position, g=0, h=0, parent=None):
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
    
    def __lt__(self, other):
        return self.f < other.f    #ovveride that is Used for priority queue for algorithms USC and A* that make the heap(pyhon) compare between nodes  via f not adress 