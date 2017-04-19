#!/usr/bin/env python3
from flask import Flask, redirect, render_template
from flask_restful import Api

from api.exec import ExecuteResource

# Initialize Flask and API
app = Flask(__name__, template_folder='templates')
api = Api(app, prefix='/api/v1')
import os

# Add views
# app.add_url_rule('/dash', view_func=DashboardHomeResource.as_view('dash_view'))

# Add API Routes
api.add_resource(ExecuteResource, '/exec.json')

@app.route('/<string:page_name>/')
def static_page(page_name):
    return render_template('%s.html' % page_name)

# @app.route('/dash/')
# def home_redirect():
#     return redirect('/dash')

def run(debug=False):
    app.run(host='0.0.0.0', debug=debug, port=5000)

if __name__ == '__main__':
    run(debug=True)
