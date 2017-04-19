from flask import render_template
from flask_restful import reqparse, Resource
import os
import subprocess

THREADS = {}
INDEX = 0

exec_parser = reqparse.RequestParser()
exec_parser.add_argument('cmd')
exec_parser.add_argument('thread')
exec_parser.add_argument('timeout', type=int)

# /api/v1/exec/manage
class ExecuteManagerResource(Resource):
    def get(self):
        args = exec_parser.parse_args()
        thread = args.get('thread', None)
        if not thread:
            return {'error': '{}: thread not found'.format(thread)}
        return THREADS[thread]

# /api/v1/exec.json
class ExecuteResource(Resource):
    def __init__(self):
        self.threads = []

    def post(self):
        return self.get()

    def start_thread(self, cmd):
        pass

    def get(self):
        result = None
        args = exec_parser.parse_args()
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
