import time


def get_data():

    def get_processor_data(data):
        ...
        return data

    def get_memory_data(data):
        ...
        return data

    def get_processes_data(data):
        ...
        return data

    data = {}
    data = get_processor_data(data)
    data = get_memory_data(data)
    data = get_processes_data(data)

    return data


def process_data(data):
    ...
    return data


def print_data(data):
    ...


def main():
    while True:
        data = get_data()
        new_data = process_data(data)
        print_data(new_data)
        time.sleep(3)


main()
