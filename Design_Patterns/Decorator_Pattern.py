"""
Декоратор (Decorator, Wrapper) - паттерн, структурирующий объекты.

Динамически добавляет объекту новые обязанности.
Является гибкой альтернативой порождению подклассов с целью расширения функциональности.


Шаблон «Декоратор» позволяет во время выполнения динамически изменять поведение объекта, обёртывая его в объект класса «декоратора».

Шаблон «Декоратор» позволяет подключать к объекту дополнительное поведение (статически или динамически),
 не влияя на поведение других объектов того же класса. Шаблон часто используется для соблюдения принципа
  единственной обязанности (Single Responsibility Principle), поскольку позволяет разделить функциональность
   между классами для решения конкретных задач.

Структурный шаблон проектирования, предназначенный для
динамического подключения дополнительного поведения к объекту.
 Шаблон декоратор предоставляет гибкую альтернативу практике
  создания подклассов с целью расширения функциональности.
"""


class User(object):
    """Пользователь"""

    def __init__(self, name, surname, age, email):
        self._name = name
        self._surname = surname
        self._age = age
        self._email = email

    def say(self):
        print(f"Hello, my name is {self._name} {self._surname}.")


class Registration(object):
    """Регистрация пользователя"""

    def __init__(self, user_model, password):
        self._user = user_model  # Объект пользователя
        self._password = password

    def __getattr__(self, item):
        return getattr(self._user, item)

    def register(self):
        # расширяем функциональность объекта добавляя возможность регистрации
        if self._password:
            self._user._password = self._password
            print(f"Пользователь {self._user._name} успешно зарегистрирован!\n"
                  f"Пароль: {self._user._password}")
        else:
            print("Пароль не может быть пустым!")


user = User('Иван', 'Иванов', 25, "ivanov@mail.ru")

user_registration = Registration(user, '12345')

user_registration.say()  # Hello, my name is Иван Иванов.
user_registration.register()  # Пользователь Иван успешно зарегистрирован!
