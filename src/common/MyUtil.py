import random
import PIL.Image
import PIL.ImageChops
import itertools
import math
import copy


RGB_COLOR_COUNT = 256
GRAYSCALE_COLOR_COUNT = 256

def getRandomNumber(start, end):
    number = random.randint(start, end)
    return number


def changeColorDepth(image, colorCount):
    if image.mode == 'L':
        raito = GRAYSCALE_COLOR_COUNT / colorCount
        change = lambda value: math.trunc(value / raito) * raito
        return image.point(change)

    if image.mode == 'RGB' or image.mode == 'RGBA':
        raito = RGB_COLOR_COUNT / colorCount
        change = lambda value: math.trunc(value / raito) * raito
        return PIL.Image.eval(image, change)

    raise ValueError('{mode}'.format(mode=image.mode))