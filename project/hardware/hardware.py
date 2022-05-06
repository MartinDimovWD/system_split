from project.software.software import Software


class Hardware():
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if software.capacity_consumption <= self.capacity and software.memory_consumption <= self.memory:
            self.software_components.append(software)
        else:
            raise Exception('Software cannot be installed')

    def uninstall(self, software: Software):
        self.software_components.remove(software)