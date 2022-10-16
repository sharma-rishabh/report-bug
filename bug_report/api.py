import os

from flask import (Blueprint,request)
import json
from . import tasks

api_blueprint = Blueprint('api', __name__, url_prefix='/api')


@api_blueprint.post('/report-bug')
def report_bug():
    tasks.add_issue.apply_async(args=[request.get_json()])
    return json.dumps({'bug_reported': True})

#
# def add_issue(bug_data):
#     token = os.environ.get('TOKEN')
#     print(bug_data['dom'])
#     url = 'https://api.github.com/repos/sharma-rishabh/report-bug/issues'
#     headers={'Authorization':'Bearer '+token}
#     title='A bug is found'
#     issue_body='A user reported a bug with html which looks like. \n ```{0}```'.format(bug_data['dom'])
#     print(issue_body)
#     body={'title':title,'body':issue_body}
#     res=requests.post(url, headers=headers, data=json.dumps(body))
#     print(res.status_code)
