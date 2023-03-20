from unittest import TestCase
from derek_and_vishav import replace_all

class Test(TestCase):
    def test_replace_all(self):
        self.fail()

class TestReplaceAll(TestCase):


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_simple_game(self, mock_output):
        replace_all("input.txt", "output.txt", "watermelon", "strawberry")
        the_replaced_all = mock_output.getvalue()
        expected_output = f"Successfully replaced occurences of"
        self.assertEqual(expected_output, the_game_printed_this)
