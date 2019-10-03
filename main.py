from robots.twitter import robotTwitter


def main():
    # cria dicionário de dados e sua estrutura
    content = {}

    content['searchTerm'] = askAndReturnSearchTerm()
    content['tweetContentOriginal'] = robotTwitter(content['searchTerm'])

    print(content)

def askAndReturnSearchTerm():
    return input('Digite o termo a ser coletado no Twitter: ')


if __name__ == "__main__":
    main()