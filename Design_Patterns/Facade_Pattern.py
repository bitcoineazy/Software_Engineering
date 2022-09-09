"""
Фасад (Facade) - паттерн, структурирующий объекты.
Предоставляет унифицированный интерфейс вместо набора интерфейсов некоторой подсистемы.
Фасад определяет интерфейс более высокого уровня, который упрощает использование подсистемы.

Шаблон «Фасад» предоставляет упрощённый интерфейс для сложной подсистемы.
«Фасад» — это объект, предоставляющий упрощённый интерфейс для более крупного тела кода, например библиотеки классов.

Фасад — структурный шаблон проектирования, позволяющий скрыть сложность
системы путём сведения всех возможных внешних вызовов к одному объекту,
делегирующему их соответствующим объектам системы.
"""


class User:
    """Пользователь"""

    def __init__(self, name, surname, age, email):
        self._name = name
        self._surname = surname
        self._age = age
        self._email = email
        self._password = ""

    def say(self):
        print(f"Hello, my name is {self._name} {self._surname}.")


class Registration:
    """Регистрация пользователя и проверка пароля"""

    def register(self, user, password):
        # расширяем функциональность объекта добавляя возможность регистрации
        if not user._password:
            if password:
                user._password = password
                print(f"Пользователь {user._name} успешно зарегистрирован!\n"
                      f"Пароль: {user._password}")
            else:
                print("Пароль не может быть пустым!")
        else:
            user._password = password
            print(f"Пользователь {user._name} успешно сменил пароль!\n"
                  f"Пароль: {user._password}")


class Facade:
    def __init__(self):
        self._user = User('Иван', 'Иванов', 25, "ivanov@mail.ru")
        self._checkpassword = Registration()

    def check(self, password):
        self._checkpassword.register(self._user, password)


f = Facade()
f.check('12345')  # Пользователь Иван успешно зарегистрирован!
f.check('12345')  # Пользователь Иван успешно сменил пароль!