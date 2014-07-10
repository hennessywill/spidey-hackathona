import Adafruit_BBIO.PWM as PWM

class Joint(object):
  """Manages leg of muybridge"""
  def __init__(self, pin, duty, freq, state):
    super(Leg, self).__init__()
    self.pin = pin
    self.duty = duty
    self.freq = freq
    self.state = state

  def set_state(state):
    self.state = state

  def start():
    PWM.start(self.pin, self.duty, self.freq)

  def reach(state):
    self.state.set(state)
    PWM.set_duty_cycle(self.pin, self.state.get_value())

  def get_possible_states():
    return self.states.possible()

  def stop():
    PWM.stop(self.pin)

  def reset():
    self.state.reset()
    self.reach(self.state.get_value())

