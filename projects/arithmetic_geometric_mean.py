#!/usr/bin/env python

from manimlib.imports import *

import sys
sys.path.append('tngt-manim')

from utils.wscene import WScene
from utils.yarn import Yarn

class ArithmeticGeometricMeanInequality(WScene):

  def construct(self):

    eq = Yarn(self, TexMobject("x"), 0, 2)

    eq.start()

    self.wait()

    eq.transition(
      ["x", ""],
      ["x", "^2 \geqslant 0"],
    )

    self.wait()

    eq.transition(
      ["x", "^2 \geqslant 0"],
      ["\left(\sqrt{a}-\sqrt{b}\\right)", "^2 \geqslant 0"],
    )

    self.wait()

    eq.transition(
      # 0         1           2    3   4           5           6     7
      ["\left(", "\sqrt{a}", "-", "", "\sqrt{b}", "\\right)", "^2", "\geqslant 0"],
      ["", "\sqrt{a}", "^2", "-", "2", "\sqrt{a}", "\sqrt{b}", "+", "\sqrt{b}", "^2", "", "\geqslant 0"],
      # 0   1           2     3    4    5           6           7    8           9     10  11
      [
        [0,0],
        [1,1],
        [1,5],
        [2,3],
        [3,7],
        [4,6],
        [4,8],
        [5,10],
        [6,2],
        [6,4],
        [6,9],
        [7,11]
      ]
    )

    self.wait()

    eq.transition(
      # 0 1       2     3     4    5    6 7       8     9 10      11    12   13 14     15    16    17           18
      ["\sqrt{", "a}", "^2", "-", "2", "\sqrt{", "a}", "\sqrt{", "b}", "+", "\sqrt{", "b}", "^2", "\geqslant", "0", ".", ".", ".", "."],
      ["", "",   "a",  "",   "-", "2", "\sqrt{", "a", "b}", "+", "",   "",   "b", "", "\geqslant", "", "0","."], 
      # 0   1     2     3     4    5    6 7       8    9     10   11    12    13   14  15           16  17
      [
        [0,0],
        [1,1],
        [2,2],
        [3,3],
        [4,4],
        [5,5],
        [6,6],
        [7,7],
        [8,8],
        [9,6],
        [10,7],
        [11,9],
        [12,12],
        [13,13],
        [14,13],
        [15,14],
        [16,15],
        [17,16],
        [18,17]
      ]
    )

    self.wait()

    eq.transition(
      ["a", "-", "2\sqrt{ab}", "+b\geqslant", "0"], 
      ["a", "+b\geqslant", "", "2\sqrt{ab}", ""],
      [
        [0,0],
        [1,2],
        [2,3],
        [3,1],
        [4,4]
      ]
    )

    self.wait()

    eq.transition(
      ["a+b",   "", "\geqslant", "2", "\sqrt{ab}"],
      ["{a+b", "\over", "2}", "\geqslant", "\sqrt{ab}"], 
      [
        [0,0],
        [1,1],
        [2,3],
        [3,2],
        [4,4]
      ]
    )

    self.wait(4)

    self.play(
      *eq.endPlay()
    )