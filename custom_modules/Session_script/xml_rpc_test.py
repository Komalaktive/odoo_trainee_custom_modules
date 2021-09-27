url = 'http://127.0.0.1:4040'  # url:url of where odoo service is running
db = 'rpc_demo_1' # db: db which is defined in odoo service
username = 'admin' #username : username through which we will login in db and make changes
password = 'admin' #password: password of user name

import xmlrpc.client #import to user xmlrpc API
import csv # Imported to read csv files
from datetime import datetime
import os

common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url) # for authentication
version = common.version() # to check if connection is correct before authentication
uid = common.authenticate(db, username, password, {}) # Used as parameter while calling methods
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url)) # Used as parameter while calling method

start_time = datetime.now()

with open('/home/odoo/komal_odoo/odoo-14/custom_modules/Session_script/res.partner.csv', newline='') as csv_file:
    csv_file = csv.DictReader(csv_file)
    '''We use this variable for us while executing csv or excel file in xmlrc
    to know how many records are updated or inserted or if
    scripts stops its execution due to any reasons at that time we can get the
    row number of xls or csv file at which row script stops its execution.'''
    excel_row = 2
    print('\n csv>>>>file>>>>>>>>', csv_file)

   
  
   

    for row in csv_file:
        rec = dict(row)
        print("Rec -------------------", rec)
        if excel_row >= 2:
            # We used strip() method to remove white spaces from the record.
            partner_id = models.execute_kw(db, uid, password, 'res.partner',
                'search', [[['email','=',rec['email'].strip()]]])
            vals = {
                'name':rec['name'].strip(),
                'email':rec['email'].strip(),
                'phone':rec['phone'].strip(),
                'city':rec['city'].strip(),
                
            }
            if not partner_id:
                partner_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [vals])
            else:
                partner_id = models.execute_kw(db, uid, password, 'res.partner', 'write',  [[partner_id[0]], vals])
            print("\n\n:::::::::excel_row:::::::::::::::", excel_row)

            # Example of read method to fetch specific field like emails and name of partner
            # Read method default returns Id field.
            # product_details = models.execute_kw(db, uid, password, 'res.partner', 'read',[product_id],{'fields':['name', 'list_price']})
            # print("product_details-------------", product_details)

        excel_row += 1

    search_partner_is = models.execute_kw(db, uid, password, 'res.partner', 'search',[[['city','=','Berlin']]])
    print("search_partner_is################",search_partner_is)

    remove_city_partner_id = models.execute_kw(db, uid, password, 'res.partner', 'search',
                                                   [[['city', '=', 'Berlin']]])
    print("remove city################",remove_city_partner_id)
    models.execute_kw(db, uid, password, 'res.partner', 'unlink',
                          [[partner for partner in remove_city_partner_id]])



 # To count existing product's count
    partner_count = models.execute_kw(db, uid, password, 'res.partner','search_count',[[]])
    print("partner_count#######@########", partner_count)

# models.execute_kw(db, uid, password, 'res.partner', 'write',[[14], {
#     'country_id': "united state" }])
