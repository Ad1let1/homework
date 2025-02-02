class MyAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, number):
        self.balance += number
        print(f"Пополнения на {number} На счете: {self.balance}")
    def withdraw(self, number):
        if(self.balance < number):
            print("Недостаточно денег")
        else:
            self.balance -= number
            print(f"Вы получили: {number} На счете: {self.balance}")
            
a = MyAccount(input("Имя: "), int(input("Сейчас на счету: ")))
a.deposit(100)
a.withdraw(200)
a.deposit(20)
a.withdraw(50)

        