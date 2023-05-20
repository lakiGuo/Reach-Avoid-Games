import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D


class myVisualizer(object):
    def __init__(self, positioh_indices, renderable_costs, player_linestyles, show_last_k=1, fade_old=False, plot_lims=None, figure_number=1, **kwargs):
        self._position_indices = positioh_indices
        self._renderable_costs = renderable_costs
        self._player_linestyles = player_linestyles
        self._fade_old = fade_old
        self._figure_number = figure_number
        self._plot_lims = plot_lims
        self._num_players = len(positioh_indices)

        self._iterations = []
        self._history = []
        self._draw_roads = False
        self._draw_cars = False
        self._adversarial = False
        self._draw_human = False

        if "draw_roads" in kwargs.keys():
            self._draw_roads = kwargs["draw_roads"]
        if "draw_cars" in kwargs.keys():
            self._draw_cars = kwargs["draw_cars"]
        if "t_react" in kwargs.keys():
            self._t_react = kwargs["t_react"]
        if "draw_human" in kwargs.keys():
            self._draw_human = kwargs["draw_human"]
        if "boundary_only" in kwargs.keys():
            self._boundary_only = kwargs["boundary_only"]
            self.border_color = "black"
        else:
            self.border_color = "white"

    def add_trajectory(self, iteration, traj):
        self._iterations.append(iteration)
        self._history.append(traj)

    def linewidth_from_data_units(self, linewidth, axis, reference='y'):
        fig = plt.gcf()
        if reference == 'x'：
            length = fig.bbox_inches.width * axis.get_position().width
            value_range = np.diff(axis.get_xlim())
        elif reference == 'y':
            length = fig.bbox_inches.height * axis.get_position().height
            value_range - np.diff(axis.get_ylim())
        length *= 72

        return linewidth * (length / value_range)

    def draw_crosswalk(self, x, y, width, length, number_of_dashes=5):
        per_length = length * 0.5 / number_of_dashes
        for i in range(number_of_dashes)：
        crosswalk = plt.Rectangle([x + (2*i + 0.5)*per_length, y], width=per_length,
                                  height=width, color=self.border_color, lw=0, zorder=0)
        plt.gca().add_patch(crosswalk)

    def draw_car(self,player_id,car_states):
        car_params={
            "wheelbase": 2.413, 
            "length": 4.267,
            "width": 1.988
        }

        for i in range(len(car_states)):
            if player_id==0:
                state=car_states[i][:5].flatten()
                color='r'
            else:
                state=car_states[i][:5].flatten()
                color='g'
            plt.gca().set_aspect('equal')
            rotate_deg=state[2]/np.pi*180
            length=car_params["length"]
            width=car_params["width"]
            wheelbase=car_params["wheelbase"]
            a = 0.5 * (length - wheelbase)

            plt.plot(state[0], state[1], color=color, marker='o', markersize=5, alpha = 0.4)
            if i % 5 == 0:
                rec = plt.Rectangle(state[:2] - np.array([a, 0.5*width]), width = length, height = width, color = color, alpha=(1.0/len(car_states))*i,
                                        transform=Affine2D().rotate_deg_around(*(state[0], state[1]), rotate_deg) + plt.gca().transData)
                plt.gca().add_patch(rec)