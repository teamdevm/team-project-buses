#!/usr/bin/env python3
from wsgiref.handlers import CGIHandler
from buses import app


CGIHandler().run(app)
