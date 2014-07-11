from state import State
from state import StateConfig

hip = {
  "pins":["P8_13", "P8_34", "P9_21", "P9_22"],
  "state_config": StateConfig([0, 130, 180], 0),
}

knee = {
  "pins":["P8_45", "P8_46", "P9_14", "P9_29"],
  "state_config": StateConfig([0, 180]),
}

override = {
  # "P8_3": StateConfig([]),
}

