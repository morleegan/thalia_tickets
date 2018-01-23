from flask import Flask
from delivery.routes import show, seating, search, order, report, ticket

"""Start flask app by running main"""
app = Flask(__name__, template_folder='templates')
app.config['JSON_SORT_KEYS'] = False

app.register_blueprint(show, url_prefix='/thalia')
app.register_blueprint(seating, url_prefix='/thalia')
app.register_blueprint(search, url_prefix='/thalia')
app.register_blueprint(order, url_prefix='/thalia')
app.register_blueprint(report, url_prefix='/thalia')
app.register_blueprint(ticket, url_prefix='/thalia')

if __name__ == '__main__':
    app.run(port=8080)
