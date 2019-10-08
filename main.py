import robots.twitter as robot
from robots.watson import sentimentWatson

def main():
    # cria dicionário de dados e sua estrutura
    content = {}

    content['searchTerm'] = askAndReturnSearchTerm()
    robot.downloadTweets(content['searchTerm'])
    content['tweetContentOriginal'] = robot.robotTwitter(content['searchTerm'])
    content['sentiment'] = sentimentWatson(content['tweetContentOriginal'][0]['text'])

    print(content)


def askAndReturnSearchTerm():
    """
    inserir termo para busca inclusive com operadores avançados de pesquisa do twitter (OR, AND, -, #, FROM, TO, @, SINCE, UNTIL)
    """
    return input('Digite o termo a ser pesquisado no Twitter: ') 


if __name__ == "__main__":
    main()