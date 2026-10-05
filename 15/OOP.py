import time


class BaseClass:
    def process_data(self):
        ...

    def print_data(self):
        ...


class ProcessorData(BaseClass):
    def get_data(self):
        ...

    def print_data(self):
        ...


class MemoryData(BaseClass):
    def get_data(self):
        ...


class ProcessesData(BaseClass):
    def get_data(self):
        ...

    def process_data(self):
        ...

    def print_data(self):
        ...


class TemperatureData(BaseClass):
    def get_data(self):
        ...

    def process_data(self):
        ...

    def print_data(self):
        ...


class App:
    def __init__(self):
        self.items = [
            ProcessorData(),
            MemoryData(),
            ProcessesData(),
            TemperatureData()
        ]

    def run(self):
        while True:
            for item in self.items:
                item.get_data()
                item.process_data()
                item.print_data()

            time.sleep(3)


App().run()
