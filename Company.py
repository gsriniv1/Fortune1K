__author__ = 'gsriniv1'
class Company:
    def __init__(self,nm):
        self._name = nm
        self._website='Unknown'

    def __str__(self):
        return "Company: %s " % self._name

    def show(self):
        print("Company %s " % self._name , " website : %s" % self._website)

    def setProperties(self,website,street='',place='',zip='',state='',country='USA'):
        self._website=website
        self._street=street
        self._place=place
        self._zip=zip
        self._state=state
        self._country=country

class Companies:
    def __init__(self):
        self._all = []
    def addCompany(self,c):
        self._all.append(c)
    def show(self):
        print("Total number of companies: ",len(self._all))
        for c in self._all:
            c.show()
        print("Total number of companies: ",len(self._all))