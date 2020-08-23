#!/usr/bin/env python

from manimlib.imports import *

import sys
sys.path.append('tngt-manim')

from utils.wscene import WScene
from utils.yarn import Yarn

class QuadraticFormula(WScene):

  def construct(self):

    eq = Yarn(self, TexMobject("ax^2+bx+c=0"), 0, 1.75)

    eq.start()

    self.wait()

    eq.transition(
      ["ax^2+bx", "+", "c", "=", "0"],
      ["ax^2+bx", "=", "-", "c", ""],
      [0,2,3,1,4]
    )

    self.wait()

    eq.transition(
      ["","ax^2+bx", "", "=", "", "{-c}", ""],
      ["4a\\times(","ax^2+bx", ")", "=", "4a\\times(", "{-c}", ")"]
    )

    self.wait()

    eq.transition(
      # 0     1          2    3      4    5     6    7    8     9           10    11    12
      ["4a", "\\times(","a", "x^2", "+", "bx", ")", "=", "4a", "\\times(", "{-", "c}", ")"],
      ["4a", "^2", "", "x^2", "+", "4a", "bx", "", "=", "{-", "4a", "", "c}", ""],
      # 0     1     2   3      4    5     6     7   8    9     10    11  12    13
      [
        [0,0],
        [0,5],
        [1,2],
        [2,1],
        [3,3],
        [4,4],
        [5,6],
        [6,7],
        [7,8],
        [8,10],
        [9,11],
        [10,9],
        [11,12],
        [12,13]
      ]
    )

    self.wait()

    eq.transition(
      ["4a^2x^2+4abx", "", "=", "{-4ac}"],
      ["4a^2x^2+4abx", "+b^2", "=", "b^2", "{-4ac}"],
      [
        [0,0],
        [1,1],
        [1,3],
        [2,2],
        [3,4]
      ]
    )

    self.wait()

    eq.transition(
      ["4a^2x^2+4abx+b^2", "=b^2{-4ac}"],
      ["(2ax+b)^2", "=b^2{-4ac}"]
    )

    self.wait()

    eq.transition(
      ["(", "2ax+b", ")", "^2", "", "=", "b^2{-4ac}"],
      ["", "2ax+b", "", "=", "\pm\sqrt{", "{b", "^2{-4ac}}}."],
      [0,1,2,4,5,3,6]
    )

    self.wait()

    eq.transition(
      ["2ax", "+", "b", "=", "\pm\sqrt{{b^2{-4ac}}}"],
      ["2ax", "=", "-", "b", "\pm\sqrt{{b^2{-4ac}}}"],
      [0,2,3,1,4]
    )

    self.wait()

    eq.transition(
      ["2a", "x", "=", "", "{-b\pm\sqrt{{b^2{-4ac}}}}"],
      ["x", "=", "{{-b\pm\sqrt{{b^2{-4ac}}}}", "\over", "2a}"],
      [4,0,1,3,2]
    )

    self.wait(4)

    self.play(
      *eq.endPlay()
    )