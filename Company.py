__author__ = 'gsriniv1'
import string
class Company:
    def __init__(self,nm):
        self._name = nm
        self._website='Unknown'

    def __str__(self):
        return "Company: %s " % self._name

    def show(self):
        print("Company %s " % self._name , " website : %s " % self._website , " ticker %s " % self._ticker )

    def setProperties(self,website,street='',place='',zip='',state='',country='USA',ticker=''):
        self._website=website
        self._street=street
        self._place=place
        self._zip=zip
        self._state=state
        self._country=country
        self._ticker=ticker

    def setTicker(self,ticker):
        self._ticker=ticker

    def getName(self):
        return self._name

    def sameAs(self,nm):
        if nm in self._name:
            return True
        if self._name in nm:
            return True
        return False

class Companies:
    def __init__(self):
        self._all = []
        self._lookup = {}

    def addCompany(self,c):
        self._all.append(c)
        self._lookup[c.getName()] = c

    def searchCompany(self,nm):
        for c in self._all:
            if c.sameAs(nm) == True:
                return c
        return None

    def lookupCompany(self,nm):
        try:
            return self._lookup[nm]
        except:
            return self.searchCompany(nm)

    def show(self):
        print("Total number of companies: ",len(self._all))
        for c in self._all:
            c.show()
        print("Total number of companies: ",len(self._all))