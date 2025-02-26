from modules.core import file_converter


def main():
    f = file_converter("src/sound1.mp3")
    print(f.get_pandas())
    print(f.get_sampling_rate())

if __name__ == "__main__":
    main()