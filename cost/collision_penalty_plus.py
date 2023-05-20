import torch
import numpy as np
import math

from cost.cost import Cost
from utils.utils import MaxFuncMux


class CollisionPenalty(Cost):
    """
    Collision Penalty between two cars.
    """

    def __init__(self, g_params, name="collision_penalty"):
        self._position_indices = g_params["position_indices"]
        self._collision_r = g_params["collision_r"]
        self._car_params = g_params["car_params"]
        self._theta_indices = g_params["theta_indices"]
        self._player_id = g_params["player_id"]

        super(CollisionPenalty, self).__init__(
            "car{}_".format(g_params["player_id"]+1)+name)

    def get_car_state(self, x, index):
        car_x_index, car_y_index = self._position_indices[index % 2]
        if type(x) is torch.Tensor:
            car_rear = x[car_x_index:2+car_x_index, 0]
            car_front = [
                x[car_x_index, 0] + self._car_params["wheelbase"] *
                torch.cos(x[self._theta_indices[index], 0]),
                x[car_y_index, 0] + self._car_params["wheelbase"] *
                torch.sin(x[self._theta_indices[index], 0])
            ]
        else:
            car_rear = np.array([x[car_x_index, 0], x[car_y_index, 0]])
            car_front = [
                x[car_x_index, 0] + self._car_params["wheelbase"] *
                math.cos(x[self._theta_indices[index], 0]),
                x[car_y_index, 0] + self._car_params["wheelbase"] *
                math.sin(x[self._theta_indices[index], 0])
            ]
        return car_rear, car_front

    def g_coll_ff(self, x, k=0, **kwargs):
        _car1_rear, _car1_front = self.get_car_state(
            x, self._player_id)  # cur_car_id 0,1,2,3
        if(self._player_id == 0):
            _car2_rear, _car2_front = self.get_car_state(x, 1-self._player_id)
            _car3_rear, _car3_front = self.get_car_state(x, 2-self._player_id)
            _car4_rear, _car4_front = self.get_car_state(x, 3-self._player_id)
        elif(self._player_id == 1):
            _car2_rear, _car2_front = self.get_car_state(x, 1-self._player_id)
            _car3_rear, _car3_front = self.get_car_state(x, 2)
            _car4_rear, _car4_front = self.get_car_state(x, 3)
        elif(self._player_id == 2):
            _car2_rear, _car2_front = self.get_car_state(x, 2-self._player_id)
            _car3_rear, _car3_front = self.get_car_state(x, 1)
            _car4_rear, _car4_front = self.get_car_state(x, 3)
        elif(self._player_id == 3):
            _car2_rear, _car2_front = self.get_car_state(x, 3-self._player_id)
            _car3_rear, _car3_front = self.get_car_state(x, 1)
            _car4_rear, _car4_front = self.get_car_state(x, 2)

        if type(x) is torch.Tensor:
            # calculate distance between car1_front and carN_front
            d12 = torch.sqrt(
                (_car1_front[0] - _car2_front[0]) ** 2 + (_car1_front[1] - _car2_front[1]) ** 2)
            d13 = torch.sqrt(
                (_car1_front[0] - _car3_front[0]) ** 2 + (_car1_front[1] - _car3_front[1]) ** 2)
            d14 = torch.sqrt(
                (_car1_front[0] - _car4_front[0]) ** 2 + (_car1_front[1] - _car4_front[1]) ** 2)

            d12 = torch.unsqueeze(d12, dim=0)
            d13 = torch.unsqueeze(d13, dim=0)
            d14 = torch.unsqueeze(d14, dim=0)
            d = torch.cat((d12, d13, d14), 0)

            # 取d12，d13，d14最小值
            return 2.0 * self._collision_r - torch.min(d)
        else:
            d12 = math.sqrt(
                (_car1_front[0] - _car2_front[0]) ** 2 + (_car1_front[1] - _car2_front[1]) ** 2)
            d13 = math.sqrt(
                (_car1_front[0] - _car3_front[0]) ** 2 + (_car1_front[1] - _car3_front[1]) ** 2)
            # distance between _car1_front and _car4_front
            d14 = math.sqrt(
                (_car1_front[0] - _car4_front[0]) ** 2 + (_car1_front[1] - _car4_front[1]) ** 2)
            return 2.0 * self._collision_r - min(d12, d13, d14)

    # def g_coll_fr(self, x, k=0, **kwargs):
    #     _car1_rear, _car1_front = self.get_car_state(x, self._player_id)
    #     _car2_rear, _car2_front = self.get_car_state(x, 1-self._player_id)
    #     if type(x) is torch.Tensor:
    #         return 2.0 * self._collision_r - torch.sqrt((_car1_front[0] - _car2_rear[0]) ** 2 + (_car1_front[1] - _car2_rear[1]) ** 2)
    #     else:
    #         return 2.0 * self._collision_r - math.sqrt((_car1_front[0] - _car2_rear[0]) ** 2 + (_car1_front[1] - _car2_rear[1]) ** 2)

    # follow g_coll_ff
    def g_coll_fr(self, x, k=0, **kwargs):
        _car_1_rear, _car_1_front = self.get_car_state(x, self._player_id)
        if(self._player_id == 0):
            _car_2_rear, _car_2_front = self.get_car_state(
                x, self._player_id+1)
            _car_3_rear, _car_3_front = self.get_car_state(
                x, self._player_id+2)
            _car_4_rear, _car_4_front = self.get_car_state(
                x, self._player_id+3)
        elif(self._player_id == 1):
            _car_2_rear, _car_2_front = self.get_car_state(
                x, 1-self._player_id)
            _car_3_rear, _car_3_front = self.get_car_state(
                x, self._player_id+1)
            _car_4_rear, _car_4_front = self.get_car_state(
                x, self._player_id+2)
        elif(self._player_id == 2):
            _car_2_rear, _car_2_front = self.get_car_state(
                x, 2-self._player_id)
            _car_3_rear, _car_3_front = self.get_car_state(x, 1)
            _car_4_rear, _car_4_front = self.get_car_state(
                x, self._player_id+1)
        elif(self._player_id == 3):
            _car_2_rear, _car_2_front = self.get_car_state(
                x, 3-self._player_id)
            _car_3_rear, _car_3_front = self.get_car_state(x, 1)
            _car_4_rear, _car_4_front = self.get_car_state(x, 2)
        if type(x) is torch.Tensor:
            # calculate distance between car1_front and carN_rear
            d12 = torch.sqrt(
                (_car_1_front[0] - _car_2_rear[0]) ** 2 + (_car_1_front[1] - _car_2_rear[1]) ** 2)
            d13 = torch.sqrt(
                (_car_1_front[0] - _car_3_rear[0]) ** 2 + (_car_1_front[1] - _car_3_rear[1]) ** 2)
            d14 = torch.sqrt(
                (_car_1_front[0] - _car_4_rear[0]) ** 2 + (_car_1_front[1] - _car_4_rear[1]) ** 2)

            d12 = torch.unsqueeze(d12, dim=0)
            d13 = torch.unsqueeze(d13, dim=0)
            d14 = torch.unsqueeze(d14, dim=0)

            d = torch.cat((d12, d13, d14), 0)

            # 取d12，d13，d14最小值
            return 2.0 * self._collision_r - torch.min(d)
        else:
            d12 = math.sqrt(
                (_car_1_front[0] - _car_2_rear[0]) ** 2 + (_car_1_front[1] - _car_2_rear[1]) ** 2)
            d13 = math.sqrt(
                (_car_1_front[0] - _car_3_rear[0]) ** 2 + (_car_1_front[1] - _car_3_rear[1]) ** 2)
            d14 = math.sqrt(
                (_car_1_front[0] - _car_4_rear[0]) ** 2 + (_car_1_front[1] - _car_4_rear[1]) ** 2)
            return 2.0 * self._collision_r - min(d12, d13, d14)

    # def g_coll_rf(self, x, k=0, **kwargs):
    #     _car1_rear, _car1_front = self.get_car_state(x, self._player_id)
    #     _car2_rear, _car2_front = self.get_car_state(x, 1-self._player_id)
    #     if type(x) is torch.Tensor:
    #         return 2.0 * self._collision_r - torch.sqrt((_car1_rear[0] - _car2_front[0]) ** 2 + (_car1_rear[1] - _car2_front[1]) ** 2)
    #     else:
    #         return 2.0 * self._collision_r - math.sqrt((_car1_rear[0] - _car2_front[0]) ** 2 + (_car1_rear[1] - _car2_front[1]) ** 2）

    # follow g_coll_ff
    def g_coll_rf(self, x, k=0, **kwargs):
        _car1_rear, _car1_front = self.get_car_state(
            x, self._player_id)  # cur_car_id 0,1,2,3
        if(self._player_id == 0):
            _car2_rear, _car2_front = self.get_car_state(x, 1-self._player_id)
            _car3_rear, _car3_front = self.get_car_state(x, 2-self._player_id)
            _car4_rear, _car4_front = self.get_car_state(x, 3-self._player_id)
        elif(self._player_id == 1):
            _car2_rear, _car2_front = self.get_car_state(x, 1-self._player_id)
            _car3_rear, _car3_front = self.get_car_state(x, 2)
            _car4_rear, _car4_front = self.get_car_state(x, 3)
        elif(self._player_id == 2):
            _car2_rear, _car2_front = self.get_car_state(x, 2-self._player_id)
            _car3_rear, _car3_front = self.get_car_state(x, 1)
            _car4_rear, _car4_front = self.get_car_state(x, 3)
        elif(self._player_id == 3):
            _car2_rear, _car2_front = self.get_car_state(x, 3-self._player_id)
            _car3_rear, _car3_front = self.get_car_state(x, 1)
            _car4_rear, _car4_front = self.get_car_state(x, 2)
        if type(x) is torch.Tensor:
            # calculate distance between car1_rear and carN_front
            d12 = torch.sqrt(
                _car1_rear[0] - _car2_front[0]) ** 2 + (_car1_rear[1] - _car2_front[1]) ** 2
            d13 = torch.sqrt(
                _car1_rear[0] - _car3_front[0]) ** 2 + (_car1_rear[1] - _car3_front[1]) ** 2
            d14 = torch.sqrt(
                _car1_rear[0] - _car4_front[0]) ** 2 + (_car1_rear[1] - _car4_front[1]) ** 2

            d12 = torch.unsqueeze(d12, dim=0)
            d13 = torch.unsqueeze(d13, dim=0)
            d14 = torch.unsqueeze(d14, dim=0)
            d = torch.cat((d12, d13, d14), 0)

            # 取d12，d13，d14最小值
            return 2.0 * self._collision_r - torch.min(d)
        else:
            d12 = math.sqrt(
                (_car1_rear[0] - _car2_front[0]) ** 2 + (_car1_rear[1] - _car2_front[1]) ** 2)
            d13 = math.sqrt(
                (_car1_rear[0] - _car3_front[0]) ** 2 + (_car1_rear[1] - _car3_front[1]) ** 2)
            d14 = math.sqrt(
                (_car1_rear[0] - _car4_front[0]) ** 2 + (_car1_rear[1] - _car4_front[1]) ** 2)
            return 2.0 * self._collision_r - min(d12, d13, d14)

    # def g_coll_rr(self, x, k=0, **kwargs):
    #     _car1_rear, _car1_front = self.get_car_state(x, self._player_id)
    #     _car2_rear, _car2_front = self.get_car_state(x, 1-self._player_id)
    #     if type(x) is torch.Tensor:
    #         return 2.0 * self._collision_r - torch.sqrt((_car1_rear[0] - _car2_rear[0]) ** 2 + (_car1_rear[1] - _car2_rear[1]) ** 2)
    #     else:
    #         return 2.0 * self._collision_r - math.sqrt((_car1_rear[0] - _car2_rear[0]) ** 2 + (_car1_rear[1] - _car2_rear[1]) ** 2)

    # follow g_coll_ff

    def g_coll_rr(self, x, k=0, **kwargs):
        _car1_rear, _car1_front = self.get_car_state(
            x, self._player_id)  # cur_car_id 0,1,2,3
        if(self._player_id == 0):
            _car2_rear, _car2_front = self.get_car_state(x, 1-self._player_id)
            _car3_rear, _car3_front = self.get_car_state(x, 2-self._player_id)
            _car4_rear, _car4_front = self.get_car_state(x, 3-self._player_id)
        elif(self._player_id == 1):
            _car2_rear, _car2_front = self.get_car_state(x, 1-self._player_id)
            _car3_rear, _car3_front = self.get_car_state(x, 2)
            _car4_rear, _car4_front = self.get_car_state(x, 3)
        elif(self._player_id == 2):
            _car2_rear, _car2_front = self.get_car_state(x, 2-self._player_id)
            _car3_rear, _car3_front = self.get_car_state(x, 1)
            _car4_rear, _car4_front = self.get_car_state(x, 3)
        elif(self._player_id == 3):
            _car2_rear, _car2_front = self.get_car_state(x, 3-self._player_id)
            _car3_rear, _car3_front = self.get_car_state(x, 1)
            _car4_rear, _car4_front = self.get_car_state(x, 2)
        if type(x) is torch.Tensor:
            # calculate distance between car1_rear and carN_rear
            d12 = torch.sqrt(
                _car1_rear[0] - _car2_rear[0]) ** 2 + (_car1_rear[1] - _car2_rear[1]) ** 2
            d13 = torch.sqrt(
                _car1_rear[0] - _car3_rear[0]) ** 2 + (_car1_rear[1] - _car3_rear[1]) ** 2
            d14 = torch.sqrt(
                _car1_rear[0] - _car4_rear[0]) ** 2 + (_car1_rear[1] - _car4_rear[1]) ** 2

            d12 = torch.unsqueeze(d12, dim=0)
            d13 = torch.unsqueeze(d13, dim=0)
            d14 = torch.unsqueeze(d14, dim=0)

            # 拼接 d12,d13,d14
            # d12 = torch.cat((d12, d13, d14), 0)
            d = torch.cat((d12, d13, d14), 0)

            # 取d12，d13，d14最大值
            return 2.0 * self._collision_r - torch.min(d)
        else:
            d12 = math.sqrt(
                (_car1_rear[0] - _car2_rear[0]) ** 2 + (_car1_rear[1] - _car2_rear[1]) ** 2)
            d13 = math.sqrt(
                (_car1_rear[0] - _car3_rear[0]) ** 2 + (_car1_rear[1] - _car3_rear[1]) ** 2)
            d14 = math.sqrt(
                (_car1_rear[0] - _car4_rear[0]) ** 2 + (_car1_rear[1] - _car4_rear[1]) ** 2)
            return 2.0 * self._collision_r - min(d12, d13, d14)

    def g_collision(self, x, **kwargs):
        _max_func = MaxFuncMux()
        _max_func.store(self.g_coll_ff, self.g_coll_ff(x))
        _max_func.store(self.g_coll_fr, self.g_coll_fr(x))
        _max_func.store(self.g_coll_rf, self.g_coll_rf(x))
        _max_func.store(self.g_coll_rr, self.g_coll_rr(x))
        func_of_max_val, max_val = _max_func.get_max()
        return max_val, func_of_max_val

    # def g_rearonly_collision(self, x, k=0, **kwargs):
    #   car1_x_index, car1_y_index = self._position_indices[0]
    #   car2_x_index, car2_y_index = self._position_indices[1]
    #   if type(x) is torch.Tensor:
    #     return 2.0 * self._collision_r - torch.sqrt((x[car1_x_index, 0] - x[car2_x_index, 0]) ** 2 + (x[car1_y_index, 0] - x[car2_y_index, 0]) ** 2)
    #   else:
    #     return 2.0 * self._collision_r - math.sqrt((x[car1_x_index, 0] - x[car2_x_index, 0]) ** 2 + (x[car1_y_index, 0] - x[car2_y_index, 0]) ** 2)

    # def g_collision(self, x, **kwargs):
    #   return self.g_rearonly_collision(x), self.g_rearonly_collision

    def __call__(self, x, k=0):
        max_val, func_of_max_val = self.g_collision(x)
        return max_val, func_of_max_val
