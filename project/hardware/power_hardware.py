from project.hardware.hardware import Hardware
from math import floor


class PowerHardware(Hardware):
    def __init__(self, name, hardware_type, capacity, memory):
        super().__init__(name, hardware_type, capacity, memory)
        self.hardware_type = 'Power'
        self.capacity = capacity * 0.25
        self.memory = floor(memory * 1.75)
        # test the rounding