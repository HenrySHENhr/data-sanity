import os
import unittest

import loader


class TestLoader(unittest.TestCase):

    def test_load_csv_file(self):
        csv_file_path = os.path.join(os.getcwd(), 'data/global.csv')
        print(csv_file_path)
        csv_content = loader.load_csv_file(csv_file_path)
        self.assertEqual(
            csv_content,
            [
                {'environment': 'ci', 'host': 'localhost', 'port': '27017'},
                {'environment': 'e2e', 'host': 'localhost', 'port': '27018'}
            ]
        )
