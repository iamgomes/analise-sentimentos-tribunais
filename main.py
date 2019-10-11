import robots.twitter as robot
from robots.watson import sentimentWatson, keywordsWatson

def main():
    # cria dicionário de dados e sua estrutura
    content = {}

    content['searchTerm'] = askAndReturnSearchTerm()
    contentTweets = robot.downloadTweets(content['searchTerm'])
    content['tweet'] = []

    for i in contentTweets:

        try:        
            data = {
                'user_id': i['user_id'],
                'user': i['user'],
                'TextOriginal': i['text'],
                'TextSanitized': i['text_sanitized'],
                'location': i['location'],
                'place': i['place'],
                'tweet_lon': i['tweet_lon'],
                'tweet_lat': i['tweet_lat'],
                'followers_count': i['followers_count'],
                'verified': i['verified'],
                'created_at': i['created_at'],
                'sentiment': sentimentWatson(i['text_sanitized']),
                'keywords': keywordsWatson(i['text_sanitized'])
            }
            
            content['tweet'].append(data)

            print('Aplicando análise de sentimentos com o Watson...,')

        except:
            print('Não foi possível aplicar o Watson!')
 
    print(content)

def askAndReturnSearchTerm():
    """
    inserir termo para busca inclusive com operadores avançados de pesquisa do twitter (OR, AND, -, #, FROM, TO, @, SINCE, UNTIL)
    """
    return input('Digite o termo a ser pesquisado no Twitter: ') 


if __name__ == "__main__":
    main()