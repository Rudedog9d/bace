from flask import render_template
from flask_restful import reqparse, Resource
import os
import subprocess


parser = reqparse.RequestParser()
parser.add_argument('cmd')
parser.add_argument('thread')
parser.add_argument('timeout', type=int)

class ExecuteResource(Resource):
    def __init__(self):
        self.threads = []

    def post(self):
        return self.get()

    def start_thread(self, cmd):
        pass

    def get(self):
        result = None
        args = parser.parse_args()
        thread = True if args['thread'] == 'True' else False
        cmd = args['cmd'].split()
        timeout = args.get('timeout', None) or 5

        print('Recieved: {}'.format(args))

        if thread:
            # if thread, start a new thread
            id = self.start_thread(cmd)
            return {'thread_id': str(id)}

        try:
            # run command immediately
            result = subprocess.check_output(cmd, timeout=timeout)
        except Exception as e:
            return {'error': str(e)}

        return {'result': str(result.decode())}

    def delete(self):
        pass

    def put(self):
        pass
