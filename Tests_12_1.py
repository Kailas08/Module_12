from Module12_1 import Runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        # Создаем объект класса Runner
        runner = Runner("Бегун 1")
        # Вызываем метод walk 10 раз
        for _ in range(10):
            runner.walk()
        # Проверяем, что distance равен 50
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        # Создаем объект класса Runner
        runner = Runner("Бегун 2")
        # Вызываем метод run 10 раз
        for _ in range(10):
            runner.run()
        # Проверяем, что distance равен 100
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        # Создаем 2 объекта класса Runner
        runner1 = Runner("Бегун 3")
        runner2 = Runner("Бегун 4")
        # Вызываем методы run и walk соответственно
        for _ in range(10):
            runner1.run()
            runner2.walk()
        # Проверяем, что distances не равны
        self.assertNotEqual(runner1.distance, runner2.distance)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()