# //NLP
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary resources
nltk.download('vader_lexicon')

# Sample text
text = "I love this product! It's amazing."

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Perform sentiment analysis
sentiment_scores = sia.polarity_scores(text)

# Print the sentiment scores
for key, value in sentiment_scores.items():
    print(f"{key}: {value}")
