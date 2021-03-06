#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import odeint
import logging as log

from synergetics.config import config as cfg
from synergetics.neurons.neurons import Neuron


class Izhikevich(Neuron):
  def __init__(self, position, excitatory=True,
              update_rule= None,
              discover_rule=None,
              u=0,
              v=0,
              a=0,
              b=0,
              c=0,
              d=0
              ):
    self.u = u
    self.v = v
    self.a = a
    self.b = b
    self.c = c
    self.d = d

    self.equations = [
      lambda u, v, I: 0.04*(v*v) + 5*v + 140 - u + I,
      lambda u, v: a*(b*v - u)
    ]

    super(LIFStochastic, self).__init__(position, excitatory, update_rule, discover_rule)

  def equations(self, vals, excitement=0):
    dV = self.equations[0](vals[0], vals[1], excitement)
    dw = self.equations[1](vals[0], vals[1])
    return array([dV, dw])

  def excite(self, excitor, excitement, timestamp):
    self.init = odeint(self.equations, self.init, time=linspace(0.0,0.001/10,timestamp-self.init_timestamp))
    self.init = odeint(self.equations, self.init, time=linspace(0.0, 0.001/10, 0.001))
    self.init = [self.init[0][-1], self.init[1][-1]]
    self.init_timestamp = timestamp

    # reset the spike, cause this is a continuous system
    if self.init[0][-1] > self.V_thresh:
      if not spiked:
        self.spike(timestamp)
        self.spiked = True
    else:
      self.spiked = False



