from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        for hardware in System._hardware:
            if hardware_name == hardware.name:
                expr_soft = ExpressSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(expr_soft)
                System._software.append(expr_soft)
                # the installation doesn't add the software to the hardware's components
                return
        return 'Hardware does not exist'

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        for hardware in System._hardware:
            if hardware_name == hardware.name:
                light_soft = LightSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(light_soft)
                System._software.append(light_soft)
                # the installation doesn't add the software to the hardware's components
                return
        return 'Hardware does not exist'

    @staticmethod
    def release_software_component(hardware_name, software_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                for software in hardware.software_components:
                    if software.name == software_name:
                        hardware.uninstall(software)
                        System._software.remove(software)

    @staticmethod
    def analyze():
        num_hardware_components = len(System._hardware)
        num_software_components = len(System._software)
        # check if this is for each hardware instance or for the system.
        operational_memory_total = System.calc_total_memory()
        capacity_taken_total = System.calc_total_capacity_taken()
        return f'System Analysis\nHardware Components: {num_hardware_components}\nSoftware Components: {num_software_components}\nTotal Operational Memory: {operational_memory_total}\nTotal Capacity Taken: {capacity_taken_total}'

    @staticmethod
    def system_split():
        return 'ok'

    @staticmethod
    def calc_total_memory():
        software_consumption = 0
        hardware_memory = 0
        for software in System._software:
            software_consumption += software.memory_consumption
        for hardware in System._hardware:
            hardware_memory += hardware.memory
        return f'{int(software_consumption)} / {int(hardware_memory)}'

    @staticmethod
    def calc_total_capacity_taken():
        software_capacity = 0
        hardware_capacity = 0
        for software in System._software:
            software_capacity += software.memory_capacity
        for hardware in System._hardware:
            hardware_capacity += hardware.capacity
        return f'{int(software_capacity)} / {int(hardware_capacity)}'


System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())


#TODO:
# Check for the installation issue.
# Optimize the code where possible.
# Finish the system_split().