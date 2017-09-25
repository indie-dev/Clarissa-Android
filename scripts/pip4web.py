# -*-coding:utf-8-*-
#qpy:webapp:QPython pip web
#qpy://127.0.0.1:10001/hello

"""
QPython Pip Web
@Author river
"""

### DEBUG MODE ###
import sys
sys.path.append('../builtins/')

from bottle import Bottle, ServerAdapter, static_file, view, request, response
import os
import base64
import sys
import shutil
import socket
import time
import zipfile
import urllib2
import json


class MyWSGIRefServer(ServerAdapter):
    server = None

    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw):
                    pass
            self.options['handler_class'] = QuietHandler
        self.server = make_server(self.host, self.port, handler, **self.options)
        self.server.serve_forever()

    def stop(self):
        # sys.stderr.close()
        import threading
        threading.Thread(target=self.server.shutdown).start()
        # self.server.shutdown()
        self.server.server_close()
        print "# QWEBAPPEND"

#####################
def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip

######################
# ---- BUILT-IN ROUTERS ----

def __exit():
    response.headers['Access-Control-Allow-Origin'] = '*'
    global server
    server.stop()


def __ping():
    response.headers['Access-Control-Allow-Origin'] = '*'
    return "ok"


def server_static(file_path):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return static_file(file_path, root=ROOT+'/static')


# ---- APPLICATION ROUTERS ----
def index():
    return {}

def hello():
    return """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Cover Template for Bootstrap</title>
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="http://getbootstrap.com/assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="http://getbootstrap.com/examples/cover/cover.css" rel="stylesheet">
    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="http://getbootstrap.com/assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="http://getbootstrap.com/assets/js/ie-emulation-modes-warning.js"></script>
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="site-wrapper">

      <div class="site-wrapper-inner">

        <div class="cover-container">

          <div class="masthead clearfix">
            <div class="inner">
              <h3 class="masthead-brand">Pip Web Console</h3>
              <nav>
                <ul class="nav masthead-nav">
                  <li class="active"><a href="#">Home</a></li>
                  <li><a href="#">Categories</a></li>
                </ul>
              </nav>
            </div>
          </div>
          <div class="inner cover">
             <form class="navbar-form navbar-center">
                <div class="form-group">
                <span style='font-size:30px;'>pip</span>
                </div>
                <div class="form-group">
                  <select type="select" class="form-control">
                    <option value=''>Install</option>
                    <option value=''>Search</option>
                    <option value=''>Uninstall</option>
                    </select>
                </div>
                <div class="form-group">
                  <input type="password" placeholder="Package" class="form-control">
                </div>
                <button type="submit" class="btn btn-success">Execute</button>
              </form>

            <div style='padding:10px;border:1px solid grey;background:#666'>
            <p class="lead">You can use pip to install/uninstall/upgrade python libraries</p>
            </div>

          </div>
          <div class="mastfoot">
            <div class="inner">
              <p>QPython WebApp</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="http://getbootstrap.com/assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="http://getbootstrap.com/dist/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="http://getbootstrap.com/assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
"""


######################
app = Bottle()
app.route('/', method='GET')(index)
app.route('/hello', method='GET')(hello)
app.route('/__exit', method=['GET', 'HEAD'])(__exit)
app.route('/__ping', method=['GET', 'HEAD'])(__ping)
app.route('/static/<file_path:path>', method='GET')(server_static)


try:
    server = MyWSGIRefServer(host="127.0.0.1", port="10001")
    app.run(server=server, reloader=False)
except Exception, ex:
    print "Exception: %s" % repr(ex)
