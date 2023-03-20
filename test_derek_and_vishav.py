from unittest import TestCase
from derek_and_vishav import replace_all

class Test(TestCase):
    def test_replace_all(self):
        self.fail()

class TestSimpleGame(TestCase):

    @patch('builtins.input', side_effect=[1, 10, 5])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_simple_game(self, mock_output, random_number_generator, mock_input):
        simple_game()
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You're right!\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[1, 10, 5])
    @patch('random.randint', return_value=6)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_simple_game_too_low(self, mock_output, random_number_generator, mock_input):
        simple_game()
        the_game_printed_this = mock_output.getvalue()
        expected_output = "Too low, the number was 6\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[1, 10, 5])
    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_simple_game_too_high(self, mock_output, random_number_generator, mock_input):
        simple_game()
        the_game_printed_this = mock_output.getvalue()
        expected_output = "Too high, the number was 4\n"
        self.assertEqual(expected_output, the_game_printed_this)

