from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd


def make_wordcloud(file):

    df = pd.read_csv(file, sep=';')

    keywords = df.dropna(subset=['keywords'], axis=0)['keywords'] #apaga os valores nulos da coluna keywords

    all_keywords = ' '.join(k for k in keywords) #junta todas as keywords em uma lista somente

    # lista de stopwords
    stopwords = set(STOPWORDS)
    stopwords.update(['da','meu','em','voce','de','ao','os'])

    # gerar uma wordcloud
    wordcloud = WordCloud(stopwords=stopwords, background_color='white', width=1600, height=800).generate(all_keywords)

    # gera imagem final
    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_axis_off()

    plt.imshow(wordcloud)
    wordcloud.to_file('analise_sentimentos_tribunais_wordcloud.png')

    print('Nuvem de palavras gerada com sucesso!')