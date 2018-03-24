# Copyright 2016, 2017 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Payment API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""

import unittest
import os
import json
from flask_api import status    # HTTP Status Codes
from mock import MagicMock, patch

import server


######################################################################
#  T E S T   C A S E S
######################################################################
class TestPetServer(unittest.TestCase):

    """ Pet Server Tests """
    def setUp(self):
        """ Runs before each test """
        self.app = server.app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        """ Test the Home Page """
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = json.loads(resp.data)
        self.assertEqual(data['name'], 'Payment Demo REST API Service')


######################################################################
#   M A I N
######################################################################
if __name__ == '__main__':
    unittest.main()
