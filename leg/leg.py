class Leg(object):
  """ One leg of the spider, containing two joints """
  def __init__(self, PWM, hip_pin, hip_state, knee_pin, knee_state):
    super(Leg, self).__init__()
    self.hip_joint = Joint(PWM, hip_pin, hip_state)
    self.knee_joint = Joint(PWM, knee_pin, knee_state)

  def set_state(self, state):
    self.knee_joint.set_state(state)
    self.hip_joint.set_state(state)

  def start(self):
    self.knee_joint.set_state(state)
    self.hip_joint.set_state(state)

  def reach(self, state):
    self.knee_joint.reach(state)
    self.hip_joint.reach(state)

  def get_possible_states(self):
    knee_possibilities = self.knee_joint.get_possible_states()
    hip_possibilities = self.hip_joint.get_possible_states()
    return [(k, h) for k in knee_possibilities for h in hip_possibilites]

  def stop(self):
    self.knee_joint.stop()
    self.hip_joint.stop()

  def reset(self):
    self.knee_joint.reset()
    self.hip_joint.reset()

  def get_hip_joint():
    return self.hip_joint

  def get_knee_joint():
    return self.knee_joint