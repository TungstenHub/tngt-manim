#!/usr/bin/env python

from manimlib.imports import *

class WScene(Scene):

  def applyComment(self, message, time=2):
    comment = TextMobject(message)
    comment.to_edge(DOWN)
    self.play(FadeIn(comment))
    self.wait(time)
    self.play(FadeOut(comment))