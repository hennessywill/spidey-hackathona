import Adafruit_BBIO.PWM as PWM
from leg import Leg

class Body(object):
  """ Body executes leg movements """
  def __init__(self, config):
    super(Body, self).__init__()
    hip_state = config.hip["state_config"].create_state()
    knee_state = config.knee["state_config"].create_state()
    hip_pins = config.hip['pins']
    knee_pins = config.hip['pins']

    legs = []
    for i in range(0, min(len(hip_pins), len(knee_pins))):
      leg = Leg(PWM, hip_pins[i], hip_state, knee_pins[i], knee_state)
      leg.set_state(state_config.create_state())
      legs.append(leg)

    # TODO - how do we define 'opposite' legs in config?
    legpair1 = LegPair(legs[0], legs[1])
    legpair2 = LegPair(legs[2], legs[3])
    self.legpairs = [legpair1, legpair2]

  def possible_next_states(self):
    possible_states = []
    for legpair in self.legpairs:
      possible_states.append(legpair.get_possible_states())
    return possible_states

  def make_move(self, legpair_index, move):
    self.legpairs[legpair_index].reach(move)

  def start(self):
    for legpair in self.legpairs:
      legpair.start()

  def reset(self):
    for legpair in self.legpairs:
      legpair.reset()

  def stop(self):
    for legpair in self.legpairs:
      legpair.stop()
    PWM.cleanup()
