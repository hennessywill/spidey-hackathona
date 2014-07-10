from joint import joint.Joint

class Body(object):
  """docstring for Robot"""
  def __init__(self, config):
    super(Robot, self).__init__()
    joint_dict = {}

    state = config.hip.state_config.create_state()
    duty = config.hip.duty
    freq = config.hip.freq
    for pin in config.hip.pins:
      joint_dict[pin] = Joint(pin, duty, freq, state)

    state = config.knee.state_config.create_state()
    duty = config.knee.duty
    freq = config.knee.freq
    for pin in config.knee.pins:
      joint_dict[pin] = Joint(pin, duty, freq, state)
    
    for (pin, state_config) in config.override:
      joint_dict[pin].set_state(state_config.create_state())

    self.joints = joint_dict.values()
    
  def possible_next_states():
    next_move = {}
    for joint in self.joints:
      next_move[joint] = joint.get_possible_states()
    return next_move

  def make_move(joint_index, move):
    self.joints[joint_index].reach(move)

  def start():
    for joint in self.joints:
      joint.start()
    self.reset()

  def reset():
    for joint in self.joints:
      joint.reset()

