from Module_12_2 import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner(name="Усэйн", speed=10)
        self.runner_andrey = Runner(name="Андрей", speed=9)
        self.runner_nick = Runner(name="Ник", speed=3)

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