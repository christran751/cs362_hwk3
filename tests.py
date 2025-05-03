import random
import unittest
from credit_card_validator import credit_card_validator


class TestCreditCard(unittest.TestCase):
    """
    Use random testing to generate random numbers to trigger all 8 bugs in
    order to come up with theories as to why the bug occured.
    """
    def generate_random_number(self, length):
        # random_length_offset = random.choice([-1, 0, 1])
        # length += random_length_offset
        # return ''.join(random.choices("0123456789", k=length))
        num = "41"
        for i in range(length - 2):
            num += str(random.randint(0, 9))
        return num

    def test_credit_card(self):
        for _ in range(694200):
            # val = self.generate_random_number(random.randint(15, 16))
            val = self.generate_random_number(16)
            credit_card_validator(val)


if __name__ == "__main__":
    unittest.main()
