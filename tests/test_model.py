
"""
Payment API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""

import unittest
import os
from mock import MagicMock, patch

from models import CreditCard

DATABASE_URI = os.getenv('DATABASE_URI', 'mongodb://localhost:27017/')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'payment-test')


class TestPaymentModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ These run once per Test suite """
        server.app.debug = False
        # Set up the test database
        server.app.config['DB_URI'] = DATABASE_URI
        server.app.config['DB_NAME'] = DATABASE_NAME

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        """ Runs before each test """
        CreditCard.init_db(server.app)
        CreditCard.collection.drop()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()