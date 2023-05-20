import os
import numpy as np

cmd = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 4                                      \
        --player_types car car car car                       \
        --init_states                                       \
            7.5 0.0   {} 0.0 3.0                              \
            3.75 40.0 {} 0.0 3.0                            \
            7.5 13.0   {} 0.0 3.0                              \
            3.75 46.0 {} 0.0 3.0                            \
        --draw_roads                                        \
        --block_goal                                        \
            20.0 45.0 20.0 45.0 20.0 55.0 24.0 45.0                                    \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --hallucinated                                      \
        --initial_margin 1.0                                \
        --cost_converge 1.0                                 \
        --plot --log --store_freq 1                         \
        --t_horizon 4.0\
        ".format(np.pi/1.99, -np.pi/2.01, np.pi/1.99, -np.pi/2.01)

os.system(cmd)
