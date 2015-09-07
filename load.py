__author__ = 'gsriniv1'
import Company
import csv

F1KFILE="fortune1000-2014.csv"

csvfile = csv.DictReader(open(F1KFILE))
cs=Company.Companies()
for row in csvfile:
    try:
        nm=row.get('NAME')
        print("Company " , nm)
        c=Company.Company(nm)
        c.setProperties(row.get('WEBSITE') , street=row.get('STREETADD'),place=row.get("PLACE"),zip=row.get("ZIP"),state=row.get("STATE"))
        cs.addCompany(c)
    except:
        pass

cs.show()
