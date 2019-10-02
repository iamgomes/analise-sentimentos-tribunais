def main():
    content = {}

    content['searchTerm'] = askAndReturnSearchTerm()

    print(content)

def askAndReturnSearchTerm():
    return input('Digite o termo a ser pequisado no Twitter: ')


if __name__ == "__main__":
    main()