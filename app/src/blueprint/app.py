from flask import Blueprint

app_route = Blueprint('app_route', __name__, template_folder='templates')


@app_route.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app_route.run()
