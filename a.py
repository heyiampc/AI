# //Unification
from unification import unify

# Example usage
x = ['x', 'c', 'a']
y = ['f', 'd', 'B']
theta = unify(x, y)
print(theta)
if theta is not None and isinstance(theta, dict):
    print("Substitution:")
    for var, value in theta.items():
        print(var, "=", value)
else:
    print("Unification failed.")

# >>> from unification import *
# >>> unify(1, 1)
# {}
# >>> unify(1, 2)
# False
# >>> x = var('x')

# >>> unify((1, x), (1, 2))
# {~x: 2}

# >>> unify((x, x), (1, 2))
# False



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
