from utils.abstract_writer import Abstract_writer
import utils.process

import json
import io


class JSON_writer(Abstract_writer):
    def __init__(self, path="./data/default.json"):
        super().__init__(path)

    def process_data(self):

        source = utils.process.entities_category(False)
        self.data['info'] = "The Solar System Application"
        self.data['data']['Planets'] = sorted(source["Planets"])
        self.data['data']['Non-planets'] = sorted(source["Non-planets"])
        return self

    def encode_data(self):
        self.data = json.dumps(self.data)
        return self

    def write_data(self):
        with open(self.path, "w") as json_file:
            json_file.write(self.data)
        return self

    def display(self):
        print(self.data)

    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data
