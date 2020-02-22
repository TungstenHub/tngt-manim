#!/usr/bin/env python

from manimlib.imports import *

import sys
sys.path.append('tngt-manim')

from utils.wscene import WScene
from utils.yarn import Yarn

class DegreeThreeEquation(WScene):

  def construct(self):

    eqq = Yarn(self, TexMobject("x^3 + px + q = 0"), 0, 1.2)

    eqq.start()

    self.wait(2)

    self.applyComment("Our goal: to find $x$ in terms of $p$ and $q$", 3.5)

    self.wait(2.5)

    self.applyComment("Trick: let's change $x$ for the sum of two variables: $u+v$", 2.5)

    eqq.transition(
      ["x",     "^3 + p", "x",     " + q = 0"],
      ["(u+v)", "^3 + p", "(u+v)", " + q = 0"],
    )

    self.wait(2)

    eqq.transition(
      ["(u+v)^3",             "+ p(u+v)", " + q = 0"],
      ["u^3+3u^2v+3uv^2+v^3", "+ p(u+v)", " + q = 0"],
    )

    self.wait(0.75)

    eqq.transition(
      ["u^3", "+3u^2v+3uv^2", "+v^3", "+ p(u+v) + q = 0"],
      ["u^3", "+v^3", "+3u^2v+3uv^2", "+ p(u+v) + q = 0"],
      [0,2,1,3]
    )

    self.wait(0.75)

    eqq.transition(
      # 0          1    2     3     4    5    6    7     8    9     10    11
      ["u^3+v^3", "+", "3u", "^2", "v", "",  "+", "3u", "v", "^2", "",   "+p(u+v)+q=0"],
      ["u^3+v^3", "+", "3u", "v",  "(", "u", "+", "v",  ")", "+p(u+v)+q=0"],
      [
        [0,0],
        [1,1],
        [2,2],
        [3,5],
        [4,3],
        [5,4],
        [6,6],
        [7,2],
        [8,3],
        [9,7],
        [10,8],
        [11,9]
      ],
    )

    self.wait(0.75)

    eqq.transition(
      # 0           1    2      3        4     5        6        7
      ["u^3+v^3+", "",  "3uv", "(u+v)", "+p", "",      "(u+v)", "+q=0"],
      ["u^3+v^3+", "(", "3uv", "+p",    ")",  "(u+v)", "+q=0"],
      [
        [0,0],
        [1,1],
        [2,2],
        [3,5],
        [4,3],
        [5,4],
        [6,5],
        [7,6]
      ]
    )

    self.wait()

    self.applyComment("By introducing two variables in place of one, \\\\ we may impose that they satisfy an extra condition", 2.5)

    self.wait()

    eqq.position(UP)

    self.wait()

    self.applyComment("We'll impose that $3uv = -p$", 1.5)

    aux = Yarn(self, TexMobject("3uv = -p"), DOWN, 1.2)

    aux.start()

    self.wait(2.5)

    self.play(
      eqq.eq[2].set_color, '#E91E63',
      eqq.eq[3].set_color, '#E91E63'
    )

    self.wait()

    self.play(
      eqq.eq[2].set_color, WHITE,
      eqq.eq[3].set_color, WHITE,
      run_time = 0.5
    )

    eqq.transition(
      # 0          1    2               3    4
      ["u^3+v^3", "+", "(3uv+p)(u+v)", "+", "q=0"],
      ["u^3+v^3", "+", "",             "q=0"],
      [0,1,2,1,3]
    )

    self.wait()

    self.applyComment("Now let's play with these equations", 1)

    eqq.transition(
      # 0      1    2      3     4     5
      ["u^3", "+", "v^3", "+q", "=",  "0"],
      ["u^3", "+", "v^3", "=",  "-q", ""],
      [0,1,2,4,3,5]
    )

    self.wait(0.75)

    aux.transition(
      # 0        1        2    3    
      ["3",     "uv = ", "-", "p"],
      ["uv = ", "-",     "{p", "\over 3}"],
      [3,0,1,2]
    )

    self.wait(0.75)

    aux.transition(   
      # extra brackets needed for the minus to be next to the fraction
      ["",      "uv", "",           "=", "",       "{-{p\over 3}}", ""], 
      ["\left(","uv", "\\right)^3", "=", "\left(", "-{p\over 3}",   "\\right)^3"]
    )

    self.wait(0.75)

    aux.transition(   
      # 0         1     2     3           4    5      6         7    8     9        10    11          12   13     14
      ["\left(", "u",  "v",  "\\right)", "^3", "=",  "\left(", "-", "{p", "\over", "3}", "\\right)", "^3"], 
      ["",       "u",  "^3", "v",        "",   "^3", "=",      "",  "{-",  "{p",    "^3", "\over",    "3", "^3}}", ""],
      [
        [0,0],
        [1,1],
        [2,3], 
        [3,4],
        [4,2],
        [4,5],
        [5,6],
        [6,7],
        [7,8],
        [8,9],
        [9,11],
        [10,12],
        [11,14],
        [12,10],
        [12,13]
      ]
    )

    self.play(
      eqq.eq[0].set_color, '#2196F3',
      eqq.eq[2].set_color, '#009688',
      aux.eq[1].set_color, '#2196F3',
      aux.eq[2].set_color, '#2196F3',
      aux.eq[3].set_color, '#009688',
      aux.eq[5].set_color, '#009688',
    )

    self.applyComment("Look! Everything is in terms of $u^3$ and $v^3$ now", 2.5)

    self.applyComment("We'll call them $\\alpha$ and $\\beta$", 2.5)

    self.play(
      eqq.eq[0].set_color, WHITE,
      eqq.eq[2].set_color, WHITE,
      aux.eq[1].set_color, WHITE,
      aux.eq[2].set_color, WHITE,
      aux.eq[3].set_color, WHITE,
      aux.eq[5].set_color, WHITE,
      run_time = 0.5
    )

    self.play(
      *eqq.transitionPlay(
        ["u^3",     "+", "v^3",    "=-q"], 
        ["\\alpha", "+", "\\beta", "=-q"]
      ),
      *aux.transitionPlay(
        ["u^3",     "v^3",    "=-{p^3\over 3^3}"], 
        ["\\alpha", "\\beta", "=-{p^3\over 3^3}"]
      )
    )

    self.wait()

    self.applyComment("We know the sum and product of $\\alpha$ and $\\beta$,", 1.5)

    self.applyComment("so they are roots of a quadratic equation", 1.5)

    self.play(
      *eqq.positionPlay(2.5*UP),
      *aux.positionPlay(1.1*UP)
    )

    quad = Yarn(self, TexMobject("t^2-(\\alpha+\\beta)t+\\alpha\\beta=0"), 1.8*DOWN, 1.2)

    quad.start()

    self.applyComment("the one having the sum and product as coefficients", 1.5)

    quad.transition(   
      ["t^2", "-(\\alpha+\\beta)", "t", "+\\alpha\\beta",  "=0"], 
      ["t^2", "+q",                "t", "-{p^3\over 3^3}", "=0"]
    )

    self.wait()

    self.play(
      *eqq.endPlay(),
      *aux.endPlay(),
      *quad.positionPlay(1.8*UP)
    )

    self.wait()

    res = Yarn(self, TexMobject("t={-b \pm \sqrt{b^2-4ac} \over 2a}"), 1.8*DOWN, 1.2)

    res.start()

    self.wait()

    res.transition(   
      # Lots of funny things for everything to work porperly
      # \sqrt and \over seem to mess everything up
      ["t={-", "b", "\pm", "\sqrt{", "b^", "2", "-", "4", "a",      "c}\over",                        "2",            "a", "}", "."], 
      ["t={-", "q", "\pm", "\sqrt{", "q^", "2", "-", "4", "\left(", "-{p^3\over 3^3}\\right)}\over ", "\phantom{.}2", ".", "}", ""]
    )

    self.wait(0.75)

    res.transition( 
      # 0     1     2    3      4 5       6                                      7      8? 9   10    11
      ["t=", "{-", "q", "\pm", "\sqrt{", "q", "^2-4\left(-{p^3\over 3^3}\\right)}\over ", "2", "}", "."],
      ["t=", "-", "{q", "\over", "2}", "\pm", "{\sqrt{", "q", "^2-4\left(-{p^3\over 3^3}\\right)}\over ", "2", "}", "."],
      # 0     1    2     3        4     5      6 7        8                                       9    10? 11   12   13                         14              15   16
      [
        [0,0],
        [1,1],
        [2,2],
        [3,5],
        [4,6],
        [5,7],
        [6,8],
        [7,3],
        [7,9],
        [8,10],
        [9,4],
        [9,11]
      ]
    )

    self.wait(0.75)

    res.transition( 
      ["t=-{q\over2}\pm{\sqrt{q^2-4\left(-{p^3\over 3^3}\\right)}\over ", "2",        "}"],
      ["t=-{q\over2}\pm{\sqrt{q^2-4\left(-{p^3\over 3^3}\\right)}\over ", "\sqrt{4}", "}"]
    )

    self.wait(0.75)

    res.transition( 
      # 0                  1 2        3    4      5    6         7    8     9           10  11   12              13        14 15     16   17     18
      ["t=-{q\over2}\pm", "{\sqrt{", "q", "^2-", "4", "\left(", "-", "{p", "^3\over ", "", "3", "^3}\\right)}", "\over ", "\sqrt{", "4", "}}.", "."],
      ["t=-{q\over2}\pm", "\sqrt{", "{q", "^2\over ", "4}", "+", "", "{4", "p", "^3\over", "4", "\\times", "2", "7}}.", "", ""],
      # 0                  1 2        3    4           5     6    7   8     9     10        11   12         13   14      15
      [
        [0,0],
        [1,1],
        [2,2],
        [3,3],
        [4,7],
        [5,8],
        [6,6],
        [7,7],
        [8,9],
        [9,12],
        [10,10],
        [11,13],
        [12,15],
        [13,4],
        [13,10],
        [14,1],
        [15,2],
        [16,5],
        [16,11]
      ],
      shift=0.06*RIGHT,
      keepShift=False
    )

    self.wait(0.75)

    res.transition(
      ["t=-{q\over2}\pm\sqrt{{q^2\over 4}+{", "4", "p^3\over", "4\\times", "27}}"],
      ["t=-{q\over2}\pm\sqrt{{q^2\over 4}+{", "",  "p^3\over", "",         "27}}"]
    )

    self.wait(0.75)

    self.play(
      *quad.endPlay(),
      *res.positionPlay(0*UP)
    )

    self.applyComment("Now we have one value for $\\alpha$ and one for $\\beta$")

    res_b = res.duplicate()

    self.play(
      *res.transitionPlay(
        ["t",       "=-{q\over2}", "\pm", "\sqrt{{q^2\over 4}+{p^3\over27}}"],
        ["\\alpha", "=-{q\over2}", "+",   "\sqrt{{q^2\over 4}+{p^3\over27}}"],
        shift = 1.2*UP
      ),
      *res_b.transitionPlay(
        ["t",      "=-{q\over2}", "\pm", "\sqrt{{q^2\over 4}+{p^3\over27}}"],
        ["\\beta", "=-{q\over2}", "-",   "\sqrt{{q^2\over 4}+{p^3\over27}}"],
        shift = 1.2*DOWN
      ),
    )

    self.wait()

    self.applyComment("But remember: they are $u^3$ and $v^3$")

    self.play(
      *res.transitionPlay(
        ["\\alpha", "=-{q\over2}+\sqrt{{q^2\over 4}+{p^3\over27}}"],
        ["u^3",     "=-{q\over2}+\sqrt{{q^2\over 4}+{p^3\over27}}"]
      ),
      *res_b.transitionPlay(
        ["\\beta", "=-{q\over2}-\sqrt{{q^2\over 4}+{p^3\over27}}"],
        ["v^3",    "=-{q\over2}-\sqrt{{q^2\over 4}+{p^3\over27}}"]
      ),
    )

    self.wait()

    self.play(
      *res.transitionPlay(
        # 0    1     2    3   4                                              5
        ["u", "^3", "=", "", "{-{q\over2}}+\sqrt{{q^2\over 4}+{p^3\over27}}", ""],
        ["u", "=",  "\sqrt[3]{", "{-", "{q\over2}}+\sqrt{{q^2\over 4}+{p^3\over27}}}.", ""],
        # 0    1     2 3          4    5
        [0,2,1,3,4,5]
      ),
      *res_b.transitionPlay(
        # 0    1     2    3   4                                              5
        ["v", "^3", "=", "", "{-{q\over2}}-\sqrt{{q^2\over 4}+{p^3\over27}}", ""],
        ["v", "=",  "\sqrt[3]{", "{-", "{q\over2}}-\sqrt{{q^2\over 4}+{p^3\over27}}}.", ""],
        # 0    1     2 3          4    5
        [0,2,1,3,4,5]
      ),
    )

    self.wait()

    fin = Yarn(self, TexMobject("x=u+v"), 2.3*DOWN, 1.2)

    self.play(
      *res.positionPlay(2.3*UP),
      *res_b.positionPlay(0*UP),
      *fin.startPlay()
    )

    self.wait()

    fin.transition(
      ["x=", "u", "+", "v"],
      ["x=", "\sqrt[3]{{-{q\over2}}+\sqrt{{q^2\over 4}+{p^3\over27}}}", "+", "\sqrt[3]{{-{q\over2}}-\sqrt{{q^2\over 4}+{p^3\over27}}}"],
      scale=1/1.2
    )

    self.wait()

    self.play(
      *res.endPlay(),
      *res_b.endPlay(),
      *fin.positionPlay(0*UP),
      run_time=2
    )

    self.wait(6)

    self.play(
      *fin.endPlay()
    )


