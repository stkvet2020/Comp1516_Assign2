from unittest import TestCase
import unittest
import sys
import os
import io
import re
import main


class TestMain(TestCase):
    correct_output = 0
    correct_errors = 0

    @classmethod
    def setUpClass(cls):
        """ Sets up the Test Case """
        TestMain.correct_output = 0
        TestMain.correct_errors = 0
        print("Grading your Main Script... ")

    @classmethod
    def tearDownClass(cls):
        """ Tears down the Test Case """
        print("Number of correct script outputs: %d/5" % TestMain.correct_output)
        print("Number of correct script error handling: %d/3" % TestMain.correct_errors)


    def test_main_invalid_report_type(self):
        """ main.py test csv """
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            sys.argv = [
                "main.py",
                "invalid",
                "COMP1516"

            ]

            main.main()
            print("No error on output type and exit(0)")

        except SystemExit as e:
            output = out.getvalue().strip()
            self.assertEqual(output, "Invalid report type. Must be summary or school.")
            TestMain.correct_errors += 1

        finally:

            sys.stdout = saved_stdout

    def test_main_invalid_number_arguments(self):
        """ main.py test csv """
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            sys.argv = [
                "main.py"
            ]

            main.main()
            print("No error on output type and exit(0)")

        except SystemExit as e:
            output = out.getvalue().strip()
            self.assertEqual(output, "Invalid number of arguments.")
            TestMain.correct_errors += 1

        finally:

            sys.stdout = saved_stdout

    def test_main_invalid_number_school_arguments(self):
        """ main.py test csv """
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            sys.argv = [
                "main.py",
                "school"
            ]

            main.main()
            print("No error on output type and exit(0)")

        except SystemExit as e:
            output = out.getvalue().strip()
            self.assertEqual(output, "Not enough arguments for the School Report.")
            TestMain.correct_errors += 1

        finally:

            sys.stdout = saved_stdout


    def test_summary_output_valid(self):
        """ main.py phone text """
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            sys.argv = [
                "main.py",
                "summary"
            ]

            if os.path.exists("summary.txt"):
                os.remove("summary.txt")

            main.main()
            output = out.getvalue()
            expected_output = """^Report:          \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}
Number Schools:  3
Schools:         BCIT,SFU,UBC
Number Courses:  6
Number Students: 120
School Averages:
                 BCIT: 77.2%
                 SFU: 78.0%
                 UBC: 77.8%
School Minimums:
                 BCIT: 20.2%
                 SFU: 26.8%
                 UBC: 36.2%
School Maximums:
                 BCIT: 99.3%
                 SFU: 99.1%
                 UBC: 94.5%\s*
$"""

            sys.stdout = saved_stdout
            self._compare_output(expected_output, output)
            TestMain.correct_output += 1

            if os.path.exists("summary.txt"):
                fh = open("summary.txt")
                file_output = fh.read()
                fh.close()

                self._compare_output(expected_output, file_output)
                TestMain.correct_output += 1

                os.remove("summary.txt")
        finally:
            sys.stdout = saved_stdout

    def test_school_report_output_valid(self):
        """ main.py phone text """
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            sys.argv = [
                "main.py",
                "school",
                "BCIT"
            ]

            if os.path.exists("bcit.txt"):
                os.remove("bcit.txt")

            main.main()
            output = out.getvalue()
            expected_output = """^Report:          \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}
School:          BCIT
Number Courses:  3
Courses:         COMM1000,COMP1516,MATH1305
Number Students: 40
Average Grade:   77.2%
Median Grade:    85.8%
Top Student:     A0001007
Top Grade:       97.5%
Bottom Student:  A0001018
Bottom Grade:    30.3%\s*
$"""

            sys.stdout = saved_stdout
            self._compare_output(expected_output, output)
            TestMain.correct_output += 1

            if os.path.exists("bcit.txt"):
                fh = open("bcit.txt")
                file_output = fh.read()
                fh.close()

                self._compare_output(expected_output, file_output)
                TestMain.correct_output += 1

                os.remove("bcit.txt")

        finally:
            sys.stdout = saved_stdout

    def test_school_report_school_invalid(self):
        """ main.py phone text """
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            sys.argv = [
                "main.py",
                "school",
                "Unknown"
            ]
            main.main()
            output = out.getvalue()
            expected_output = """^School Unknown does NOT exist!\s*
$"""

            sys.stdout = saved_stdout
            self._compare_output(expected_output, output)
            TestMain.correct_output += 1

        finally:
            sys.stdout = saved_stdout

    def _compare_output(self, expected_output, actual_output):
        """ Compares the expected against the actual """
        expected_lines = expected_output.split("\n")
        output_lines = actual_output.split("\n")

        self.assertEqual(len(expected_lines), len(output_lines),
                         "Expected %d lines of output but got %d" % (len(expected_lines),
                                                                     len(output_lines)))

        for line_num in range(0, len(expected_lines)):
            if re.search(expected_lines[line_num], output_lines[line_num]) is None:
                print("Expected at Line %02d: %s" % (line_num, expected_lines[line_num]))
                print("Actual Output      : %s" % output_lines[line_num])

            self.assertIsNotNone(re.search(expected_lines[line_num], output_lines[line_num]),
                                 "Line %d of output doesn't match" % line_num)


if __name__ == "__main__":
    unittest.main()