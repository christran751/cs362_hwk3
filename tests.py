import random
import unittest
from credit_card_validator import credit_card_validator

class TestCreditCard(unittest.TestCase):
    """
    Sample docstring
    """
    def generate_random_number(self, length):
        random_length_offset = random.choice([-1, 0, 1])
        length += random_length_offset
        val = ''.join(random.choices("0123456789", k=length))
        return val

    def test_credit_card(self):
        for _ in range(100000):
            val = self.generate_random_number(random.randint(16, 17))
            credit_card_validator(val)

if __name__ == "__main__":
    unittest.main()



