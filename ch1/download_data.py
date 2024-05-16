import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def main():
    url = "https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt"
    df = pd.read_csv(url, sep='\t')

    print(df.head())


if __name__ == '__main__':
    main()
