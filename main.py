import config
import loader


def main():
    df = loader.clean_data(loader.load_data())
    print(df.info)
    for c in config.FACTOR_COLS:
        print(df[c].describe())


if __name__ == "__main__":
    main()
