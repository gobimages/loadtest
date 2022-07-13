
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
    
    uniqid = str(req.params.get('uniqid'))
    gobi = f'(&(objectCategory=Person)(department={uniqid}))'
    #ODScode = req.params.get('ods')
    
    con=Connection("xxxx","xxx\\gobinath","password",auto_bind='TLS_AFTER_BIND')
    con.search("OU=Users,OU=Front Line Services,DC=int1,DC=wks,DC=accenturenhs,DC=co,DC=uk",search_filter=gobi, attributes=['distinguishedName']) 
    ent = con.entries
    print(ent) 
    if ent:
        con.modify(f'{ent[0].distinguishedName}', {'userAccountControl': [(MODIFY_REPLACE, [512])]})
        return func.HttpResponse("account has been updated")
    else:
       
        return func.HttpResponse("Something happened")