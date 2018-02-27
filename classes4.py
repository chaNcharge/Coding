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
        return self.first + " " + self.last + " " + "Hourly Pay: " + str(self.pay)
    def daily_pay(self):
        ''' Calculate daily pay, assuming 8 work hours '''
        return round(self.pay * 8, 2)
    def monthly(self):
        ''' Calculate monthly wage, assuming it's a 30 day month '''
        return round(self.daily_pay() * 30, 2)
    def salary(self):
        ''' Calculate yearly salary from monthly '''
        return round(self.monthly() * 12, 2)

emp1 = Employee("Ethan", "Cha", 9.75)
emp2 = Employee("Corey", "Schafer", 10.95)

print(emp2.description())
print(emp2.daily_pay())
print(emp2.salary())