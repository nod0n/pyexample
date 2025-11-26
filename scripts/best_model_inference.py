#!/usr/bin/env python3
from pyexample.utils import data
from pyexample.models import baseline


def main():
    data.prepare_data()
    baseline.forward("some input")


if __name__ == "__main__":
    main()
