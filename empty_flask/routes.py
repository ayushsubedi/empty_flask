from empty_flask import application

@application.route('/')
def index():
    return 'future home of some app'