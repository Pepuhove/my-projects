import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def load_data(file_path):
    return pd.read_csv(file_path)

def positive_words():
    with open("positive_words.txt", "r") as file:
        positive_words = file.read().splitlines()
    return positive_words

def negative_words():
    with open("negative_words.txt", "r") as file:
        negative_words = file.read().splitlines()
    return negative_words

def get_sentiment_score(tweet, pos_words, neg_words):
    positive_score = len([word for word in tweet if word in pos_words])
    negative_score = len([word for word in tweet if word in neg_words])
    net_score = positive_score - negative_score
    return positive_score, negative_score, net_score

def process_tweet(tweet):
    tweet = tweet.lower()
    tokens = word_tokenize(tweet)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    return tokens

def generate_resulting_data(data):
    pos_words = positive_words()
    neg_words = negative_words()

    resulting_data = []

    for index, row in data.iterrows():
        tweet = process_tweet(row["Text"])
        pos_score, neg_score, net_score = get_sentiment_score(tweet, pos_words, neg_words)
        resulting_data.append([row["Number of Retweets"], row["Number of Replies"], pos_score, neg_score, net_score])

    resulting_df = pd.DataFrame(resulting_data, columns=["Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", "Net Score"])
    resulting_df.to_csv("resulting_data.csv", index=False)

if __name__ == "__main__":
    data = load_data("project_twitter_data.csv")
    generate_resulting_data(data)
