import config, brain

if __name__ == "__main__":
  b = brain.Brain(config)
  b.run(manual=True)
  b.stop()
