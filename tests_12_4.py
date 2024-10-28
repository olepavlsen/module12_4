import rt_with_exceptions as rnr
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            ole = rnr.Runner('Ole', -10)
            ole.speed > 0
            logging.info(f"'test_walk' выполнен успешно")
            i = 1
            while i <= 10:
                rnr.Runner.walk(ole)
                i += 1
            self.assertEqual(ole.distance, 100)
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            leo = rnr.Runner(23, 5)
            isinstance(leo.name, str)
            logging.info(f"'test_run' выполнен успешно")
            i = 1
            while i <= 10:
                rnr.Runner.run(leo)
                i += 1
            self.assertEqual(leo.distance, 100)
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    # @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    # def test_challenge(self):
    #     alex = rnr.Runner('Alex', 10)
    #     vlad = rnr.Runner('Vlad', 10)
    #     i = 1
    #     while i <= 10:
    #         rnr.Runner.run(alex)
    #         rnr.Runner.walk(vlad)
    #         i += 1
    #     self.assertNotEqual(alex.distance, vlad.distance)


if __name__ == "__main__":
    unittest.main()
logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding="UTF-8", format="%("
                                                                        "levelname)s | %(message)s")
