import numpy
from IPython import embed
import math
from matplotlib import pyplot as plt

class MapEnvironment(object):

    def __init__(self, mapfile, start, goal):

        # Obtain the boundary limits.
        # Check if file exists.
        self.map = numpy.loadtxt(mapfile)
        self.xlimit = [1, numpy.shape(self.map)[0]] # TODO (avk): Check if this needs to flip.
        self.ylimit = [1, numpy.shape(self.map)[1]]
        print self.map[1,2], self.map[4,7]
        self.start = start
        self.goal  = goal

        # Check if start and goal are within limits and collision free
        if not self.state_validity_checker(start) or not self.state_validity_checker(goal):
            raise ValueError('Start and Goal state must be within the map limits');
            exit(0)

        # Display the map
        plt.imshow(self.map, interpolation='nearest')

    def compute_distance(self, start_config, end_config):

        #
        # TODO: Implement a function which computes the distance between
        # two configurations.
        #
        return math.sqrt((start_config[0] - end_config[0])**2 + (start_config[1] - end_config[1])**2)


    def state_validity_checker(self, config):

        #
        # TODO: Implement a state validity checker
        # Return true if valid.
        #
        if self.xlimit[0] <= config[0] <= self.xlimit[1] and self.ylimit[0] <= config[1] <= self.ylimit[1] and not self.map[config[0]-1, config[1]-1]:
            return True
        else:
            return False

    def edge_validity_checker(self, config1, config2):

        #
        # TODO: Implement an edge validity checker
        #
        #
        if self.map[config1[0], config1[1]] or self.map[config2[0], config2[1]]:
            return False
        else:
            return True

    def compute_heuristic(self, config):

        #
        # TODO: Implement a function to compute heuristic.
        #
        return math.sqrt((config[0] - self.goal[0])**2 + (config[1] - self.goal[1])**2)

    def visualize_plan(self, plan):
        '''
        Visualize the final path
        @param plan Sequence of states defining the plan.
        '''
        plt.imshow(self.map, interpolation='nearest')
        for i in range(numpy.shape(plan)[0] - 1):
            x = [plan[i,0]-1, plan[i+1, 0]-1]
            y = [plan[i,1]-1, plan[i+1, 1]-1]
            plt.plot(y, x, 'k')
        plt.show()
