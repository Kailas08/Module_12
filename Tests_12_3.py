import unittest
from Module12_1 import Runner as Runner1
from Module_12_2 import Runner as Runner2, Tournament

# Класс тестирования для Module12_1
class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        # Создаем объект класса Runner
        runner = Runner1("Бегун 1")
        # Вызываем метод walk 10 раз
        for _ in range(10):
            runner.walk()
        # Проверяем, что distance равен 50
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        # Создаем объект класса Runner
        runner = Runner1("Бегун 2")
        # Вызываем метод run 10 раз
        for _ in range(10):
            runner.run()
        # Проверяем, что distance равен 100
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        # Создаем 2 объекта класса Runner
        runner1 = Runner1("Бегун 3")
        runner2 = Runner1("Бегун 4")
        # Вызываем методы run и walk соответственно
        for _ in range(10):
            runner1.run()
            runner2.walk()
        # Проверяем, что distances не равны
        self.assertNotEqual(runner1.distance, runner2.distance)

# Класс тестирования для Module_12_2
class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner2(name="Усэйн", speed=10)
        self.runner_andrey = Runner2(name="Андрей", speed=9)
        self.runner_nick = Runner2(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            print(f"{test_name}: {result}")

    def test_usain_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results['Usain_Nick'] = {place: str(runner) for place, runner in results.items()}
        last_place = max(results.keys(), default=None)
        self.assertTrue(results[last_place] == "Ник")

    def test_andrey_nick(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results['Andrey_Nick'] = {place: str(runner) for place, runner in results.items()}
        last_place = max(results.keys(), default=None)
        self.assertTrue(results[last_place] == "Ник")

    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results['Usain_Andrey_Nick'] = {place: str(runner) for place, runner in results.items()}
        last_place = max(results.keys(), default=None)
        self.assertTrue(results[last_place] == "Ник")

# Запуск тестов
if __name__ == "__main__":
    unittest.main()