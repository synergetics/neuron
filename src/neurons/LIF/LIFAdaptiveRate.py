#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import logging as log

from synergetics.config import config as cfg
from synergetics.neurons.LIF.LIF import LIF


class LIFAdaptiveRate(LIF):
  def __init__(self, position, excitatory=True,
              update_rule= Default_update(),
              discover_rule=Default_discovery()
              tau_rc=0.02,
              tau_th=0.002):
    super(LIFStochastic, self).__init__(position, excitatory, update_rule, discover_rule)

  def excite(self, excitor, excitement, timestamp):
    pass
