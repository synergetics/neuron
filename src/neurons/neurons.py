#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import logging as log
import uuid

from synergetics.config import config as cfg
from synergetics.learning.default import Default as Default_update
from synergetics.networks.default import Default as Default_discovery


class Neuron(object):

  def __init__(self, position, excitatory=True,
              update_rule= Default_update(),
              discover_rule=Default_discovery()):
    self.uuid = uuid.uuid4()
    self._connections = {}
    self._excitatory = excitatory
    self._update_rule = update_rule
    self._position = position
    self._discover_rule = discover_rule
    self._probe = None

  def connection(self, other, weight, excitatory=True, on_spike=None):
    # if we are already connected, update the weights
    if other.uuid in self._connections:
      self._connections[other.uuid] = self._connections[other.uuid] + weight
    else:
      self._connections[other.uuid] = {
        "neuron": other,
        "weight": weight,
        "on_spike": on_spike,
        "excitatory": excitatory
      }

  def connect(self, other, weight):
    other.connection(self, weight, self.on_spike)

  def probe(self, callback):
    self._probe = callback

  def discover(self):
    discoveries, weights = self._discover_rule(self._position)

    for d in xrange(len(discoveries)):
      self.connect(discoveries[d], weights[d])

  def propagate(self, excitement, timestamp):
    for connection in self._connections:
      self._connections[connection]["on_spike"](self, excitement, timestamp)

  def excite(self, excitor, excitement, timestamp):
    pass

