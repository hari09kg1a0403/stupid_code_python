import logging
import json


class JsonUtils:

    @staticmethod
    def is_json_file(json_string: str):
        try:
            json.loads(json_string)
        except ValueError:
            return False
        return True

    def remove_json_header(self, json_with_header: str):
        if self.is_json_file(json_with_header):
            return json_with_header.split('{')[1]
        else:
            logging.info("The string you provided is already a json string")


def main():
    pass


if __name__ == '__main__':
    main()
