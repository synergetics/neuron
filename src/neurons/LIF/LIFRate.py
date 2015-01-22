#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import logging as log

from synergetics.config import config as cfg
from synergetics.neurons.LIF.LIF import LIF


class LIFRate(LIF):
  """
  http://en.wikipedia.org/wiki/Biological_neuron_model#Leaky_integrate-and-fire
  """
  def __init__(self, position, excitatory=True,
              update_rule=None,
              discover_rule=None,
              tau_rc=0.02,
              tau_th=0.002,
              reversal_potential=0,
              membrane_resistance=0.01,
              refractory_period=1):
    self._tau_rc    = tau_rc
    self._tau_th    = tau_th
    self._i_thresh  = reversal_potential/membrane_resistance
    self._t_ref     = refractory_period

    super(LIFStochastic, self).__init__(position, excitatory, update_rule, discover_rule)

  def excite(self, excitor, excitement, timestamp):
    if excitement > self._i_thresh:
      rate = 1.0/(self._t_ref - self._tau_rc*np.log(1.0 - (excitement/self._tau_th)))
    else:
      rate = 0
    if rate: self.spike(timestamp, num=rate)

