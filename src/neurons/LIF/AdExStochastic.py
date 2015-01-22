#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import odeint
import logging as log

from synergetics.config import config as cfg
from synergetics.neurons.neurons import Neuron

class AdExStochastic(Neuron):

  def __init__(self, position, excitatory=True,
              update_rule= None,
              discover_rule=None,
              membrane_capacitance=0,
              adaptation_variable=0,
              leak_conductance=0,
              leak_reversal_potential=0,
              threshold_voltage=0,
              slope_factor=0,
              adaptation_coupling_param=0,
              adaptation_time_constant=0,
              resting_potential=0):
    self.C = membrane_capacitance
    self.w = adaptation_variable
    self.g_l = leak_conductance
    self.E_l = leak_reversal_potential
    self.V_thresh = threshold_voltage
    self.delta_t = slope_factor
    self.a = adaptation_coupling_param
    self.tau_w = adaptation_time_constant
    self.init = [resting_potential, 0]

    self.init_timestamp = 0
    self.spiked = True

    self.equations = [
      lambda V, w, I: (1/C)*( -1.0*self.g_l*(self.V - self.E_l) +\
                self.g_l*self.delta_t*np.exp((V - self.V_thresh)/self.delta_t) -\
                self.w + I),
      lambda V, w: (1/self.tau_w)*(self.a*(V - self.E_l) - w)
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

