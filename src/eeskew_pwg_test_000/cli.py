import argparse

from eeskew_pwg_test_000.sarcasm import sarcastic_cowsay


def main():
    """Cowsay something sarcastically from the command line."""
    parser = argparse.ArgumentParser()
    parser.add_argument("speech")
    args = parser.parse_args()

    s = args.speech
    sarcastic_cowsay(s)
