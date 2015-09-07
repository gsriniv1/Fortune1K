__author__ = 'gsriniv1 and RajaSrinivasan'
import Company
import csv

F1KFILE="fortune1000-2014.csv"
TICKERSYMFILE="companylist.csv"

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

print("Now loading Ticker symbol file")
tickerfile=csv.DictReader(open(TICKERSYMFILE))
for row in tickerfile:
    try:
        tickersym=row.get("Symbol")
        # print(tickersym)
        tickercompany=row.get("Name")
        print(tickercompany)
        c=cs.lookupCompany(tickercompany)
        c.setTicker(tickersym)
        # c.show()
    except:
        pass

cs.show()
