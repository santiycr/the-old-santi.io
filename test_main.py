#!/usr/bin/env python

import unittest

import appengine_config
import main


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        main.app.config['TESTING'] = True
        self.app = main.app.test_client()

    def test_index(self):
        index = self.app.get("/")
        self.assertEqual(index.status_code, 200)
        self.assertIn("Ashley & Santi", index.data)

if __name__ == '__main__':
    unittest.main()
