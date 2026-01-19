import sys
from io import StringIO
from unittest.mock import patch

from spongebobify.main import main


def test_main_command():
    test_args = ["spongebobify", "hello", "world"]
    with patch.object(sys, "argv", test_args):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue().strip()
            # The output should contain 'hello world' (case-insensitive)
            assert "hello world" in output.lower()


def test_main_no_args():
    test_args = ["spongebobify"]
    with patch.object(sys, "argv", test_args):
        # argparse will call sys.exit(2) and print usage to stderr when args are missing
        with patch("sys.stderr", new=StringIO()) as fake_err:
            try:
                main()
            except SystemExit as e:
                assert e.code == 2

            assert "the following arguments are required: text" in fake_err.getvalue()


def test_version_flag():
    test_args = ["spongebobify", "--version"]
    with patch.object(sys, "argv", test_args):
        # argparse version action prints to stdout and exits with 0
        with patch("sys.stdout", new=StringIO()) as fake_out:
            try:
                main()
            except SystemExit as e:
                assert e.code == 0

            assert "spongebobify version:" in fake_out.getvalue()
