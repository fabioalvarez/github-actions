import os


def main():
    name = os.getenv("USERNAME")
    print("Hola {name}, desde GitHub")

if __name__ == "__main__":
    main()