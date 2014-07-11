class LegPair(object):
  """ A pair of legs that are diagonally opposite and move together """
  def __init__(self, leg1, leg2):
    super(LegPair, self).__init__()
    self.leg1 = leg1
    self.leg2 = leg2

  def set_state(self, state):
    self.leg1.set_hip_state(state)
    self.leg1.set_knee_state(state)
    self.leg2.set_hip_state(state)
    self.leg2.set_knee_state(state)

  def start(self):
    self.leg1.reset()
    self.leg2.reset()

  def reach(self, state):
    self.leg1.reach(state)
    self.leg2.reach(state)

  def get_possible_states(self):
    # a state is only possible if both legs can transition to that state
    leg1_possibs = self.leg1.get_possible_states()
    leg2_possibs = self.leg2.get_possible_states()
    return [poss for poss in leg1_possibs if poss in leg2_possibs]

  def stop(self):
    self.leg1.stop()
    self.leg2.stop()

  def reset(self):
    self.leg1.reset()
    self.leg2.reset()
