
from datetime import datetime
import logging
import json
import azure.functions as func
from ldap3 import Connection, Server, MODIFY_REPLACE

import os


#uniqid = "1234567"
#con=Connection("10.11.7.4","int1\\gobinath","Months@2019",auto_bind='TLS_AFTER_BIND')
#con.search("OU=Users,OU=Front Line Services,DC=int1,DC=wks,DC=accenturenhs,DC=co,DC=uk",f"(department={uniqid})", attributes=['distinguishedName']) 
##con.search("OU=Users,OU=Front Line Services,DC=int1,DC=wks,DC=accenturenhs,DC=co,DC=uk",f"(department={uniqid})", attributes=['employeeID', 'msDS-User-Account-Control-Computed', 'userAccountControl'])
#ent = con.entries
#print(ent[0].distinguishedName)
#con.modify(f'{ent[0].distinguishedName}',
#         {'userAccountControl': [(MODIFY_REPLACE, [512])]})
#print(ent[0].userAccountControl) 
#print(ent[0]['msDS-User-Account-Control-Computed']) 

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
<<<<<<< HEAD
    uniqid = str(req.params.get('uniqid'))
    gobi = f'(&(objectCategory=Person)(department={uniqid}))'
    ODScode = req.params.get('ods')
    
    con=Connection("10.11.7.4","int1\\gobinath","Months@2019",auto_bind='TLS_AFTER_BIND')
    con.search("OU=Users,OU=Front Line Services,DC=int1,DC=wks,DC=accenturenhs,DC=co,DC=uk",search_filter=gobi, attributes=['employeeID', 'msDS-User-Account-Control-Computed', 'userAccountControl'], search_scope = 'SUBTREE' )
    ent = con.entries
    print(ent) 
    if ent:
        ods = True
        Accountstate = True
        if ent[0].userAccountControl == 514 or ent[0].userAccountControl == 528 or ent[0]['msDS-User-Account-Control-Computed'] == 16 or ent[0]['msDS-User-Account-Control-Computed'] == 8388624:
            Accountstate = False
        if ent[0].employeeID != ODScode:
            ods = False
        myvalues = {'output':True, 'ods':ods, 'Accountstate':Accountstate}
=======
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
>>>>>>> fb1fcbd4e22f5bb8658b83ff2b46b6a16e0a2002
        jsonv = json.dumps(myvalues)
        logging.info(jsonv)
        return func.HttpResponse(jsonv)
    else:
        myvalues = {'output':False, 'ods':False, 'Accountstate':False}
        jsonv = json.dumps(myvalues)
        return func.HttpResponse(jsonv)
