# -*- coding: utf-8 -*-
"""
Created on Sat May 20 16:36:22 2023

@author: pot13
"""

import queue
import pickle
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from scipy.interpolate import CubicSpline
from matplotlib.transforms import Affine2D
from collections import deque
import imageio

exp_name = "experiment_2023-05-14-12_19_01"


def file_open(name,logs):
    f = open('./result/'+name+'/'+logs+'/experiment.pkl', 'rb')
    return f

def read_from_pickle(f):
    data = pickle.load(f)
    xs = data["xs"]
    return xs

def draw_road_rules(road_rules, ax):

    x_max = 25
    # y_max
    y_max = 50

    y_min = -5

    # plot road rules
    x_center = road_rules["x_min"] + 0.5 * \
        (road_rules["x_max"] - road_rules["x_min"])
    y_center = road_rules["y_min"] + 0.5 * \
        (road_rules["y_max"] - road_rules["y_min"])

    # plot border
    plt.plot([road_rules["x_min"], road_rules["x_min"]], [
        y_min, y_max], c="white", linewidth=2, zorder=-1)
    plt.plot([road_rules["x_max"], road_rules["x_max"]], [
        y_min, road_rules["y_min"]], c="white", linewidth=2, zorder=-1)
    plt.plot([road_rules["x_max"], road_rules["x_max"]], [
        road_rules["y_max"], y_max], c="white", linewidth=2, zorder=-1)
    plt.plot([road_rules["x_max"], x_max], [road_rules["y_min"],
                                            road_rules["y_min"]], c="white", linewidth=2, zorder=-1)
    plt.plot([road_rules["x_max"], x_max], [road_rules["y_max"],
                                            road_rules["y_max"]], c="white", linewidth=2, zorder=-1)

    # plot background
    plt.fill_between([0, road_rules["x_min"]], [y_min, y_min], [
        y_max, y_max], color="#7f7f7f", edgecolor='none', alpha=0.6, zorder=-1)
    plt.fill_between([road_rules["x_max"], x_max], [road_rules["y_max"], road_rules["y_max"]], [
        y_max, y_max], color="#7f7f7f", edgecolor='none', alpha=0.6, zorder=-1)
    plt.fill_between([road_rules["x_max"], x_max], [y_min, y_min], [
        road_rules["y_min"], road_rules["y_min"]], color="#7f7f7f", edgecolor='none', alpha=0.6, zorder=-1)

    plt.plot([x_center, x_center], [y_min, y_max], "--",
             c='white', linewidth=5, dashes=(5, 5), zorder=-1)

    plt.plot([road_rules["x_max"], x_max], [y_center, y_center],
             "--", c='white', linewidth=5, dashes=(5, 5), zorder=-1)
    # color the region in grey color
    # between x_min and x_max length 0 to y_max
    # 置于底层，保留前面的图像
    plt.fill_between([road_rules["x_min"], road_rules["x_max"]], [y_min, y_min], [
        y_max, y_max], color="#bcbcbc", edgecolor='none', alpha=0.6, zorder=-1)

    # color the region in grey color
    # between road_rules["y_min"] and road_rules["y_max"] length:road_rules["x_min"] to x_max
    # 取消边界颜色

    plt.fill_between([road_rules["x_max"], x_max], [road_rules["y_min"], road_rules["y_min"]], [
        road_rules["y_max"], road_rules["y_max"]], color="#bcbcbc", edgecolor='none', alpha=0.6, zorder=-1)


def draw_matching_area(road_rules, ax):
    x_max = 25
    # y_max
    y_max = 50

    # plot road rules
    xc = road_rules["x_min"] + 0.5 * \
        (road_rules["x_max"] - road_rules["x_min"])
    yc = road_rules["y_min"] + 0.5 * \
        (road_rules["y_max"] - road_rules["y_min"])
    # go straight
    # pick: #f4dde0
    # deep pick #ce6872
    ys_min = 3
    ys_max = 20
    # add arrows to explain the matching area and add text

    plt.fill_between([xc, road_rules["x_max"]], [ys_min, ys_min], [
        ys_max, ys_max], color="#de9aa1", edgecolor='none', alpha=0.6, zorder=-1)
    # turn left
    yl_min = 30
    yl_max = 48
    plt.fill_between([road_rules["x_min"], xc], [yl_min, yl_min], [
        yl_max, yl_max], color="#dce7bf", edgecolor='none', alpha=0.6, zorder=-1)
    
    
    
def draw_single_real_car(car_states, k, color="white", path=None):
    # TODO: change all the constants in the function to car_params
    car_params = {
        "wheelbase": 2.413,
        "length": 4.267,
        "width": 1.988
    }
    if k == 0:
        state = car_states[0][:5].flatten()
    else:
        state = car_states[0][5:10].flatten()

    if(color == 'r'):
        color = "r"
        path = "visual_components/car_robot_r.png" if path is None else path
    elif color == 'y':

        color = "y"
        path = "visual_components/car_robot_y.png" if path is None else path
    elif color == 'pink':

        color = 'pink'
        path = "visual_components/car_robot_pink.png" if path is None else path
    elif color == 'white':

        color = "white"
        path = "visual_components/delorean-flux-white.png" if path is None else path
    elif color == 'blue':

        color = "blue"
        path = "visual_components/delorean-flux-blue.png" if path is None else path
    elif color == 'purple':

        color = "purple"
        path = "visual_components/delorean-flux-purple.png" if path is None else path
    elif color == 'grey':

        color = "grey"
        path = "visual_components/delorean.png" if path is None else path

    i = 0
    transform_data = Affine2D().rotate_deg_around(
        *(state[0], state[1]), state[2]/np.pi * 180) + plt.gca().transData
    # plt.plot(state[0], state[1], color=color, marker='o', markersize=5, alpha = 0.4)
    # numpy.real(A)
    if i % 5 == 0:
        # A=plt.imread(path, format="png").astype(float)
        im = plt.imshow(
            plt.imread(path, format="png").astype(float),
            transform=transform_data,
            interpolation='none',
            origin='lower',
            extent=[state[0] - 0.927, state[0] + 3.34,
                    state[1] - 0.944, state[1] + 1.044],
            alpha=1,
            # alpha=(1.0/len(car_states))*i
            clip_on=True)
    return im



f0= file_open(exp_name,"logs0")
f1 = file_open(exp_name,"logs1")

xs0=read_from_pickle(f0)
xs1=read_from_pickle(f1)

n_step0 = len(xs0)
n_step1 = len(xs1)

xs_last0 = xs0[n_step0-1]
xs_last1 = xs1[n_step1-1]
t_step0 = len(xs_last0)
t_step1 = len(xs_last1)

T=t_step0

car_params = {
    "wheelbase": 2.413,
    "length": 4.267,
    "width": 1.988
}

road_rules = {
    "x_min": 2,
    "x_max": 9.4,
    "y_max": 27.4,
    "y_min": 20,
    "width": 3.7
}

fig, ax = plt.subplots()

draw_road_rules(road_rules, ax)
ax.set_xlim(0, 25)
ax.set_ylim(-5, 50)
ims=[]
for i in range(t_step0+t_step1):
        ax.cla()  # clear trajectory
        ax.set_xlim(0, 25)
        ax.set_ylim(-5, 50)
        draw_road_rules(road_rules, ax)
        draw_matching_area(road_rules, ax)
        # draw_roads(road_rules, 50, 25)
        if(i < t_step0 and xs_last0[i][1] < 27.4):
            draw_single_real_car([xs_last0[i]], k=1, color="r")
            draw_single_real_car([xs_last0[i]], k=0, color="white")
            draw_single_real_car([xs_last1[0]], k=1, color="y")
            draw_single_real_car([xs_last1[0]], k=0, color="grey")
            t_key=i
        elif(i< t_step0 and xs_last0[i][1] >= 27.4):
            draw_single_real_car([xs_last0[i]], k=1, color="r")
            draw_single_real_car([xs_last0[i]], k=0, color="white")
            draw_single_real_car([xs_last1[i-t_key-1]], k=1, color="y")
            draw_single_real_car([xs_last1[i-t_key-1]], k=0, color="grey")
        elif(i >= t_step0 and i-t_key-1 < t_step1):
            draw_single_real_car([xs_last1[i-t_key-1]], k=1, color="y")
            draw_single_real_car([xs_last1[i-t_key-1]], k=0, color="grey")
        elif(i-t_key-1 >= t_step1):
            break    
        plt.pause(0.01)
        plt.savefig(f"./result_pics/experiment_2023-05-14-12_19_01/frame_{i}.png")
        ims.append(imageio.imread(f"./result_pics/experiment_2023-05-14-12_19_01/frame_{i}.png"))

imageio.mimsave('./experiment.gif', ims, fps=20)

