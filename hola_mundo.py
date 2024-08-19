import os


def main():
    name = os.getenv('USERNAME')
    print(f'Hello {name} from GitHub Actions!!! :)')


if __name__ == '__main__':
    main()
