import re
import shlex
import subprocess

import render


class MongoTester:

    def __init__(self, host, port, db, username, password):
        self.host = host
        self.port = port
        self.db = db
        self.username = username
        self.password = password

    def run(self, query, expect):
        try:
            # Render query js file
            render.render_to_js(query)

            # Run script and get response
            cmd = 'mongo ' + self.host + ':' + self.port + '/' + self.db + ' -u "' + self.username + '" -p "'\
                  + self.password + '" --authenticationDatabase "' + self.db + '" --quiet script.js'
            cmd_args = shlex.split(cmd)
            cmd_process = subprocess.Popen(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            process_output = cmd_process.communicate()

            # Parse response
            match = re.match(b'^(\d+)\\r\\n*', process_output[0], re.M | re.I)
            response = None
            if match:
                response = match.group(1)
                print('Response:', response)
            else:
                print('ERROR:', process_output)

            # Verify response
            if type(expect) == int:
                print('Verify:', int(response) == expect)
            elif expect == '>0':
                print('Verify:', int(response) > 0)
            else:
                print('ERROR: Can not find expected results.')
        except Exception as e:
            print(str(e))
