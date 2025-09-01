import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

pairs = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I am fine, thank you!",
    "bye": "Goodbye! Have a nice day.",
    "what is ai": "AI is the simulation of human intelligence in machines."
}

# Chat function
def chatbot_response(user_input):
    user_input = user_input.lower()
    vectorizer = TfidfVectorizer()
    keys = list(pairs.keys())
    tfidf = vectorizer.fit_transform(keys + [user_input])
    similarity = cosine_similarity(tfidf[-1], tfidf[:-1])
    index = similarity.argmax()
    return pairs[keys[index]]

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Chatbot:", pairs["bye"])
        break
    print("Chatbot:", chatbot_response(user))