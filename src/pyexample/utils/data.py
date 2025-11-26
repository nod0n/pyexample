import pandas as pd

from externalcode2 import data_preprocessing


def prepare_data():
    print("Preparing data in pyexample.utils.data.")
    data_preprocessing.transform()
    print("Data preparation is complete.")


def main():
    prepare_data()
    print("Main function in pyexample.utils.data is done.")


def load():
    print("Loading data in pyexample.utils.data.")
    return pd.DataFrame()  # Example placeholder


if __name__ == "__main__":
    main()
