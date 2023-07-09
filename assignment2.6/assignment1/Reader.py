import json
import linecache
import time


class CsvConverter:
    def __init__(self, header, delimiter=','):
        keys = header.split(delimiter)
        self.delimiter = delimiter
        self.keys = keys

    def csv_to_json(self, csv_lines):
        res = []
        for line in csv_lines:
            values = line.split(self.delimiter)
            assert len(values) == len(
                self.keys), f"amount of keys and values are different: {len(self.keys)} and {len(values)} respectively"
            res.append(dict(zip(self.keys, values)))
        return json.dumps(res)

    def get_keys_len(self):
        return len(self.keys)


class Reader:
    observers = {}

    def __init__(self, location='dSST.csv', delimiter=',', scope_size=5):
        self.pointer = 2
        self.scope_size = scope_size
        self.location = location
        header = self.read_csv_header()
        self.converter = CsvConverter(header, delimiter)

    def start_reading(self):
        next_lines = self.get_lines()
        while len(next_lines) != 0:
            Reader.notify_observers(next_lines)
            time.sleep(5)
            next_lines = self.get_lines()

    def read_csv_header(self):
        header = linecache.getline(self.location, 1).rstrip()
        assert header != "", f"no data provided in csv file!"
        return header

    def get_lines(self):
        if self.pointer == -1:
            return []
        lines = [line for i in range(self.pointer, self.pointer + self.scope_size) if
                 (line := linecache.getline(self.location, i).rstrip()) != ""]
        if len(lines) != self.scope_size:
            self.pointer = -1
        else:
            self.pointer += self.scope_size
        return self.converter.csv_to_json(lines)

    @staticmethod
    def notify_observers(json_lines):
        for consumer in Reader.observers.values():
            consumer.update(json_lines)

    @staticmethod
    def add_observer(consumer):
        Reader.observers[consumer.id] = consumer

    @staticmethod
    def remove_observer(consumer):
        Reader.observers.pop(consumer.id, None)
