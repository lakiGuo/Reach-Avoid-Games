import os
import numpy as np


cmd = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 5                                     \
        --player_types car car car car car                      \
        --init_states                                       \
            7.5 0.0   {} 0.0 3.0                              \
            3.75 40.0 {} 0.0 3.0                            \
            7.5 13.0   {} 0.0 3.0                              \
            3.75 46.0 {} 0.0 3.0                            \
            7.5 6.0   {} 0.0 3.0\
        --draw_roads                                        \
        --block_goal                                        \
            20.0 45.0 20.0 45.0 20.0 55.0 24.0 0.0  20.0 55.0   \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --initial_margin 1.0                                \
        --cost_converge 0.5                               \
        --t_horizon 4.0\
        --match 1\
        ".format(np.pi/1.99, -np.pi/2.01, np.pi/1.99, -np.pi/2.01, np.pi/1.99)

cmd1 = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 5                                     \
        --player_types car car car car car                      \
        --init_states                                       \
            7.5 0.0   {} 0.0 3.0                              \
            3.75 40.0 {} 0.0 3.0                            \
            7.5 13.0   {} 0.0 3.0                              \
            3.75 46.0 {} 0.0 3.0                            \
            7.5 6.0   {} 0.0 3.0\
        --draw_roads                                        \
        --block_goal                                        \
            20.0 45.0 20.0 45.0 20.0 55.0 24.0 0.0  20.0 55.0   \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --initial_margin 1.0                                \
        --cost_converge 0.5                               \
         --log   --store_freq 1                    \
        --t_horizon 4.0\
        --match 1\
        ".format(np.pi/1.99, -np.pi/2.01, np.pi/1.99, -np.pi/2.01, np.pi/1.99)


cmd511 = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 7                                    \
        --player_types car car car car car  car car                    \
        --init_states                                       \
            7.6 0.0   {} 0.0 3.0                              \
             3.5 34.0 {} 0.0 3.0                            \
            3.5 40.0 {} 0.0 3.0                            \
            7.6 15.0   {} 0.0 0.0                              \
            3.5 46.0 {} 0.0 5.0                            \
            7.6 5.0   {} 0.0 1.0                             \
             7.6 10.0   {} 0.0 1.0                             \
        --draw_roads                                        \
        --block_goal                                        \
            20.0 45.0 24.0 0.0 24.0 0.0 20.0 55.0 24.0 0.0 24.0 55.0  20.0 55.0   \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
         --time_consistency                                  \
        --eps_state 0.5 --eps_control 0.3                   \
        --initial_margin 1.0                                \
        --cost_converge 0.5                               \
         --log   --store_freq 1                    \
        --t_horizon 4.0\
        --match 1\
        ".format(np.pi/1.99, -np.pi/2.01, -np.pi/2.01,np.pi/1.99, -np.pi/2.01, np.pi/1.99, np.pi/1.99)

cmd514 = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 4                                   \
        --player_types car car car car            \
        --init_states                                       \
            7.6 0.0   {} 0.0 3.0                              \
             3.5 46.0 {} 0.0 3.0                            \
            3.5 40.0 {} 0.0 3.0                            \
            7.6 13.0   {} 0.0 3.0                              \
        --draw_roads                                        \
        --block_goal                                        \
            20.0 45.0 24.0 0.0 24.0 0.0 20.0 45.0           \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
         --time_consistency                                  \
        --eps_state 0.5 --eps_control 0.3                   \
        --initial_margin 1.0                                \
        --cost_converge 0.5                               \
         --log   --store_freq 1                    \
        --t_horizon 4.0\
        --match 1\
        ".format(np.pi/1.99, -np.pi/2.01, -np.pi/2.01,np.pi/1.99, -np.pi/2.01, np.pi/1.99, np.pi/1.99)


os.system(cmd514)
