import unittest
from Tests_12_3 import RunnerTest, TournamentTest

# Создаем декоратор для проверки атрибута is_frozen
def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)
    return wrapper

# Применяем декоратор ко всем тестовым методам
class CustomRunnerTest(RunnerTest):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        super().test_challenge()

    @skip_if_frozen
    def test_run(self):
        super().test_run()

    @skip_if_frozen
    def test_walk(self):
        super().test_walk()

class CustomTournamentTest(TournamentTest):
    is_frozen = True

    @skip_if_frozen
    def test_usain_nick(self):
        super().test_usain_nick()

    @skip_if_frozen
    def test_andrey_nick(self):
        super().test_andrey_nick()

    @skip_if_frozen
    def test_usain_andrey_nick(self):
        super().test_usain_andrey_nick()

# Создание TestSuite
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(CustomRunnerTest))
suite.addTest(unittest.makeSuite(CustomTournamentTest))

# Исполнение тестов
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)