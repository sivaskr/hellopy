# A simple hello world app to test Flask and AWS Elastic Beanstalk integration.

import flask
application = flask.Flask(__name__)


@application.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    application.run(host='0.0.0.0',debug=True)
