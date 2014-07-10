class Joint(object):
  """Manages leg of muybridge"""
  def __init__(self, pwm, pin, state):
    super(Joint, self).__init__()
    self.pin = pin
    self.state = state
    self.pwm = pwm

  def set_state(self, state):
    self.state = state

  def start(self):
    self.state.reset()
    self.servo = Servo(self.pwm, self.pin, self.state.get_value())

  def reach(self, state):
    self.state.set(state)
    self.servo.set(self.state.get_value())

  def get_possible_states(self):
    return self.state.possible()

  def stop(self):
    self.servo.stop()

  def reset(self):
    self.state.reset()
    self.reach(self.state.get_value())


class Servo:
  PTP = 25
  def __init__(self, pwm, pin, init=0.0):
    self.pwm = pwm
    self.pin = pin
    self.pwm.start(self.pin, self._get_duty_percent(init), self._get_freq())

  def _get_freq(self):
    return 1000.0/Servo.PTP

  def _get_duty_percent(self, angle):
    t = 2.0 * (angle/180.0) + 0.5
    d = (t / Servo.PTP) * 100.0
    return d

  def set(self, angle):
    self.pwm.set_duty_cycle(self.pin, self._get_duty_percent(angle))

  def stop(self):
    self.pwm.stop(self.pin)

