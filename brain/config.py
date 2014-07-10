from state import State

hip = {
  pins:[],
  duty:10,
  freq:60.0,
  state_config: StateConfig([0, 180], 0),
}

knee = {
  pins:[],
  duty:10,
  freq:60.0,
  state_config: StateConfig([]),
}

override = {
  "P8_3": StateConfig([]),
}

class StateConfig(object):
  """config for state type"""
  def __init__(self, degrees, initial = 0, offer_stationary = False, offer_all = False):
    super(StateConfig, self).__init__()
    self.degrees = degrees
    self.initial = initial
    self.offer_stationary = offer_stationary
    self.offer_all = offer_all

  def create_state():
    return State(self.degrees, self.initial offer_stationary=self.offer_stationary, offer_all=self.offer_all)
