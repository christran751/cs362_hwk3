import random
import unittest
from credit_card_validator import credit_card_validator

class TestCreditCard(unittest.TestCase):
    """
    Sample docstring
    """

    length = [16, 17]

    def generate_random_number(self, length):
        val = ""
        chance = random.choice([1, 2, 3])
        if chance == 1:
            length -= 1
        elif chance == 2:
            length += 1
        else:
            length = length

        for i in range(length):
            val = val + str(random.randint(0, 9))
        return val

    def test_credit_card(self):
        for _ in range(100000):
            credit_card_validator(self.generate_random_number(random.choice(self.length)))


if __name__ == "__main__":
    unittest.main()



