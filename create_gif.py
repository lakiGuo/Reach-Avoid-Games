import os
import numpy as np
import matplotlib.pyplot as plt
import imageio

folder_name = "image_outputs_2021-12-07-01_37"
experiment_name = "experiment_result_2021-12-07-01_37"
# Build GIF
image_count = len(os.listdir(folder_name))
with imageio.get_writer('{}.gif'.format(experiment_name), mode='I') as writer:
    for i in range(image_count):
        filename = "plot-{}.jpg".format(i)
        image = imageio.imread(os.path.join(folder_name, filename))
        writer.append_data(image)