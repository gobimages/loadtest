
from datetime import datetime
import logging
import json
import azure.functions as func
from ldap3 import Connection
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    uniqid = req.params.get('uniqid')
    if not uniqid:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            uniqid = req_body.get('uniqid')
    con=Connection("servername","xxx\\gobinath","password123",auto_bind='TLS_AFTER_BIND', authentication='NTLM')
    
    con.search("OU=People,DC=xxmailloadtest,DC=com",f"(cis2uid={uniqid})")
    entries = con.entries 
    if entries:
        myvalues = {'output':True}
        jsonv = json.dumps(myvalues)
        return func.HttpResponse(jsonv)
    else:
        myvalues = {'output':False}
        jsonv = json.dumps(myvalues)
        return func.HttpResponse(jsonv)
