import robots.twitter as robot
from robots.watson import sentimentWatson, keywordsWatson

def main():
    # cria dicionário de dados e sua estrutura
    content = {}

    content['searchTerm'] = askAndReturnSearchTerm()

    contentTweets = robot.downloadTweets(content['searchTerm'])
    
    content['user_id'] = contentTweets[0]['user_id']
    content['user'] = contentTweets[0]['user']
    content['TextOriginal'] = contentTweets[0]['text']
    content['TextSanitized'] = contentTweets[0]['text_sanitized']
    content['location'] = contentTweets[0]['location']
    content['place'] = contentTweets[0]['place']
    content['followers_count'] = contentTweets[0]['followers_count']
    content['verified'] = contentTweets[0]['verified']
    content['created_at'] = contentTweets[0]['created_at']
    content['sentiment'] = sentimentWatson(contentTweets[0]['text'])
    content['keywords'] = keywordsWatson(contentTweets[0]['text'])

    print(content)


def askAndReturnSearchTerm():
    """
    inserir termo para busca inclusive com operadores avançados de pesquisa do twitter (OR, AND, -, #, FROM, TO, @, SINCE, UNTIL)
    """
    return input('Digite o termo a ser pesquisado no Twitter: ') 


if __name__ == "__main__":
    main()