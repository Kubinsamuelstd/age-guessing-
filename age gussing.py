from datetime import date


class person_details:
    def _init_(self,name,contry,dob):
        self.name=name
        self.dob=dob
        self.contry=contry
    def calculating_age(self):
      today=date.today()
      age=today.year - self.dob.year
      if today<date(today.year,self.dob.month,self.dob.day):
          age-=1
          return age

person=person_details("kubin","india",date(2003,10,16))
print(person)
print(person.name)
print(person.calculating_age())
print(person.contry)