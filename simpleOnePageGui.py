'''
Created on 1 mei 2014

@author: hj
'''


from app.opra.echo import echo
import bottle
from bottle import route, run, request, static_file


bottle.debug(True)
# bottle.run(reloader=True)

app = bottle.default_app()

# Static files (css,js) setup

echo()

@route('/js/:path#.+#')
def server_static(path):
    return static_file(path, root='app/js/')


@route('/css/:path#.+#')
def server_static(path):
    return static_file(path, root='app/css/')


@route('/img/:path#.+#')
def server_static(path):
    return static_file(path, root='app/images/')


@route('/partials/:path#.+#')
def server_static(path):
    return static_file(path, root='app/partials/')


# Application setup
@route('/')
@route('/index.html')
def index():
    raise static_file('index.html', root='./app')


bottle.run(app=app, host='localhost', port=8180)
