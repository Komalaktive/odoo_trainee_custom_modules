url = "http://127.0.0.1:4040"
db = "rpc_demo_1"
username = "admin"
password = "admin"

import xmlrpc.client  # import to user xmlrpc API
import csv  # Imported to read csv files
from datetime import datetime
import os

common = xmlrpc.client.ServerProxy("%s/xmlrpc/2/common" % url)
version = common.version()
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(url))

start_time = datetime.now()

with open(
    "/home/odoo/komal_odoo/odoo-14/custom_modules/Session_script/res.partner.csv",
    newline="",
) as csv_file:
    csv_file = csv.DictReader(csv_file)

    excel_row = 2
    print("\n csv>>>>file>>>>>>>>", csv_file)

    for row in csv_file:
        rec = dict(row)
        print("Rec -------------------", rec)
        if excel_row >= 2:
            # We used strip() method to remove white spaces from the record.
            partner_id = models.execute_kw(
                db,
                uid,
                password,
                "res.partner",
                "search",
                [[["email", "=", rec["email"].strip()]]],
            )
            vals = {
                "name": rec["name"].strip(),
                "email": rec["email"].strip(),
                "phone": rec["phone"].strip(),
                "city": rec["city"].strip(),
            }
            if not partner_id:
                partner_id = models.execute_kw(
                    db, uid, password, "res.partner", "create", [vals]
                )
            else:
                partner_id = models.execute_kw(
                    db, uid, password, "res.partner", "write", [[partner_id[0]], vals]
                )
            print("\n\n:::::::::excel_row:::::::::::::::", excel_row)

        excel_row += 1

    search_partner_is = models.execute_kw(
        db, uid, password, "res.partner", "search", [[["city", "=", "Berlin"]]]
    )
    print("search_partner_is################", search_partner_is)

    remove_city_partner_id = models.execute_kw(
        db, uid, password, "res.partner", "search", [[["city", "=", "Berlin"]]]
    )
    print("remove city################", remove_city_partner_id)
    models.execute_kw(
        db,
        uid,
        password,
        "res.partner",
        "unlink",
        [[partner for partner in remove_city_partner_id]],
    )

    partner_count = models.execute_kw(
        db, uid, password, "res.partner", "search_count", [[]]
    )
    print("partner_count#######@########", partner_count)

# models.execute_kw(db, uid, password, 'res.partner', 'write',[[14], {
#     'country_id': "united state" }])
