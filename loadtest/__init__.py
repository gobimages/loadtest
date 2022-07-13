
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
    
    con.search("OU=People,DC=xxmailloadtest,DC=com",f"(cis2uid={uniqid})", attributes=['userAccountControl', 'pwdLastSet', 'msDS-User-Account-Control-Computed'])
    entries = con.entries 
    if entries:
        output = True
        Accountstate = True
        Passwordexpired = False
        date = entries[0].pwdLastSet.values[0]
        output = True 
        if date.strftime('%m-%d-%Y') == "01-01-1601" or entries[0].userAccountControl.values[0] == 8389120 or entries[0]['msDS-User-Account-Control-Computed'] == 8388608:
            Passwordexpired = True
        if entries[0].userAccountControl.values[0] == 514 or entries[0].userAccountControl.values[0] == 528 or entries[0]['msDS-User-Account-Control-Computed'] == 16 or entries[0]['msDS-User-Account-Control-Computed'] == 8388624:
            Accountstate = False
        myvalues = {'output':output, 'Accountstate':Accountstate, 'Passwordexpired':Passwordexpired}
        jsonv = json.dumps(myvalues)
        return func.HttpResponse(jsonv)
    else:
        myvalues = {'output':False, 'Accountstate':True, 'Passwordexpired':False}
        jsonv = json.dumps(myvalues)
        return func.HttpResponse(jsonv)
