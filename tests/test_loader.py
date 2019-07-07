import os
import unittest

import loader


class TestLoader(unittest.TestCase):

    def test_load_csv_file(self):
        csv_file_path = os.path.join(os.getcwd(), 'data/user_agent.csv')
        print(csv_file_path)
        csv_content = loader.load_csv_file(csv_file_path)
        self.assertEqual(
            csv_content,
            [
                {'user_agent': 'iOS/10.1'},
                {'user_agent': 'iOS/10.2'},
                {'user_agent': 'iOS/10.3'}
            ]
        )
