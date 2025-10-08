#   1. Online Banking System
class Account:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.__balance = 0.0
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining Balance: ₹{self.__balance}")
        else:
            print("Insufficient funds!")
    def get_balance(self):
        return self.__balance

class SavingsAccount(Account):
    def __init__(self, account_holder, interest_rate):
        super().__init__(account_holder)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        print(f"Interest earned: ₹{interest}")
        return interest

class CheckingAccount(Account):
    def __init__(self, account_holder, overdraft_limit):
        super().__init__(account_holder)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            print(f"Withdrawn ₹{amount}. Balance after overdraft: ₹{new_balance}")
        else:
            print("Overdraft limit exceeded!")

savings = SavingsAccount("Ravi", 5)
savings.deposit(10000)
savings.calculate_interest()
checking = CheckingAccount("Anita", 2000)
checking.deposit(5000)
checking.withdraw(6500)


# 2. Library Management System
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Book: {self.title} | Author: {self.author}")

class User:
    def __init__(self, name, max_books):
        self.name = name
        self.max_books = max_books
        self.borrowed_books = []
    def borrow_book(self, book):
        if len(self.borrowed_books) < self.max_books:
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{self.name} cannot borrow more books.")
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")

class Student(User):
    def __init__(self, name):
        super().__init__(name, 3)

class Faculty(User):
    def __init__(self, name):
        super().__init__(name, 5)

book1 = Book("Python 101", "Guido")
book2 = Book("AI Basics", "Andrew Ng")
stu = Student("Datta")
fac = Faculty("Prof. Rao")
stu.borrow_book(book1)
fac.borrow_book(book1)
fac.borrow_book(book2)


# 3. Online Shopping Cart
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price

class Discount:
    def apply_discount(self, total):
        raise NotImplementedError

class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent
    def apply_discount(self, total):
        return total - (total * self.percent / 100)

class FixedDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount
    def apply_discount(self, total):
        return max(total - self.amount, 0)

class Cart:
    def __init__(self):
        self.items = []
        self.discount = None
    def add_item(self, item):
        self.items.append(item)
    def set_discount(self, discount):
        self.discount = discount
    def calculate_total(self):
        total = sum(item.get_price() for item in self.items)
        if self.discount:
            total = self.discount.apply_discount(total)
        print(f"Final Total: ₹{total}")
        return total

cart = Cart()
cart.add_item(Item("Shoes", 1500))
cart.add_item(Item("Bag", 1000))
cart.set_discount(PercentageDiscount(10))
cart.calculate_total()


# 4. Employee Management System
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def calculate_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def calculate_salary(self):
        return self.salary + self.bonus

class Developer(Employee):
    def __init__(self, name, salary, overtime_pay):
        super().__init__(name, salary)
        self.overtime_pay = overtime_pay
    def calculate_salary(self):
        return self.salary + self.overtime_pay

m = Manager("Kiran", 60000, 15000)
d = Developer("Datta", 40000, 10000)
print(f"Manager Salary: ₹{m.calculate_salary()}")
print(f"Developer Salary: ₹{d.calculate_salary()}")


# 5. Vehicle Rental System
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, name, rental_rate):
        self.name = name
        self.rental_rate = rental_rate
    @abstractmethod
    def calculate_rental(self, days):
        pass

class Car(Vehicle):
    def __init__(self, name, rental_rate, insurance_cost):
        super().__init__(name, rental_rate)
        self.insurance_cost = insurance_cost
    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.insurance_cost

class Bike(Vehicle):
    def calculate_rental(self, days):
        return self.rental_rate * days

car = Car("Sedan", 2000, 1000)
bike = Bike("Yamaha", 500)
print(f"Car rental for 3 days: ₹{car.calculate_rental(3)}")
print(f"Bike rental for 3 days: ₹{bike.calculate_rental(3)}")


# 6. Hotel Reservation System
class Room:
    def __init__(self, room_type, price):
        self.room_type = room_type
        self.__price = price
    def get_price(self):
        return self.__price
    def display_info(self):
        print(f"Room Type: {self.room_type}, Price per night: ₹{self.__price}")

class Customer:
    def __init__(self, name):
        self.name = name

class Reservation:
    def __init__(self, room, customer, nights):
        self.room = room
        self.customer = customer
        self.nights = nights
    def calculate_total(self):
        total = self.room.get_price() * self.nights
        print(f"{self.customer.name}'s total: ₹{total}")
        return total

room = Room("Deluxe", 3000)
cust = Customer("Datta")
res = Reservation(room, cust, 2)
res.calculate_total()


# 7. Student Management System
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}")

class GraduateStudent(Student):
    def __init__(self, name, age, grades, research_topic):
        super().__init__(name, age, grades)
        self.research_topic = research_topic
    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")

s1 = Student("Ravi", 20, "A")
s2 = GraduateStudent("Anu", 24, "A+", "AI and Robotics")
s1.display_info()
s2.display_info()


# 8. Inventory Management System
class Item:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.__price = price
        self.__quantity = quantity
    def update_quantity(self, amount):
        self.__quantity += amount
    def display_info(self):
        print(f"{self.category}: {self.name}, Price: ₹{self.__price}, Qty: {self.__quantity}")

class Electronics(Item):
    def __init__(self, name, price, quantity, warranty_period):
        super().__init__(name, "Electronics", price, quantity)
        self.warranty_period = warranty_period

class Furniture(Item):
    def __init__(self, name, price, quantity, material):
        super().__init__(name, "Furniture", price, quantity)
        self.material = material

tv = Electronics("Smart TV", 45000, 5, "2 years")
chair = Furniture("Wooden Chair", 2500, 10, "Teak Wood")
tv.display_info()
chair.display_info()


# 9. Social Media Platform
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def post(self, content):
        print(f"{self.username} posted: {content}")
    def comment(self, content):
        print(f"{self.username} commented: {content}")

class Admin(User):
    def delete_post(self, post):
        print(f"Admin {self.username} deleted the post: {post}")

u1 = User("Datta", "datta@mail.com")
a1 = Admin("AdminUser", "admin@mail.com")
u1.post("Hello world!")
a1.delete_post("Hello world!")


# 10. Game Development RPG Game
class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f"{self.name} attacked {enemy.name}! {enemy.name}'s health: {enemy.health}")

class Warrior(Character):
    def attack_enemy(self, enemy):
        print(f"{self.name} swings sword ⚔️!")
        super().attack_enemy(enemy)

class Mage(Character):
    def attack_enemy(self, enemy):
        print(f"{self.name} casts fireball 🔥!")
        super().attack_enemy(enemy)

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

warrior = Warrior("Arjun", 100, 25)
mage = Mage("Kiran", 80, 30)
enemy = Enemy("Goblin", 120)
warrior.attack_enemy(enemy)
mage.attack_enemy(enemy)
