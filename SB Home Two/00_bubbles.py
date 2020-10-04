# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# centre = sd.get_point(600, 300)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position=centre, radius=radius, width=3)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг


# def bubble(point, step):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=3)


# centre = sd.get_point(600, 300)
# bubble(point=centre, step=10)

# Нарисовать 10 пузырьков в ряд


def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=3)


# for x in range(100, 1001, 100):
#     centre = sd.get_point(x, 100)
#     bubble(point=centre, step=5)

# Нарисовать три ряда по 10 пузырьков

# for y in range(100, 301, 100):
#     for x in range(100, 1001, 100):
#         centre = sd.get_point(x, y)
#         bubble(point=centre, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    centre = sd.random_point()
    step = random.randint(1, 10)
    bubble(point=centre, step=step)

sd.pause()


