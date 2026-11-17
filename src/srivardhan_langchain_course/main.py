import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("welcome srivardhan")
    print(__name__)
    print(os.environ.get("GOOGLE_API_KEY"))


if __name__ == "__main__":
    main()
