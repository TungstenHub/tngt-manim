#!/usr/bin/env python

from manimlib.imports import *

class Yarn:

  def __init__(self, scene, eq, pos=0*UP, scale=1):
    self.scene = scene
    self.eq = eq.move_to(pos).scale(scale)
    self.pos = pos
    self.scale = scale

  def duplicate(self):
    return Yarn(
      self.scene, 
      self.eq.copy().scale(1/self.scale), 
      np.array([self.pos[0],self.pos[1],self.pos[2]]), 
      self.scale)

  def position(self, pos):
    self.pos = pos
    self.scene.play(
      self.eq.move_to, self.pos
    )

  def positionPlay(self, pos):
    self.pos = pos
    return [self.eq.move_to, self.pos]

  def setScale(self, scale):
    self.scale = scale
    self.scene.play(
      self.eq.scale, self.scale
    )

  def start(self):
    self.scene.play(
      FadeIn(self.eq)
    )

  def end(self):
    self.scene.play(
      FadeOut(self.eq)
    )

  def startPlay(self):
    return [FadeIn(self.eq)]

  def endPlay(self):
    return [FadeOut(self.eq)]

  def transitionPlay(self, i, e, o=[], shift=0*UP, keepShift=True, scale=1, keepScale=True):
    
    obj1 = TexMobject(*[x if len(x)>0 else "\phantom{}" for x in i]).scale(self.scale).move_to(self.pos)
    obj2 = TexMobject(*[x if len(x)>0 else "\phantom{}" for x in e]).scale(self.scale*scale).move_to(self.pos).shift(shift)
    if keepShift: self.pos += shift
    if keepScale: self.scale *= scale

    extras = []

    for item in self.eq:
      self.scene.remove(item)

    if o == []: 
      order = list(zip(range(len(obj1)), range(len(obj1))))
    elif isinstance(o[0], int) : 
      order = list(zip(range(len(o)), o))
    else:
      order = o

      # handling of possible duplicates, that is, a piece in obj1 transforming into several of obj2
      
      idx = 0
      dup = 0 # number of duplicate indexes for obj1
      l = len(o)
      while idx < l - dup:
        if o[idx][0] < idx:
          extras.append([obj1[idx-1].copy(), obj2[o[idx][1]]])
          o.pop(idx)
          dup += 1
        else:
          idx += 1

    self.scene.add(obj1)

    self.eq = obj2

    return [ReplacementTransform(obj1[i],obj2[j]) for i,j in order] + [ReplacementTransform(a,b) for a,b in extras]

  def transition(self, i, e, o=[], shift=0*UP, keepShift=True, scale=1, keepScale=True):
    self.scene.play(*self.transitionPlay(i, e, o, shift, keepShift, scale, keepScale))