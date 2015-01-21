
import numpy as np
import logging as log

from synergetics.config import config as cfg
from synergetics.neurons.neurons import Neuron

class Izhikevich(Neuron):
  timestep = 0.001

  def __init__(self, position, excitatory=True,
              update_rule= Default_update(),
              discover_rule=Default_discovery(),
              resting_potential=0,
              reversal_potential=0,
              threshold=0):
    self._resting_potential = resting_potential
    self._reversal_potential = reversal_potential
    self._threshold = threshold
    self._membrane_potential = resting_potential
    self._spikes = []
    super(Izhikevich, self).__init__(position, excitatory, update_rule, discover_rule)

  def excite(self, excitor, excitement, timestamp):
    pass

  def spike(self, timestamp):
    timestamp = timestamp + timestep
    self.spikes.append(timestamp)

    if self._probe:
      self._probe(timestamp)
    self.propagate(timestamp)
    self.reset()

  def reset(self):
    self._membrane_potential = self._reversal_potential


class IzhikevichStochastic(Izhikevich):
  def __init__(self, position, excitatory=True,
              update_rule= Default_update(),
              discover_rule=Default_discovery(),
              resting_potential=0,
              reversal_potential=0,
              threshold=0):
    super(IzhikevichStochastic, self).__init__(position, excitatory, update_rule,
          discover_rule, resting_potential, reversal_potential, threshold)


  def excite(self, excitor, excitement, timestamp):
    pass


class IzhikevichContinuous(Izhikevich):
  def __init__(self, position, excitatory=True,
              update_rule= Default_update(),
              discover_rule=Default_discovery(),
              resting_potential=0,
              reversal_potential=0,
              threshold=0):
    super(IzhikevichStochastic, self).__init__(position, excitatory, update_rule,
          discover_rule, resting_potential, reversal_potential, threshold)

  def excite(self, excitor, excitement, timestamp):
    pass


class IzhikevichAdaptiveStochastic(Izhikevich):
  def __init__(self, position, excitatory=True,
              update_rule= Default_update(),
              discover_rule=Default_discovery(),
              resting_potential=0,
              reversal_potential=0,
              threshold=0):
    super(IzhikevichStochastic, self).__init__(position, excitatory, update_rule,
          discover_rule, resting_potential, reversal_potential, threshold)

  def excite(self, excitor, excitement, timestamp):
    pass


class IzhikevichAdaptiveContinuous(Izhikevich):
  def __init__(self, position, excitatory=True,
              update_rule= Default_update(),
              discover_rule=Default_discovery(),
              resting_potential=0,
              reversal_potential=0,
              threshold=0):
    super(IzhikevichStochastic, self).__init__(position, excitatory, update_rule,
          discover_rule, resting_potential, reversal_potential, threshold)

  def excite(self, excitor, excitement, timestamp):
    pass

