#!/usr/bin/env python3
''' Learning to use classes by simulating a company environment '''

class Employee:
    ''' Worker information '''
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    def description(self):
        ''' Print full name with hourly pay '''
        print(self.first, self.last, "Hourly Pay:", self.pay)
    def daily_pay(self):
        return self.pay * 8
    def salary(self):
        ''' Calculate monthly wage, assuming it's a 30 day month '''
        return self.daily_pay() * 30

emp1 = Employee("Ethan", "Cha", 9.75)
emp2 = Employee("Corey", "Schafer", 10.95)

emp2.description()
print(emp2.daily_pay())
print(emp2.salary())