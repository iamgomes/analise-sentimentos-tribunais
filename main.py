import robots.twitter as robot


def main():
    # cria dicionário de dados e sua estrutura
    content = {}

    content['searchTerm'] = askAndReturnSearchTerm()
    robot.downloadTweets(content['searchTerm'])
    #content['tweetContentOriginal'] = robot.robotTwitter(content['searchTerm'])

    print(content)

def askAndReturnSearchTerm():
    """
    inserir termo para busca inclusive com operadores avançados de pesquisa do twitter (OR, AND, -, #, FROM, TO, @, SINCE, UNTIL)
    """
    return input('Digite o termo a ser pesquisado no Twitter: ') 


if __name__ == "__main__":
    main()