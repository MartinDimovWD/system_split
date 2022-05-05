from project.hardware.hardware import Software
from math import floor


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption, software_type='Light'):
        super().__init__(name, software_type, capacity_consumption, memory_consumption)
        self.capacity_consumption = floor(capacity_consumption * 1.5)
        self.memory_consumption = floor(memory_consumption * 0.5)
        self.software_type = 'Light'
        # test the rounding

