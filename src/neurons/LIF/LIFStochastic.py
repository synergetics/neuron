#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import logging as log

from synergetics.config import config as cfg
from synergetics.neurons.LIF.LIF import LIF


class LIFStochastic(LIF):
  """
  http://icwww.epfl.ch/~gerstner/SPNM/node26.html#SECTION02311200000000000000
  """
  def __init__(self, position, excitatory=True,
              update_rule=None,
              discover_rule=None,
              resting_potential=0,
              reversal_potential=0,
              tau_rc=0.02):
    self._tau_rc = tau_rc
    self._V_rest = resting_potential
    self._V_rev = reversal_potential
    self._t_prev = 0

    super(LIFStochastic, self).__init__(position, excitatory, update_rule, discover_rule)

  def excite(self, excitor, excitement, timestamp):
    t = timestamp - self._t_prev
    v = np.exp(-1.0 * (self._tau_rc * t))
    v = v + excitement

    if v > self._V_rev:
      v = self._V_rest
      self.spike(timestamp)
