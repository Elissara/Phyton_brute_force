import random

class ListGenerator:
    """
    Генератор строк из списка
    """
    def __init__(self, lines):
        """Инициализация генератора"""
        self.i = 0
        self.lines = lines

    def reset(self):
        self.i = 0

    def next(self):
        """Получение следущей строки"""
        if self.i >= len(self.lines):
            return None

        line = self.lines[self.i]
        self.i += 1
        return line

class FileLinesGenerator(ListGenerator):
    """
    Генератор строк из файла
    """
    def __init__(self, filepath):
        """Инициализация генератора"""
        self.i = 0
        with open(filepath) as f:
            file_data = f.read()
        lines = file_data.split('\n')
        super().__init__(lines)


class BadPasswordGenerator(FileLinesGenerator):
    """
    Генератор плохих=небезопасных паролей
    пример использования класса
    generator = BadPasswordGenerator()
    print(generator.next())
    print(generator.next())
    """
    def __init__(self, filepath='bad_passwords.txt'):
        super().__init__(filepath)


# пример использования класса
# generator = BadPasswordGenerator()
# print(generator.next())
# print(generator.next())




class GoodPasswordGenerator:
    """
    Генератор безопасных паролей
    generator2 = GoodPasswordGenerator()
    print(generator2.next())
    print(generator2.next())
    """
    def __init__(self, alphabet='1234567890qwertyuiopasdfghjklzxcvbnm'
                                'QWERTYUIOPASDFGHJKLZXCVBNM@#$%^&*()_+'):
        """Инициализация генератора"""
        self.alphabet = alphabet

    def reset(self):
        pass

    def next(self, length=10):
        """Получение следущего пароля"""
        password = ''
        for i in range(length):
            c = random.choice(self.alphabet)
            password += c
        return password


class BruteForceGenerator:
    """
    Генератор полным перебором
    """
    def __init__(self, alphabet='1234567890qwertyuiopasdfghjklzxcvbnm'
                                'QWERTYUIOPASDFGHJKLZXCVBNM@#$%^&*()_+', min_length=0):
         """Инициализация генератора"""
         self.alphabet = alphabet
         self.base = len(alphabet)
         self.min_length = min_length
         self.length = 0
         self.counter = 0


    def reset(self):
        self.length = self.min_length
        self.counter = 0

    def next(self):
        result = ''
        number = self.counter
        while number > 0:
            rest = number % self.base
            result = self.alphabet[rest] + result
            number = number // self.base

        while len(result) < self.length:
            result = self.alphabet[0] + result

        if self.alphabet[-1] * self.length == result:
            # встретили последний пароль для данной длины
            self.length += 1
            self.counter = 0
        else:
            self.counter += 1

        return result