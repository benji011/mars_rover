import unittest
import subprocess


class TestRover(unittest.TestCase):
    def test_move_rover_example_1(self):
        process = subprocess.Popen(
            ["python", "main.py", "test_input_1.txt"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        output, error = process.communicate()
        expected_output = "(4, 4, E)\n(0, 4, W) LOST"
        self.assertEqual(output.decode().strip(), expected_output)
        self.assertEqual(error, b"")

    def test_move_rover_example_2(self):
        process = subprocess.Popen(
            ["python", "main.py", "test_input_2.txt"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        output, error = process.communicate()
        expected_output = "(2, 3, W)\n(1, 0, S) LOST"
        self.assertEqual(output.decode().strip(), expected_output)
        self.assertEqual(error, b"")
