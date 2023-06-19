import json
import os


class Model:
    def get_new_id(self, data_file_path):
        if os.path.exists(data_file_path):
            with open(data_file_path, 'r') as file:
                data = json.load(file)
                if data:
                    last_id = data[-1].get('id', 0)
                    return last_id + 1
                else:
                    return 1
        else:
            return 1
