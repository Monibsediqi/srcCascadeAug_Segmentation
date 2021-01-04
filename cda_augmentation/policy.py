#############################################################
# Created by: Monib Sediqi                                  #
# Email: monib.korea@gmail.com                          `   #
# Copyright (c) 2020                                        #
#############################################################


from cda_augmentation.cda import *  #Only random_augment_list , get_augment and apply_augment is imported
from collections import defaultdict
import random

def arsaug_policy():
    exp0_0 = [
        [('solarize', 0.66, 0.34), ("equalize", 0.56, 0.61)],
        [('equalize', 0.43, 0.06) ,('auto_contrast', 0.66, 0.08)],
        [('color', 0.72, 0.47), ('contrast', 0.88, 0.86)],
        [('brightness', 0.84, 0.71), ('flip_x', 0.88, 0.88)]]
    exp0_1 = [
        [('flip_x', 0.88, 0.96), ('brightness', 0.53, 0.79)],
        [('auto_contrast', 0.44, 0.36), ('solarize', 0.22, 0.48)],
        [('auto_contrast', 0.93, 0.32), ('posterize', 0.85, 0.26)],
        [('solarize', 0.55, 0.38), ('equalize', 0.43, 0.48)],
        [('flip_x', 0.82, 0.93), ('auto_contrast', 0.83, 0.95)]
    ]
    exp0_2 = [
        [('solarize', 0.43, 0.58), ('auto_contrast', 0.82, 0.26)],
        [('flip_y', 0.71, 0.79), ('auto_contrast', 0.81, 0.94)],
        [('auto_contrast', 0.92, 0.18), ('flip_y', 0.77, 0.85)],
        [('equalize', 0.71, 0.69), ('color', 0.23, 0.33)],
        [('sharpness', 0.36, 0.98), ('brightness', 0.72, 0.78)]]
    exp0_3 = [
        [('equalize', 0.74, 0.49), ('flip_y', 0.86, 0.91)],
        [('flip_x', 0.82, 0.91), ('auto_contrast', 0.96, 0.79)],
        [('auto_contrast', 0.53, 0.37), ('solarize', 0.39, 0.47)],
        [('flip_x', 0.72, 0.78), ('color', 0.91, 0.65)],
        [('brightness', 0.82, 0.46), ('color', 0.23, 0.91)]]
    exp0_4 = [
        [('flip_x', 0.72, 0.78), ('equalize', 0.37, 0.21)],
        [('color', 0.43, 0.23), ('brightness', 0.65, 0.71)],
        [('flip_x', 0.72, 0.78), ('auto_contrast', 0.92, 0.28)],
        [('equalize', 0.62, 0.59), ('equalize', 0.38, 0.91)],
        [('solarize', 0.57, 0.31), ('equalize', 0.61, 0.51)]]

    exp0_5 = [
        [('flip_x', 0.72, 0.78), ('sharpness', 0.31, 0.64)],
        [('color', 0.73, 0.77), ('flip_x', 0.65, 0.76)],
        [('flip_x', 0.72, 0.78), ('posterize', 0.42, 0.58)],
        [('color', 0.92, 0.79), ('equalize', 0.68, 0.54)],
        [('sharpness', 0.87, 0.91), ('sharpness', 0.93, 0.41)]]
    exp0_6 = [
        [('solarize', 0.39, 0.35), ('color', 0.31, 0.44)],
        [('color', 0.33, 0.77), ('color', 0.25, 0.46)],
        [('flip_x', 0.72, 0.78), ('posterize', 0.42, 0.58)],
        [('auto_contrast', 0.32, 0.79), ('flip_x', 0.72, 0.78)],
        [('auto_contrast', 0.67, 0.91), ('auto_contrast', 0.73, 0.83)]]

    exp0_7 = [
        [('rotate', 0.7, 0.6), ('color', 0.31, 0.44)],
        [('rotate', 0.2, 0.7), ('brightness', 0.57, 0.31)],
        [('rotate', 0.9, 0.2), ('posterize', 0.42, 0.58)],
        [('rotate', 0.2, 0.1), ('equalize', 0.61, 0.51)],
        [('rotate', 0.1, 0.9), ('auto_contrast', 0.73, 0.83)]]

    return exp0_0 + exp0_1 + exp0_2 + exp0_3 + exp0_4 + exp0_5 + exp0_6 + exp0_7


#
# def autoaug2arsaug(f):
#     def autoaug():
#         mapper = defaultdict(lambda: lambda x: x)
#         mapper.update({
#             'shearX': lambda x: float_parameter(x, 0.3),
#             'shearY': lambda x: float_parameter(x, 0.3),
#             'translateX': lambda x: int_parameter(x, 10),
#             'translateY': lambda x: int_parameter(x, 10),
#             'rotate': lambda x: int_parameter(x, 30),
#             'solarize': lambda x : 256 - int_parameter(x, 256),
#             'postarize2': lambda x: 4 - int_parameter(x, 4),
#             'contrast': lambda x: float_parameter(x, 1.8) + .1,
#             'color': lambda x: float_parameter(x, 1.8) + .1,
#             'brightness': lambda x: float_parameter(x, 1.8) + .1,
#             'sharpness': lambda x: float_parameter(x, 1.8) + .1,
#             'cutoutAbs': lambda x: int_parameter(x, 20)
#         })
#
#         def low_high(name, prev_value):
#             _, low, high = get_augment(name)
#             return float(prev_value - low) / (high - low)
#
#         policies = f()
#         new_policies = []
#         for policy in policies:
#             new_policies.append([(name, pr, low_high(name, mapper[name](level))) for name, pr, level in policy])
#         return new_policies
#     return autoaug
#
# PARAMETER_MAX = 10
#
# def float_parameter(level, maxval):
#     return float(level) * maxval/PARAMETER_MAX
#
# def int_parameter(level, maxval):
#     return int(float_parameter(level,maxval))

# def no_duplicates(f):
#     def wrap_remove_duplicate():
#         policies = f()
#         return remove_duplicates(policies)
#     return wrap_remove_duplicate()

# def remove_duplicates(policies):
#     s = set()
#     new_policies = []
#     for ops in policies:
#         key = []
#         for op in ops:
#             key.append(op[0])
#         key = '_'.join(key)
#         if key in s:
#             continue
#         else:
#             s.add(key)
#             new_policies.append(ops)
#     return new_policies

# def policy_decoder(augment, num_policy, num_op):
#     op_list = random_augment_list()
#     policies = []
#     for i in range (num_policy):
#         ops = []
#         for j in range (num_op):
#             op_idx = augment ['policy_%d_%d' % (i, j)]
#             op_prob = augment['prob_%d_%d' % (i, j)]
#             op_level = augment ['level_%d_%d' % (i, j)]
#             ops.append((op_list[op_idx][0].__name__, op_prob, op_level))
#         policies.append(ops)
#     return policies

class Augmentation():
    def __init__(self, policies):
        self.policies = policies

    def __call__(self, img, msk):
        for _ in range(1):
            policy = random.choice(self.policies)
            for name, pr, level in policy:

                if random.random () > pr:
                    continue
                img, msk = apply_augment(img, msk, name, level)
        return img, msk



