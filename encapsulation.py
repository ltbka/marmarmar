# =====================Инкапсуляция========================

# 1) Обьединение всез свойств и методов в одну капсулу или класс
# 2) Ограничение доступа к методам и атрибутам , т.е соерытие данных

# class Phone:
#     number = '+996702234543'
    
#     def _print_number(self):
#         print(f'my number is: {self.number}')
        
# my_phone = Phone()
# my_phone_print_number()


#class Phone:
#     number = '+996702234543'
    
#     def _print_number(self):
#         print(f'my number is: {self.number}')
        
# my_phone = Phone()
# my_phone._print_number()



# class Point:
#     def __init__(self, x=0, y=0, z=0) -> None:
#         self._x = x
#         self._y = y
#         self._z = z
#     def get_cordinats(self):
#         return self._x, self._y, self._z
    
#     def set_cordinats(self, x, y, z):
#         if type(x) in (int, float) and type (y) in (int, float) and type(z) in (int, float):
#             self.__ = x
#             self.__ = y
#             self.__ = z
#         else:
#             raise  ValueError ('Кординаты должны быть числами!')
            
        
# point = Point(2,3,4)
# # print(point._Point_x)
# point.set_cordinats(1,4.45,3) 
# print(point.get_cordinats())



# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self._age = age
        
#         @property
#         def age(self):
#             return self._age
        
#         @age.setter
#         def set_age(self, new_age):
#             if type (new_age) != int:
#                 raise ValueError("age must be integer")
#             if 0 < new_age and new_age < 100:
#                 self._age = new_age
#             else:
#                 raise Exception('age must be in range(0, 100)')
        
#         @age.getter
#         def get_age(self):
#             if self._age < 99:
#                 raise Exception ('we cant delete age')
#             del self._age 
            
             
# john = Person('john', '18')
# print(john.name) 
# john.set_age = 100
# john.delete_age
# print(john.get_age)
 
# class BankAccouunt:
#     def __init__(self, account_number, balance ) -> None:
#         self._account_number = account_number
#         self._balance = balance
    
    
#     def get_balance(self):
#         return self._balance
    
#     def set_balanse(self, new_balance):
#         if new_balance > 0:
#             self._balance += new_balance
#         else:
#             raise Exception('new_balanse должен быть больше 0')
        
#     def withdraw(self, amout):
#         if amout <= self._balance:
#             self._balance -= amout
#         else:
#             raise Exception('you don\'t have alot if balanse')
#     @property
#     def account_number(self):
#         return self._account_number
    
#     @account_number.getter
#     def get_account_number(self):
#         return self._account_number
    

# adilet = BankAccouunt('12345678', 1000)
# print(adilet.get_balance())
# adilet.withdraw(700) 
# print(adilet.get_balance())
# adilet.set_balanse(500)
# print(adilet.get_balance())
# print(adilet.get_account_number)          

            
""""            
Создайте класс Terminal. Создайте объект-карточку от этого класса, передав номер своей карточки и пин код. При этом,
необходимо проверить валидность карточки: номер карточки должен содержать строго 16 цифр, а пин код - 4 цифры (для этого используйте инкапсуляцию).
При создании карточки в ней содержится 0 сом. Далее в классе должны быть следующие методы:
метод put, который будет принимать в качестве аргументов: пин код карточки, вторым аргументом - сумму денег,
которую вы хотите закинуть на эту карточку. Прежде, чем закидывать деньги,
необходимо проверить введенный пин код на совпадение (используйте инкапсуляцию)

метод get_money, который также принимает первым аргументом пин код, вторым аргументом - сумму денег, которую вы хотите извлечь из карточки.
Здесь также необходимо использовать валидацию: проверка пин кода + сумма денег должна быть округленной до десятичных чисел, типа 10, 100, 200, 5000 и т.д. 
(67, 899, 45.6 - невалидные данные). И только после проверки деньги извлекаются.
Примените данные методы к своей карточке несколько раз и в конце выдайте, сколько денег на карточке.
Примечание: нельзя извлечь сумму денег, если она больше, чем сумма денег на карточке; также нельзя вытащить пин код карточки (эти данные должны быть скрыты
"""
class Terminal:
    def __init__(self, card_number, pin_code):
        self._card_number = self._validate_card_number(card_number)
        self._pin_code = self._validate_pin_code(pin_code)
        self._balance = 0

    def _validate_card_number(self, card_number):
        if isinstance(card_number, int) and len(str(card_number)) == 16:
            return card_number
        else:
            raise ValueError('Номер карты должен быть 16-ти значным целым числом ')

    def _validate_pin_code(self, pin_code):
        if isinstance(pin_code, int) and len(str(pin_code)) == 4:
            return pin_code
        else:
            raise ValueError('Пин код должен состоять из 4-х цифр ')

    def put(self, pin_code, amount):
        if pin_code == self._pin_code:
            if isinstance(amount, int) and amount > 0:
                self._balance += amount
                print(f'На карту успешно добавленна {amount}  сом')
            else:
                print('На карту успешно добавлена {amount} сом')
        else:
            print('Неправельный пин код!')

    def get_money(self, pin_code, amount):
        if pin_code == self._pin_code:
            if isinstance(amount, int) and amount % 10 == 0 and amount > 0 and amount <= self._balance:
                self._balance -= amount
                print(f'Сумма успешно снята')
            else:
                print('Недопустимая сумма. Пожалуйста, введите действительную сумму (положительное целое число, кратное 10).')
        else:
                print('Неправельный пин код!')

    def check_balance(self):
         return self._balance

card = Terminal(1234567890123456, 1234)
card.put(1234, 5000)
card.get_money(1111, 2500)

balance = card.check_balance()
print(f'"Баланс на карте составляет {balance} сом.')