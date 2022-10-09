# 다시풀기

import itertools
import copy

from numpy import square

N, M = map(int, input().split())
office = []

cctv = [[], [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]],
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        [[0, 1, 2, 3]]]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
square = 1000000000
