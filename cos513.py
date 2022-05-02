import os
import numpy as np
import pickle

human_pos = []
for i in range(50, 30, -2):
        human_pos.append((16.0, float(i)))
for i in range(16, 50):
        human_pos.append((float(i), 30.0))
for i in range(30, 0, -2):
        human_pos.append((50.0, float(i)))

for i, pos in enumerate(human_pos):
        list_exps = os.listdir("result")
        if len(list_exps) > 0:
                most_recent_exp = list_exps[-1]
                loadpath = os.path.join("result", most_recent_exp)
                # get experiment file:
                file_list = os.listdir(os.path.join(loadpath, "logs"))
                print("\t>> Found {} file(s)".format(len(file_list)))

                if len(file_list) > 1:
                        index = input("Please choose which log file to use: ")
                else: 
                        index = 0

                # Read log
                file_path = os.path.join(loadpath, "logs", file_list[index])
                raw_data = pickle.load(open(file_path, "rb"))

                final_traj = raw_data["xs"][-1]
                final_pos_wrt_time = final_traj[i]
                x = round(final_pos_wrt_time[0][0], 2)
                y = round(final_pos_wrt_time[1][0], 2)
                theta = round(final_pos_wrt_time[2][0], 2)
                phi = round(final_pos_wrt_time[3][0], 2)
                v = 5.0 # prevent the previous v to explode
        else:
                x = 0.0
                y = 0.0
                theta = np.pi/4.0
                phi = 0.0
                v = 5.0
        
        command = "python3 run.py                                           \
                        --env_type goal_with_obs                            \
                        --init_states {} {} {} {} {}                        \
                        --no_players 1                                      \
                        --obstacles                                         \
                                {} {} 3.0                                   \
                        --goal 50.0 50.0 2.0                                \
                        --time_consistency                                  \
                        --alpha_scaling trust_region                        \
                        --trust_region_type ratio                           \
                        --initial_margin 5.0                                \
                        --t_horizon {}                                      \
                        --eps_control 0.1 --eps_state 0.1                   \
                        --hallucinated                                      \
                        --plot --log                                        \
                        ".format(x, y, theta, phi, v, pos[0], pos[1], (50-i)*0.1)

        os.system(command)