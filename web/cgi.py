# !usr/bin/python
from wsgiref.handlers import CGIHan
from buses import app


CGIHandler().run(app)
