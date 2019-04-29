import sys
import time
import numpy as np

class AStarPlanner(object):
    def __init__(self, planning_env):
        self.planning_env = planning_env
        self.nodes = dict()

    def Plan(self, start_config, goal_config):

        plan = []
        epsilon = 1.0
        # TODO (student): Implement your planner here.
        openlist = dict()
        closelist = dict()
        Delta = [[0, 1], [1, 1], [1, 0], [1, -1], [-1, 1], [-1, 0], [-1, -1], [0, -1]]
        openlist[tuple(start_config)] = [0, 0]
        while len(openlist):
            mincost    = float("+inf")
            minconfig  = None
            mincontent = None
            nextconfig = None
            for config, content in openlist.items():
                if content[0] < mincost:
                    mincost = content[0]
                    minconfig = config
                    mincontent = content
            closelist[minconfig] = mincontent
            openlist.pop(minconfig)
            for delta in Delta:
                nextconfig = (np.array(minconfig) + np.array(delta)).tolist()
                if self.planning_env.state_validity_checker(nextconfig) and not closelist.has_key(tuple(nextconfig)):
                    g = closelist[minconfig][1] + self.planning_env.compute_distance(minconfig, nextconfig)
                    if openlist.has_key(tuple(nextconfig)) and openlist[tuple(nextconfig)][1] < g:
                        pass
                    else:
                        cost = g + epsilon * self.planning_env.compute_heuristic(nextconfig)
                        openlist[tuple(nextconfig)] = [cost, g] + list(minconfig)

                if list(nextconfig) == goal_config:
                    break
            if list(nextconfig) == goal_config:
                break
        backtrack = openlist[tuple(goal_config)]
        plan.append(goal_config)
        while len(backtrack) == 4:
            plan.append(backtrack[-2:])
            backtrack = closelist[tuple(backtrack[-2:])]

        plan.reverse()
        return np.array(plan)

    def ShortenPath(self, path):

        # TODO (student): Postprocess the planner.
        return path
