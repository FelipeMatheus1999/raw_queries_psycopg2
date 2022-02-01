from . import users_route

from flask import Flask


def init_app(app: Flask):
    users_route.membros_route(app)
