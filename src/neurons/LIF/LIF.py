#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import logging as log

from synergetics.config import config as cfg
from synergetics.neurons.neurons import Neuron

class LIF(Neuron):
  timestep = 0.001

  def __init__(self, position, excitatory=True,
              update_rule= Default_update(),
              discover_rule=Default_discovery()):
    self._spikes = []
    super(LIF, self).__init__(position, excitatory, update_rule, discover_rule)

  def excite(self, excitor, excitement, timestamp):
    pass

  def spike(self, timestamp, num=1):
    timestamp = timestamp + timestep
    self.spikes.append(timestamp)

    if self._probe:
      self._probe(timestamp)
    self.propagate(timestamp)
    self.reset()

  def reset(self):
    self._membrane_potential = self._reversal_potential
