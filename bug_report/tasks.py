import os
import requests
import json
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

app = Celery(__name__)
app.conf.broker_url='redis://127.0.0.1:6379/0'
app.conf.result_backend='redis://127.0.0.1:6379/0'


@app.task()
def add_issue(bug_data):
    token = os.environ.get('TOKEN')
    url = 'https://api.github.com/repos/sharma-rishabh/report-bug/issues'
    headers={'Authorization':'Bearer '+token}
    title='A bug is found'
    issue_body='A user reported a bug with html which looks like. \n ```{0}```'.format(bug_data['dom'])
    body={'title':title,'body':issue_body}
    requests.post(url, headers=headers, data=json.dumps(body))
