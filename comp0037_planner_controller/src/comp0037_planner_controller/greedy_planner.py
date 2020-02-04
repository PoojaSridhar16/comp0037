# -*- coding: utf-8 -*-

from cell_based_forward_search import CellBasedForwardSearch

class GreedyPlanner(CellBasedForwardSearch):

    # This implements a simple LIFO (last in first out or depth first) search algorithm
    
    def __init__(self, title, occupancyGrid):
        CellBasedForwardSearch.__init__(self, title, occupancyGrid)
        self.lifoQueue = list()

    def getSqDistanceToGoal(self, cell):
        sqDist = (cell.coords[0] - self.goal.coords[0])**2 + (cell.coords[1] - self.goal.coords[1])**2
        return sqDist

    # Simply put on the end of the queue
    def pushCellOntoQueue(self, cell):
        self.lifoQueue.append(cell)
        done = False
        while not done:
            done = True
            for i in range(len(self.lifoQueue) - 1):
                sqDist1 = self.getSqDistanceToGoal(self.lifoQueue[i])
                sqDist2 = self.getSqDistanceToGoal(self.lifoQueue[i + 1])

                if sqDist1 > sqDist2:
                    temp = self.lifoQueue[i]
                    self.lifoQueue[i] = self.lifoQueue[i + 1]
                    self.lifoQueue[i + 1] = temp
                    done = False

    # Check the queue size is zero
    def isQueueEmpty(self):
        return not self.lifoQueue

    # Simply pull from the front of the list
    def popCellFromQueue(self):
        cell = self.lifoQueue.pop(0)
        return cell

    def resolveDuplicate(self, cell, parentCell):
        # Nothing to do in self case
        pass
