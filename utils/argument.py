import argparse
from random import choices


def get_argument():
    parser = argparse.ArgumentParser()

    # experiment params
    parser.add_argument("--no_players",
                        help="Number of players",       type=int,       default=1)
    parser.add_argument("--time_consistency",
                        help="Is the run time consistent",  action="store_true")
    # parser.add_argument("--adversarial",        help="Is the run adversarial",      action="store_true")

    parser.add_argument("--batch_run",
                        help="Experiment is running in batch",          action="store_true")

    parser.add_argument(
        "--t_react",            help="T reaction for adversarial case",     type=int)
    parser.add_argument(
        "--one_side",            help="T reaction for one side case",    type=int)
    parser.add_argument("--t_horizon",          help="Time horizon for the traj",
                        type=float,     default=3.0)
    parser.add_argument("--t_resolution",
                        help="Time react",       type=float,     default=0.1)

    parser.add_argument("--cost_converge",      help="Cost threshold to be considered as converged",
                        type=float,     default=0.0)

    parser.add_argument("--exp_name",
                        help="Name of experiment",              default="experiment")
    parser.add_argument("--player_types",
                        help="List of player types car/ped",    default=["car"],    nargs="*")
    parser.add_argument("--init_states",        help="Init states for all players",
                        default=[0.0, 0.0, 0.0, 0.0, 0.0], type=float, nargs="*")

    parser.add_argument("--env_type",           help="Type of environment",
                        default=None,       choices=["goal_with_obs", "t_intersection"])
    parser.add_argument("--alpha_scaling",      help="Method to do alpha scaling",
                        default=None,       choices=["armijo", "trust_region", "iterative"])
    parser.add_argument("--trust_region_type",  help="Type of trust region to run",
                        default="naive",   choices=["naive", "conservative", "ratio", "constant_margin"])
    parser.add_argument("--initial_margin",
                        help="Initial margin for trust region",         type=float,     default=5.0)

    parser.add_argument("--eps_state",          help="Epsilon state for Player Cost",
                        type=float,     default=0.1)
    parser.add_argument("--eps_control",
                        help="Epsilon control for Player Cost",         type=float,     default=0.1)

    parser.add_argument("--max_steps",
                        help="Max steps to run before termination regardless of convergence",   type=int,     default=1000)
    # parser.add_argument(
    #     "--turnleft", help="turn left",     type=int)

    # if goal_with_obs is chosen for env_type
    parser.add_argument("--obstacles",          help="List of obstacle in format [x, y, r]",    default=[
                        6.0, 25.0, 4.0], type=float, nargs="*")
    parser.add_argument("--goal",               help="Goal information in format [x, y, r]",    default=[
                        6.0, 40.0, 2.0], type=float, nargs="*")
    # if t_intersection is chosen for env_type
    parser.add_argument("--block_goal",         help="Block goal for players [goal_x_p1, goal_y_p1, goal_x_p2, goal_y_p2, ...]",    default=[
                        20.0, 35.0, 20.0, 0.0], type=float, nargs="*")

    parser.add_argument(
        "--match",         help="employ match policy",    type=int)
    # solver params
    parser.add_argument(
        "--log",                help="Turn on log for exp",             action="store_true")
    parser.add_argument("--store_freq",
                        help="Logging frequency",               type=int, default=5)
    parser.add_argument(
        "--plot",               help="Turn on plot for exp",            action="store_true")
    parser.add_argument("--vel_plot",
                        help="Turn on vel plot for exp",        action="store_true")
    parser.add_argument("--ctl_plot",
                        help="Turn on ctl plot for exp",        action="store_true")
    parser.add_argument("--boundary_only",
                        help="Only plot boundary of roads",     action="store_true")
    parser.add_argument("--hallucinated",
                        help="Plot hallucinated trajectory",    action="store_true")

    # visualize params
    parser.add_argument(
        "--draw_cars",    help="Draw cars instead of points",    action="store_true")
    parser.add_argument("--draw_roads",   help="Draw roads",
                        action="store_true")
    parser.add_argument("--draw_human",   help="Draw human",
                        action="store_true")

    return parser.parse_args()


def check_argument(args):
    player_dim = {
        "car": 5,
        "ped": 4
    }
    # Some logistic checking on the available experiments
    if args.no_players != 2 and args.t_react is not None:
        raise NotImplementedError(
            "Experiment is not available, please choose another run.")

    # check information of env_type
    if args.env_type == "goal_with_obs":
        # check to make sure there is only one goal
        if (len(args.goal) % 3) != 0:
            raise TypeError(
                "Something is wrong with your goal information, goal should be in the format of 'x y r'")
        elif int(len(args.goal) / 3) > 1:
            raise TypeError(
                "Current implementation only supports single goal for this type of env")

        # check information of obstacles
        if (len(args.obstacles) % 3) != 0:
            raise TypeError(
                "Something is wrong with your obs information, obs should be in the format of 'x y r'")

    elif args.env_type == "t_intersection":
        # check to see if the init_states, the no_players and the list of players match each other
        if args.no_players < 1:
            raise NotImplementedError(
                "t_intersection env_type only takes no_players >= 1")
        else:
            # check if the list of player_types and number of players are consistent
            if args.no_players != len(args.player_types):
                raise TypeError("The no_players value and length of player_types are not consistent: {} and {}".format(
                    args.no_players, args.player_types))
            # check if the length of init_states and no_players, player_types are consistent
            n_dim = sum([player_dim[type] for type in args.player_types])
            if n_dim != len(args.init_states):
                raise TypeError("The length of init_states and the expected dimension based on the input number of players and type of players are not consistent: {} and {}".format(
                    args.init_states, args.player_types))
            # check current availability of run
            if args.no_players == 2 and args.player_types != ["car", "car"]:
                raise NotImplementedError(
                    "Currently there is only implementation for [car, car] for two players case.")
            elif args.no_players == 3 and args.player_types != ["car", "car", "ped"]:
                raise NotImplementedError(
                    "Currently there is only implementation for [car, car, ped] for two players case.")

    else:
        raise TypeError("You have not chosen any env_type to run")

    print("EXPERIMENT INFORMATION")
    print("\nGeneral information")
    for item in vars(args).items():
        print("{}:\t{}".format(item[0].rjust(20), item[1]))
