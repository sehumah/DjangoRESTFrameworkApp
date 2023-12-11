import requests


# consume or use the REST API created in this project
def consume():
    url = 'http://localhost:8000/drinks/'
    response = requests.get(url)
    print(response.json())


def main():
    consume()


if __name__ == '__main__':
    main()
