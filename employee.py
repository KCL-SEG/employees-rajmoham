"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee():
    total_pay = 0
    output = ""
    def __init__(self, name, contract_type, *args):
        self.name = name
        self.contract_type = contract_type
        args = list(args)

        self.total_pay = 0
        self.output += f"{self.name} works on a "

        if contract_type == "monthly":
            self.salary = args.pop(0)
            self.total_pay += self.salary
            self.output += f"monthly salary of {self.salary}"
            
        elif contract_type == "hourly":
            self.hours_worked = args.pop(0)
            self.hourly_rate = args.pop(0)
            self.total_pay += self.hours_worked * self.hourly_rate
            self.output += f"contract of {self.hours_worked} hours at {self.hourly_rate}/hour"

        if (len(args) == 1):
            self.bonus = args.pop(0)
            self.total_pay += self.bonus
            self.output += f" and receives a bonus commission of {self.bonus}"
        elif (len(args) == 2):
            self.contracts_sold = args.pop(0)
            self.contract_rate = args.pop(0)
            self.total_pay += self.contracts_sold * self.contract_rate
            self.output += f" and receives a commission for {self.contracts_sold} contract(s) at {self.contract_rate}/contract"

        self.output += f".  Their total pay is {self.total_pay}."

    def get_pay(self):
        return self.total_pay

    def __str__(self):
        return self.output


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly", 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", 120, 30, 600)
