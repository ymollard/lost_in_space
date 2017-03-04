#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

class Spawn():
    def __init__(self,img_size, position,parent=None):
        self.x = position[0]
        self.y = position[1]
        default_colors = [[1.0,0,0],[0,1.0,0],[0,0,1.0],[0,1.0,1.0],[1.0,0,1.0],[1.0,1.0,0]] # RGBCMY
        
        if parent is None:
            self.stage = 0
            self.color = default_colors[randint(0,len(default_colors)-1)]
        else:
            self.color = parent.color
            self.stage = min(parent.stage +1, 3) # evolution stage : 0 = pixel, 1, 2, 3
        self.points = []

        #self.color = default_colors[0] # for testing purposes !
        #self.stage = randint(0,1) # for testing purposes !

        patterns = [
                # red stages 0 to 3
                [
                    [[0,0]],
                    [[0,0],[0,1],[1,0],[0,-1],[-1,0]],
                    [[0,0],[0,1],[1,0],[0,-1],[-1,0],[0,2],[2,0],[0,-2],[-2,0]],
                    [[0,0],[0,1],[1,0],[0,-1],[-1,0],[0,2],[2,0],[0,-2],[-2,0],[0,3],[3,0],[0,-3],[-3,0],[1,1],[-1,1],[-1,-1],[1,-1]] 
        
                    ],
                # green stages 0 to 3
                [
                    [[0, 0]],
                    [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]],
                    [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 2], [2, 0], [0, -2], [-2, 0]],
                    [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 2], [2, 0], [0, -2], [-2, 0], [0, 3], [3, 0], [0, -3],
                     [-3, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]]
                ],
                # blue stages 0 to 3
            [
                [[0, 0]],
                [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]],
                [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 2], [2, 0], [0, -2], [-2, 0]],
                [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 2], [2, 0], [0, -2], [-2, 0], [0, 3], [3, 0], [0, -3],
                 [-3, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]]
            ],
                # cyan stages 0 to 3
            [
                [[0, 0]],
                [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]],
                [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 2], [2, 0], [0, -2], [-2, 0]],
                [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 2], [2, 0], [0, -2], [-2, 0], [0, 3], [3, 0], [0, -3],
                 [-3, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]]
            ],
                # magenta stages 0 to 3
            [
                [[0, 0]],
                [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]],
                [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 2], [2, 0], [0, -2], [-2, 0]],
                [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 2], [2, 0], [0, -2], [-2, 0], [0, 3], [3, 0], [0, -3],
                 [-3, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]]
            ],
                # yellow stages 0 to 3
            [
                [[0, 0]],
                [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]],
                [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 2], [2, 0], [0, -2], [-2, 0]],
                [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 2], [2, 0], [0, -2], [-2, 0], [0, 3], [3, 0], [0, -3],
                 [-3, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]]
            ],
                ]
        speed_mods = [
                # red stages 0 to 3
                [1, 2, 4],
                # green stages 0 to 3
                [1, 1.6, pow(1.6,2)],
                # blue stages 0 to 3
                [1, 1.3, pow(1.3,2)],
                # cyan stages 0 to 3
                [1, 1.3, pow(1.3, 2)],
                # magenta stages 0 to 3
                [1, 2, 4],
                # yellow stages 0 to 3
                [1, 1.6, pow(1.6, 2)],
                ]
        fading_mods = [
                # red stages 0 to 3
                [10, 20, 40],
                # green stages 0 to 3
                [13, 20.8, 33.28],
                # blue stages 0 to 3
                [17, 22.1,28.73],
                # cyan stages 0 to 3
                [17, 22.1, 28.73],
                # magenta stages 0 to 3
                [10, 20, 40],
                # yellow stages 0 to 3
                [13, 20.8, 33.28],
                ]
                
        color_index = default_colors.index(self.color)
        pattern = patterns[color_index][self.stage]
        self.speed = speed_mods[color_index][min(self.stage,2)]
        self.fading = fading_mods[color_index][min(self.stage,2)]

        for point in pattern:
            #print point
            self.points.append([(self.x + point[0] + img_size[0])%img_size[0],
                (self.y + point[1] + img_size[1])%img_size[1]])
        #if self.stage == 0:
            #self.points.append([(self.x + img_size[0])%img_size[0],self.y + img_size[1]%img_size[1]])
        #print self.points

         
