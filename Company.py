__author__ = 'gsriniv1'
class Company:
    def __init__(self,nm):
        self._name = nm
    def __str__(self):
        return "Company: %s" % self._name