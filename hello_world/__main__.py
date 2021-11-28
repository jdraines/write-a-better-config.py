from termcolor import cprint, colored
from .config import CONFIG


def main():

    text = colored('Hello, World!', CONFIG.color, attrs=CONFIG.attrs)
    print(text)


if __name__ == "__main__":

    # Uncomment the line below to try out the test mode config
    CONFIG.set_test_mode_enabled(True)

    main()