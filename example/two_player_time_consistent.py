import os
import numpy as np



cmd14 = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 2                                      \
        --player_types car car                              \
        --init_states                                       \
            7.6 5.0 {} 0.0 3.0                              \
            3.5 46.0 {} 0.0 3.0                           \
        --block_goal \
            20.0 49.0 24.0 0.0   \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --initial_margin 1.0                                \
        --cost_converge 0.1                           \
         --log --store_freq 1  \
        --time_consistency  \
        --t_horizon 4.0\
        --max_steps 1000\
        ".format(np.pi/1.99, -np.pi/2.02)


cmd13 = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 2                                      \
        --player_types car car                              \
        --init_states                                       \
            7.5 15.0 {} 0.0 7.0                              \
            3.75 34.0 {} 0.0 3.0                           \
        --block_goal \
            20.0 49.0 24.0 0.0   \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --initial_margin 1.0                                \
        --cost_converge 0.1                           \
         --log --store_freq 1  \
        --time_consistency  \
        --t_horizon 4.0\
        --max_steps 1000\
        ".format(np.pi/1.99, -np.pi/2.02)


cmd = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 2                                      \
        --player_types car car                              \
        --init_states                                       \
            7.5 13.0 {} 0.0 0.0                              \
            3.75 40.0 {} 0.0 7.0                           \
        --block_goal \
            20.0 55.0 24.0 0.0   \
        --draw_roads\
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --initial_margin 1.0                                \
        --cost_converge 0.1                           \
        --plot --log --store_freq 1  \
        --time_consistency  \
        --t_horizon 4.0\
        --max_steps 1000\
        ".format(np.pi/1.99, -np.pi/2.01)


cmd12 = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 2                                      \
        --player_types car car                              \
        --init_states                                       \
            7.5 13.0 {} 0.0 3.0                              \
            3.75 40.0 {} 0.0 3.0                           \
        --block_goal \
            20.0 55.0 24.0 0.0   \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --initial_margin 1.0                                \
        --cost_converge 0.8                           \
        --log \
        --time_consistency  \
        --t_horizon 4.0\
        --max_steps 1000\
        ".format(np.pi/1.99, -np.pi/2.01)


cmd11 = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 2                                      \
        --player_types car car                              \
        --init_states                                       \
            7.5 0.0 {} 0.0 3.0                              \
            3.75 46.0 {} 0.0 3.0                           \
        --block_goal \
            20.0 45.0 24.0 0.0   \
        --draw_roads                                        \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --hallucinated                                      \
        --initial_margin 1.0                                \
        --cost_converge 0.5                           \
        --plot --log --store_freq 1                         \
        --time_consistency  \
        --t_horizon 4.0\
        --max_steps 1000\
        ".format(np.pi/1.99, -np.pi/2.01)
cmd1 = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 2                                      \
        --player_types car car                              \
        --init_states                                       \
            7.5 13.0 {} 0.0 3.0                              \
            3.75 40.0 {} 0.0 3.0                           \
        --block_goal \
            20.0 55.0 24.0 0.0   \
        --draw_roads                                        \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --hallucinated                                      \
        --initial_margin 1.0                                \
        --cost_converge 0.8                           \
        --plot --log --store_freq 1                         \
        --time_consistency  \
        --t_horizon 4.0\
        --max_steps 1000\
        ".format(np.pi/1.99, -np.pi/2.01)

cmd2 = "python run.py                                       \
        --env_type t_intersection                           \
        --no_players 2                                      \
        --player_types car car                              \
        --init_states                                       \
            7.5 0.0 {} 0.0 3.0                              \
            3.75 46.0 {} 0.0 3.0                           \
        --block_goal \
            20.0 45.0 24.0 0.0   \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --boundary_only                                     \
        --eps_state 0.5 --eps_control 0.3                   \
        --initial_margin 1.0                                \
        --cost_converge 0.5                           \
        --log                       \
        --time_consistency  \
        --t_horizon 4.0\
        --max_steps 1000\
        ".format(np.pi/1.99, -np.pi/2.01)

# --draw_roads --draw_human --draw_cars
# --time_consistency
#
# os.system(cmd11)
os.system(cmd14)
