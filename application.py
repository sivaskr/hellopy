# A simple hello world app to test Flask and AWS Elastic Beanstalk integration.

import flask
application = flask.Flask(__name__)


@application.route('/')
def hello():
    return 'Hello, World! This is sample Python Web Application'


if __name__ == '__main__':
    application.run(host='0.0.0.0',debug=True)
