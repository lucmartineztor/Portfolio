from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def main():

    sid_obj = SentimentIntensityAnalyzer()
    sentence=input('text: ')
    sentiment_dict = sid_obj.polarity_scores(sentence)
         
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
     
    print("Positive") if sentiment_dict['compound'] >= 0.05 else (print("Negative") if sentiment_dict['compound'] <= - 0.05 else print("Neutral"))

if __name__ == "__main__":
    main()


