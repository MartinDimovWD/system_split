from project.hardware.hardware import Hardware
from math import floor


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory, hardware_type='Heavy'):
        super().__init__(name, hardware_type, capacity, memory)
        self.capacity = capacity * 2
        self.memory = floor(memory * 0.75)
        self.hardware_type = 'Heavy'
        self.software_components = []
        # test the rounding

