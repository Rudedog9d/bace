from flask import render_template
from flask_restful import reqparse, Resource
import os
import subprocess


parser = reqparse.RequestParser()
parser.add_argument('password')

WIN_PASSWD_CMD_BASE = '''powershell -ExecutionPolicy bypass -Command "C:\Windows\passwd.ps1 -PlainTextPassword '{passwd}'"'''

class PasswdResource(Resource):
    '''
    changed the password on the local machine
    '''
    def post(self):
        return self.get()

    def start_thread(self, cmd):
        pass

    def get(self):
        result = None
        args = parser.parse_args()
        passwd = args['password']

        print('Recieved: {}'.format(args))

        try:
            # run command immediately
            result = subprocess.check_output(WIN_PASSWD_CMD_BASE.format(passwd=passwd), timeout=5)
        except Exception as e:
            return {'error': str(e)}

        return {'result': str(result.decode())}

    def delete(self):
        pass

    def put(self):
        pass
