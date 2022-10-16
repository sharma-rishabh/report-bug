from flask import (Blueprint,request)
import json
import requests

api_blueprint = Blueprint('api',__name__,url_prefix='/api')

@api_blueprint.post('/report-bug')
def report_bug():
    print(request.get_json())
    return json.dumps({'bug_reported': True})
