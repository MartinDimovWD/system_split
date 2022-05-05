from project.hardware.hardware import Hardware
from math import floor


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory, hardware_type='Power'):
        super().__init__(name, hardware_type, capacity, memory)
        self.capacity = capacity * 0.25
        self.memory = floor(memory * 1.75)
        self.hardware_type = 'Power'
        self.software_components = []
        # test the rounding


