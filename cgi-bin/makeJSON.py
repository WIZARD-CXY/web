#!/usr/bin/env python

import json
print "Content-type: application/json"
print
response={'x':54,'y':99}
print json.JSONEncoder().encode(response)
