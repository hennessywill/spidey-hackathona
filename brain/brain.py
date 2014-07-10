from body import Body
from time import sleep

class Brain(object):
  """docstring for Brain"""
  def __init__(self, config):
    super(Brain, self).__init__()
    self.body = Body(config)
    self.body.start()

  def run(self, manual=False):
    while True:
      next_states = self.body.possible_next_states()
      if manual:
        print next_states
        joint, move = raw_input("joint, move: ").split()
        joint = int(joint)
        move = int(move)
        if joint == -1:
          break
      else:
        break
      self.body.make_move(joint, move)
      sleep(0.1)

  def stop(self):
    self.body.stop()
