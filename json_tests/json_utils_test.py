import unittest

from json_core.json_utils import JsonUtils


class TestJsonUtils(unittest.TestCase):

    def test_is_json_file(self):
        json_string = "{\"jsonAttribute\": \"jsonValue\"}"
        self.assertEquals(JsonUtils.is_json_file(json_string), True)

    def test_remove_json_header(self):
        json_with_header = "header#{\"jsonAttribute\": \"jsonValue\"}"
        self.assertEquals(JsonUtils.remove_json_header( json_with_header ), "{\"jsonAttribute\": \"jsonValue\"}")

    if __name__ == '__main__':
        unittest.main()
