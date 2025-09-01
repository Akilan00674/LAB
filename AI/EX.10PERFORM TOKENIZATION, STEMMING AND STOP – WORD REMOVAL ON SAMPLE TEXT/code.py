import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required resources (only once needed)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Sample text
text = """Perform tokenization, stemming, and stop-word removal on sample text."""

# Tokenization
tokens = word_tokenize(text)

# Stop-word removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words and word.replace("-", "").isalpha()]

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Output
print("Original Tokens: ", tokens)
print("Filtered Tokens (no stop-words): ", filtered_tokens)
print("Stemmed Tokens: ", stemmed_tokens)
