def countdown(n):
    """
    Prints a countdown from n to 0.
    """
    while n >= 0:
        print(f"Countdown: {n}")
        n -= 1

if __name__ == "__main__":
    countdown(5)

    # Extra Credit: Unit Test
    import unittest

    class TestCountdown(unittest.TestCase):
        def test_countdown(self):
            from io import StringIO
            import sys
            saved_stdout = sys.stdout
            try:
                out = StringIO()
                sys.stdout = out
                countdown(3)
                output = out.getvalue().strip().split("\n")
                self.assertEqual(output, ["Countdown: 3", "Countdown: 2", "Countdown: 1", "Countdown: 0"])
            finally:
                sys.stdout = saved_stdout

    unittest.main(argv=[''], exit=False)
