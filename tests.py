import random
import unittest
from credit_card_validator import credit_card_validator


class TestCreditCard(unittest.TestCase):
    """
    Use random testing to generate random numbers to trigger all 8 bugs in
    order to come up with theories as to why the bug occured.
    """
    def generate_random_number(self, length):
        """
        Generate a numeric string of a given length
        """
        return ''.join(random.choices("0123456789", k=length))

    def test_credit_card(self):
        """
        Randomized test to explore different cases that might trigger bugs.
        """
        for _ in range(694200):
            val = self.generate_random_number(random.randint(1, 17))
            credit_card_validator(val)


if __name__ == "__main__":
    unittest.main()
