# Import necessary libraries
import pandas as pd
import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Download NLTK resources
nltk.download('punkt')          # Tokenizer
nltk.download('stopwords')      # Stopwords list
nltk.download('wordnet')        # Lemmatizer
nltk.download('omw-1.4')        # Lemma dictionary

# Load your dataset
file_path = 'businessday_final3.csv'  # Replace with your dataset file path
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("Original Dataset:")
print(df.head())

# Step 1: Data Cleaning
# Convert text to lowercase
df['Excerpt_cleaned'] = df['Excerpt'].str.lower()

# Remove punctuation and special characters
df['Excerpt_cleaned'] = df['Excerpt_cleaned'].str.replace(f"[{string.punctuation}]", "", regex=True)

# Tokenize the text
df['Excerpt_tokens'] = df['Excerpt_cleaned'].apply(word_tokenize)

# Remove stop words
stop_words = set(stopwords.words('english'))
df['Excerpt_tokens'] = df['Excerpt_tokens'].apply(lambda tokens: [word for word in tokens if word not in stop_words])

# Lemmatize the tokens
lemmatizer = WordNetLemmatizer()
df['Excerpt_tokens'] = df['Excerpt_tokens'].apply(lambda tokens: [lemmatizer.lemmatize(word) for word in tokens])

# Combine tokens back into a single string
df['Excerpt_cleaned'] = df['Excerpt_tokens'].apply(lambda tokens: " ".join(tokens))

# Display the cleaned dataset
print("\nCleaned Dataset:")
print(df[['Title', 'Excerpt_cleaned']].head())

# Step 2: Sentiment Analysis
# Calculate polarity using TextBlob
df['polarity'] = df['Excerpt_cleaned'].apply(lambda text: TextBlob(text).sentiment.polarity)

# Classify sentiment based on polarity
def classify_sentiment(polarity):
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['polarity'].apply(classify_sentiment)

# Display the dataset with sentiment analysis
print("\nDataset with Sentiment Analysis:")
print(df[['Title', 'Excerpt_cleaned', 'polarity', 'sentiment']].head())

# Step 3: Sentiment Visualization
# Count the number of articles for each sentiment
sentiment_counts = df['sentiment'].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis')

# Add labels and title
plt.title('Sentiment Analysis', fontsize=16)
plt.xlabel('Sentiment', fontsize=12)
plt.ylabel('Number of Articles', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Add value labels on the bars
for index, value in enumerate(sentiment_counts.values):
    plt.text(index, value, str(value), ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()

# Save the updated dataset to a new CSV file
output_file = 'businessday_with_sentiment.csv'
df.to_csv(output_file, index=False)
print(f"\nUpdated dataset saved to '{output_file}'") 