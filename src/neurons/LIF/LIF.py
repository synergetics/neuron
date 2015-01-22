#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import logging as log

from synergetics.config import config as cfg
from synergetics.neurons.neurons import Neuron

class LIF(Neuron):

  def __init__(self, position, excitatory=True,
              update_rule= Default_update(),
              discover_rule=Default_discovery()):
    super(LIF, self).__init__(position, excitatory, update_rule, discover_rule)

  def excite(self, excitor, excitement, timestamp):
    pass

