from project.hardware.hardware import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption, software_type='Express'):
        super().__init__(name, software_type, capacity_consumption, memory_consumption)
        self.memory_consumption = memory_consumption * 2
        self.software_type = 'Express'



