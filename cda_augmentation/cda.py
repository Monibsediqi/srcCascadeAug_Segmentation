#############################################################################
# Created by: Monib Sediqi                                                  #
# Email: monib.sediqi@gmail.com                                             #
# Copyright (c) 2020                                                        #                  #
#############################################################################
#write source where you adopt code from
# https://github.com/kakaobrain/fast-autoaugment
# https://github.com/rpmcruz/autoaugment
import random

import numpy as np
import PIL, PIL.ImageOps, PIL.ImageEnhance, PIL.ImageDraw


__all__ = ['random_augment_list', 'get_augment', 'apply_augment']
RESAMPLE_MODE = PIL.Image.BICUBIC       #PIL.Image.BILINEAR

RANDOM_MIRROR = True

def shear_x(img, msk,  v, resample=RESAMPLE_MODE):     #[0.3, 0.3]
    assert -0.3 <= v <= 0.3
    if RANDOM_MIRROR and random.random() > 0.5:
        v = -v
    image = img.transform(img.size, PIL.Image.AFFINE, (1, v, 0, 0, 1, 0), resample=resample)
    mask = msk.transform(img.size, PIL.Image.AFFINE, (1, v, 0, 0, 1, 0), resample=resample)
    return image, mask

def shear_y(img, msk, v, resample=RESAMPLE_MODE): # [-0.3, 0.3]
    assert -0.3 <= v <= 0.3
    if RANDOM_MIRROR and random.random() > 0.5:
        v = -v
    image = img.transform(img.size, PIL.Image.AFFINE, (1, 0, 0, v, 1, 0), resample=resample)
    mask = msk.transform(img.size, PIL.Image.AFFINE, (1, 0, 0, v, 1, 0), resample=resample)
    return image, mask

def translate_x(img, msk, v, resample = RESAMPLE_MODE):   # [-150,150] => percentage [-0.45, 0.45]
    assert -0.45 <= v <= 0.45
    if RANDOM_MIRROR and random.random() > 0.5:
        v = -v
    v = v * img.size[0]
    image =  img.transform(img.size, PIL.Image.AFFINE, (1, 0, v, 0, 1, 0),
                         resample=resample)
    mask = msk.transform(img.size, PIL.Image.AFFINE, (1, 0, v, 0, 1, 0),
                         resample=resample)
    return image, mask

def translate_y(img, msk, v, resample=RESAMPLE_MODE):  # [-150, 150] => percentage: [-0.45, 0.45]
    assert -0.45 <= v <= 0.45
    if RANDOM_MIRROR and random.random() > 0.5:
        v = -v
    v = v * img.size[1]
    image = img.transform(img.size, PIL.Image.AFFINE, (1, 0, 0, 0, 1, v),
                         resample=resample)
    mask = msk.transform(img.size, PIL.Image.AFFINE, (1, 0, 0, 0, 1, v),
                         resample=resample)
    return image, mask

def translate_x_abs(img, msk, v, resample = RESAMPLE_MODE): # [-150, 150] => percentage: [-0.45, 0.45]
    assert v >= 0
    if random.random() > 0.5:
        v = -v
    image = img.transform(img.size, PIL.Image.AFFINE, (1, 0, v, 0, 1, 0), resample = resample)
    mask = msk.transform(img.size, PIL.Image.AFFINE, (1, 0, v, 0, 1, 0), resample=resample)
    return image, mask

def translate_y_abs(img, msk, v, resample = RESAMPLE_MODE): # [-150, 150] => percentage: [-0.45, 0.45]
    assert v >= 0
    if random.random() > 0.5:
        v = -v
    image = img.transform(img.size, PIL.Image.AFFINE, (1,0,0,0,1,v), resample= resample)
    mask = msk.transform(img.size, PIL.Image.AFFINE, (1,0,0,0,1,v), resample= resample)
    return image, mask


def rotate(img, msk, v):     # [-30, 30]
    assert -30<= v <=30
    if RANDOM_MIRROR and random.random() >0.5:
        v = -v
    image = img.rotate(v)
    mask = msk.rotate(v)
    return image, mask

def auto_contrast(img, msk, _):
    return PIL.ImageOps.autocontrast(img), msk

def invert(img, msk, _):     #invert (negate) the image
    return PIL.ImageOps.invert(img), msk

def equalize(img, msk, _):
    return PIL.ImageOps.equalize(img), msk

def flip_y(img, msk, _): # Flip the image vertically (top to bottom)
    return PIL.ImageOps.flip(img), PIL.ImageOps.flip(msk)

def flip_x(img, msk, _):     # Flip image horizontally (left to right)
    return PIL.ImageOps.mirror(img), PIL.ImageOps.mirror(msk)

def posterize(img, msk, v):   # Reduce the number of bits for each color channel
    # assert 4 <= v <=8
    v = int(v)
    return PIL.ImageOps.posterize(img,v), msk


def solarize(img, msk, v):  #: Invert all pixel values above a threshold
    assert 0 <= v <=256
    return PIL.ImageOps.solarize(img, v), msk

def solarize_add(img, msk, addition=0, threshold = 128):
    img_np = np.array(img).astype(np.int)
    img_np = img_np + addition
    img_np = np.clip(img_np, 0, 256)        # np.clip(limit) the values in an array
    img_np = img_np.astype(np.uint8)
    img = PIL.Image.fromarray(img_np)
    return PIL.ImageOps.solarize(img, threshold), msk

def contrast(img, msk, v):   #[0.1, 1.9] a value of 1.0 returns the original image
    assert 0.1 <= v <= 1.9
    return PIL.ImageEnhance.Contrast(img).enhance(v), msk

def color (img, msk, v):     #[0.1, 1.9] , adjust image color balance
    assert 0.1<= v <=1.9
    return PIL.ImageEnhance.Color(img).enhance(v), msk

def brightness(img, msk, v): #[0.1, 1.9]
    assert 0.1 <= v <=1.9
    return PIL.ImageEnhance.Brightness(img).enhance(v), msk

def sharpness(img, msk, v):  #[0.1, 1.9]
    assert 0.1 <= v <= 1.9
    image = PIL.ImageEnhance.Sharpness(img).enhance(v)
    return image, msk

def cutout_abs(img, v):     # [0, 60] => percentage[0, 0.2]
    #assert 0 <= v <= 20
    if v < 0:
        return img
    w, h = img.size
    x0 = np.random.uniform(w)
    y0 = np.random.uniform(h)


    x0 = int(max(0, x0 - v / 2.))
    y0 = int(max(0, y0 - v / 2.))
    x1 = min(w, x0 + v)
    y1 = min(h, y0 + v)

    xy = (x0, y0, x1, y1)
    color = (125, 123, 114)
    #color = (0,0,0)
    img = img.copy
    PIL.ImageDraw.Draw(img).rectangle(xy, color)
    return img,

def cutout(img, v):     # [0,60] => percentage [0,0.2]
    assert 0.0 <= v <=0.2
    if v <=0.:
        return img
    v = v * img.size[0]
    return cutout_abs(img, v)


def random_augment_list():  #16 operation and their range
    l = [
        (auto_contrast, 0, 1),
        (equalize, 0, 1),
        (invert, 0, 1),
        (rotate, 0, 30),
        (posterize, 0, 4),
        (solarize, 0, 256),
        (solarize_add, 0, 110),
        (color, 0.1, 1.9),
        (contrast, 0.1, 1.9),
        (brightness, 0.1, 1.9),
        (sharpness, 0.1, 1.9),
        (shear_x, 0, 0.3),
        (shear_y, 0, 0.3),
        (translate_x_abs, 0, 100),
        (translate_y_abs, 0., 100),
        (translate_x, -0.45, 0.45),
        (translate_y, -.45, 0.45),
        (flip_x, 0,1),
        (flip_y, 0,1)
    ]
    return l

augment_dict = {fn.__name__:(fn, v1, v2) for fn, v1, v2 in random_augment_list()}

def get_augment(name):
    return augment_dict[name]

def apply_augment(img, msk, name, level):
    augment_fn, low, high = get_augment(name)
    return augment_fn(img.copy(), msk.copy(), level * (high - low) + low)


# class RandomAugment(object):
#     def __init__(self, n, m):
#         self.n = n
#         self.m = m
#         self.augment_list = random_augment_list()
#
#     def __call__(self, img, msk):
#
#         ops = random.choices(self.augment_list, k = self.n)     # Randomly select multiple (k) choices from the list
#         for rand_aug, minval, maxval in ops:
#             if random.random() > random.uniform(0.2, 0.8):
#                 continue
#             val = (float(self.m)/30) * float(maxval - minval) + minval
#             img, msk = rand_aug(img, msk, val)
#         return img, msk




