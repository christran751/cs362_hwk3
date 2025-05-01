import random
import unittest
from credit_card_validator import credit_card_validator

class TestCreditCard(unittest.TestCase):
    """
    Sample docstring
    """
    random.seed(42)
    valid_length = [15, 16]
    invalid_length = [random.randint(0, 14), 17]

    def generate_random_number(self, length):
        val = ""
        for i in range(length):
            val = val + str(random.randint(0, 9))
        return val

    def test_credit_card(self):
        for _ in range(100000):
            if random.choice([True, False]):
                length = random.choice(self.invalid_length)
            else:
                length = random.choice(self.valid_length)
            credit_card_validator(self.generate_random_number(length))


if __name__ == "__main__":
    unittest.main()



