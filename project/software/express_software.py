from project.hardware.hardware import Software


class ExpressSoftware(Software):
    def __init__(self, name, software_type, capacity_consumption, memory_consumption):
        super().__init__(name, software_type, capacity_consumption, memory_consumption)
        self.software_type = 'Express'
        self.capacity_consumption = capacity_consumption * 2

