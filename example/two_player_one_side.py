import os
import numpy as np

cmd = "python3 run.py                                       \
        --env_type t_intersection                           \
        --no_players 2                                      \
        --player_types car car                              \
        --init_states                                       \
            7.5 0.0 {} 0.0 9.0                              \
            3.75 40.0 {} 0.0 7.0                            \
        --draw_roads                                        \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --hallucinated                                      \
        --initial_margin 2.0                                \
        --cost_converge 0.8                                 \
        --plot --log --store_freq 1                         \
        ".format(np.pi/1.99, -np.pi/2.01)

# --draw_roads --draw_human --draw_cars

cmd2 = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 2                                      \
        --player_types car car                              \
        --init_states                                       \
            7.5 0.0 {} 0.0 5.0                              \
            7.5 7.0 {} 0.0 5.0                             \
        --block_goal                                       \
            20.0 45.0 20.0 35.0                             \
        --draw_roads                                        \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --hallucinated                                      \
        --initial_margin 1.0                                \
        --cost_converge 0.8                                 \
        --plot --log --store_freq 1                         \
        --time_consistency                                  \
        --t_horizon  4.0\
        --one_side  1\
        --max_steps 300\
        ".format(np.pi/1.99, np.pi/1.99)

# --draw_roads --draw_human --draw_cars


os.system(cmd2)
