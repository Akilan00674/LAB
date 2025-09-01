from textblob import TextBlob

text = input("Enter a sentence for sentiment analysis: ")

analysis = TextBlob(text)

polarity = analysis.sentiment.polarity


if polarity > 0:
    print("Sentiment: Positive 😊")
elif polarity < 0:
    print("Sentiment: Negative 😡")
else:
    print("Sentiment: Neutral 😐")
