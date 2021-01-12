import random
import sys
# sys.path.append("..\\")
# from util import Util
import math

LOOP_LIMIT = 5000

"""
AStar Class:
    Defininig functions required to perform A star algorithm
"""

class AStar():

    def __init__(self, utility):
        self.utility = utility
        self.player_pos = self.utility.get_player_pos()
        self.wall_pos = self.utility.get_walls_pos()
        self.food_pos = self.utility.get_food_pos()
        self.num_moves = 0
        self.direction = "Right"


    """
    Function to find shortest path using A star algorithm
    returns:
        openListPos (LIST) : list of path which player can follow to reach food
        closedListPos (LIST) : list of positions which player has explored
    """
    def get_next_moves(self):

        g,h,f = 0,0,0

        # yet to travel to these locations
        openList = []
        openListPos = []
        # already visited nodes
        closedList = []
        closedListPos = []

        startNode = Node(self.player_pos, None)
        targetNode = Node(self.food_pos, None)

        openList.append(startNode)
        wallsList = self.wall_pos
        loop_counter = 0

        while len(openList) > 0 :

            if loop_counter > LOOP_LIMIT:
                break

            openList.sort()
            currentNode = openList.pop(0)
            closedList.append(currentNode)
            closedListPos.append(currentNode.position)

            # if reached to goal node
            if currentNode == targetNode:
                path = []
                # travel in reverse order
                while currentNode != startNode:
                    path.append(currentNode.position)
                    currentNode = currentNode.parent
                return path, closedListPos

            (x, y) = currentNode.position

            neighbors = self.utility.near_by_pos(currentNode.position)

            for neighborDir in neighbors:
                neighborPos = self.utility.direction_to_loc(neighborDir, currentNode.position)
                # creating a neighbor node
                neighbor = Node(neighborPos ,currentNode)
                # if neighbour already visited
                if neighbor in closedList:
                    continue

                # calculating euclidean distance for cost estimation
                neighbor.g = self.utility.euclidean_dist(startNode.position, neighbor.position)
                neighbor.h = self.utility.euclidean_dist(neighbor.position, targetNode.position)

                # can use manhattan_dist too
                # neighbor.g = self.utility.manhattan_dist(startNode.position, neighbor.position)
                # neighbor.h = self.utility.manhattan_dist(neighbor.position, targetNode.position)
                neighbor.f = neighbor.g + neighbor.h

                # if neighbour has lower f value and is in openList
                if self.compareTotalVal(openList, neighbor):
                    openList.append(neighbor)
                    openListPos.append(neighbor.position)
                    self.player_pos = neighbor.position
                    loop_counter+=1

        # if no path is found
        return openListPos, closedListPos


    """
    Function to check if neighbour has lower f value and is in openList
    returns:
        boolean: based on f of nodes
    """
    def compareTotalVal(self, openList , neighbor):
        for node in openList:
            if neighbor == node and neighbor.f >= node.f:
                return False
        return True


"""
Node class:
    To create node for A star

    g => represents the distance from current node to start node
    h => represnts the distance from current node to goal node
    f => represents the total cost to travel = g + h
"""

class Node:

    def __init__(self, position:(), parent:()):
        # initalizing all variables with 0 and arguments value
        self.g = 0
        self.h = 0
        self.f = 0
        self.position = position
        self.parent = parent

    def __eq__(self, other):
        # comparing the two nodes
        return self.position == other.position

    def __lt__(self, other):
        # sorting based on total cost values
        return self.f < other.f
