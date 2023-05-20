import os
import numpy as np






cmd = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 1                                     \
        --player_types car                              \
        --init_states                                       \
            7.6 0.0 {} 0.0 3.0                              \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --initial_margin 1.0                                \
        --cost_converge 0.1                                 \
        --log --store_freq 1                         \
        --time_consistency                                  \
        ".format(np.pi/1.99)


cmd11 = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 1                                     \
        --player_types car                              \
        --init_states                                       \
            7.5 10.0 {} 0.0 3.0                              \
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
        ".format(np.pi/1.99)


cmd1 = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 1                                     \
        --player_types car                              \
        --init_states                                       \
            3.75 40.0 {} 0.0 3.0                              \
        --draw_roads                                        \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --hallucinated                                      \
        --initial_margin 1.0                                \
        --cost_converge 0.3                                 \
        --plot --log --store_freq 1                         \
        --time_consistency                                  \
        --t_horizon 5.0\
        ".format(-np.pi/2.01)

# --draw_roads --draw_human --draw_cars

os.system(cmd)
