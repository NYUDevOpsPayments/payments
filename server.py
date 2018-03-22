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
Payment Service

Paths:
------
GET / - Returns the information of payment service
"""

import os
import sys
from flask import Flask, jsonify, request, url_for, make_response, abort
from flask_api import status    # HTTP Status Codes
from werkzeug.exceptions import NotFound

# For this example we'll use SQLAlchemy, a popular ORM that supports a
# variety of backends including SQLite, MySQL, and PostgreSQL

# Create Flask application
app = Flask(__name__)

# Pull options from environment
DEBUG = (os.getenv('DEBUG', 'False') == 'True')
PORT = os.getenv('PORT', '5000')

######################################################################
# GET INDEX
######################################################################
@app.route('/')

def index():
    """ Root URL response """
    return jsonify(name='Payment Demo REST API Service',version='1.0',), status.HTTP_200_OK

######################################################################
#   M A I N
######################################################################
if __name__ == "__main__":
    print "========================================="
    print " P A Y M E N T   S E R V I C E   S T A R T I N G"
    print "========================================="
    app.run(host='0.0.0.0', port=int(PORT), debug=DEBUG)
