################################################################################
#
# Iterative LQ solver.
#
################################################################################

import numpy as np
import math as m
import torch
import matplotlib.pyplot as plt
import os
from collections import deque

from cost.maneuver_penalty import ManeuverPenalty
from ilq_solver.base_solver import BaseSolver
from player_cost.player_cost import PlayerCost
from cost.proximity_to_block_cost import ProximityToLeftBlockCost, ProximityToUpBlockCost
from cost.pedestrian_proximity_to_block_cost import PedestrianProximityToBlockCost
from cost.collision_penalty import CollisionPenalty
from cost.pedestrian_collision_penalty import PedestrianToCarCollisionPenalty
from cost.road_rules_penalty import RoadRulesPenalty
from solve_lq_game.solve_lq_game import solve_lq_game
import time
timestr = time.strftime("%Y-%m-%d-%H_%M")

class ILQSolver(BaseSolver):
    def __init__(self,
                 dynamics,
                 player_costs,
                 x0,
                 Ps,
                 alphas,
                 alpha_scaling= 1.0, # 0.01,
                 reference_deviation_weight=None,
                 logger=None,
                 visualizer=None,
                 u_constraints=None,
                 config=None):
        """
        Initialize from dynamics, player costs, current state, and initial
        guesses for control strategies for both players.

        :param dynamics: two-player dynamical system
        :type dynamics: TwoPlayerDynamicalSystem
        :param player_costs: list of cost functions for all players
        :type player_costs: [PlayerCost]
        :param x0: initial state
        :type x0: np.array
        :param Ps: list of lists of feedback gains (1 list per player)
        :type Ps: [[np.array]]
        :param alphas: list of lists of feedforward terms (1 list per player)
        :type alphas: [[np.array]]
        :param alpha_scaling: step size on the alpha
        :type alpha_scaling: float
        :param reference_deviation_weight: weight on reference deviation cost
        :type reference_deviation_weight: None or float
        :param logger: logging utility
        :type logger: Logger
        :param visualizer: optional visualizer
        :type visualizer: Visualizer
        :param u_constraints: list of constraints on controls
        :type u_constraints: [Constraint]
        """
        super().__init__(dynamics, player_costs, x0, Ps, alphas, alpha_scaling, reference_deviation_weight, logger, visualizer, u_constraints, config)
    
    def set_player_cost_derivative(self, func_key_list, l_func_list, g_func_list, k, player_index, calc_deriv_cost, is_t_star):
        if is_t_star:
            if func_key_list[k] == "l_x":
                c1gc = l_func_list[k]
                self._player_costs[player_index].add_cost(c1gc, "x", 1.0)
                calc_deriv_cost.appendleft("True")
                self.calc_deriv_cost = True
            elif func_key_list[k] == "g_x":
                c1gc = g_func_list[k]
                self._player_costs[player_index].add_cost(c1gc, "x", 1.0)
                calc_deriv_cost.appendleft("True")
                self.calc_deriv_cost = True
            else:
                c1gc = g_func_list[k]
                self._player_costs[player_index].add_cost(c1gc, "x", 0.0)
                calc_deriv_cost.appendleft("False")
                self.calc_deriv_cost = False
        else:
            if func_key_list[k] == "l_x":
                c1gc = l_func_list[k]
                self._player_costs[player_index].add_cost(c1gc, "x", 0.0)
                calc_deriv_cost.appendleft("False")
                self.calc_deriv_cost = False
            elif func_key_list[k] == "g_x":
                c1gc = g_func_list[k]
                self._player_costs[player_index].add_cost(c1gc, "x", 0.0)
                calc_deriv_cost.appendleft("False")
                self.calc_deriv_cost = False
            else:
                c1gc = g_func_list[k]
                self._player_costs[player_index].add_cost(c1gc, "x", 0.0)
                calc_deriv_cost.appendleft("False")
                self.calc_deriv_cost = False
        return calc_deriv_cost, c1gc