class Human:
    def __init__(self):
        #set default = high, not allow user enter
        self._intelligence = 'high'

class Vietnamese(Human):
    def __init__(self, name):
        self.name = name
        Human.__init__(self)

    def showinfo(self):
        print('Name: ', self.name,'IQ level: ', self._intelligence)

nguoi = Vietnamese('Ho Chi Minh')
nguoi.showinfo()
#not work 'caused protected:
#print("Iq: ", self._intelligence)