from flask import Blueprint

class DemoBlueprint(Blueprint):
    def __init__():
        self.add_url_rule('/', view_func='index')

    def index():
        return 'Hello World'
