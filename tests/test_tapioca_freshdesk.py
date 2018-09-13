# coding: utf-8

import unittest

from tapioca_freshdesk import Freshdesk


class TestTapiocaFreshdesk(unittest.TestCase):
    def setUp(self):
        self.wrapper = Freshdesk()


if __name__ == "__main__":
    unittest.main()
