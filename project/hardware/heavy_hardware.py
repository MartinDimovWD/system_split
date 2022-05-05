from project.hardware.hardware import Hardware
from math import floor


class HeavyHardware(Hardware):
    def __init__(self, name, hardware_type, capacity, memory):
        super().__init__(name, hardware_type, capacity, memory)
        self.hardware_type = 'Heavy'
        self.capacity = capacity * 2
        self.memory = floor(memory * 0.75)
        # test the rounding