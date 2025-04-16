import pandas as pd

# Load the dataset with sentiment analysis results
file_path = 'businessday_with_sentiment.csv'  # Replace with your dataset file path
df = pd.read_csv(file_path)

# Ensure the 'sentiment' column exists
if 'sentiment' not in df.columns:
    raise ValueError("The dataset does not contain a 'sentiment' column.")

# Calculate the total count for each sentiment
sentiment_counts = df['sentiment'].value_counts()

# Calculate the percentage for each sentiment
sentiment_percentages = (sentiment_counts / len(df)) * 100

# Display the results
print("Sentiment Analysis Results:")
for sentiment, count in sentiment_counts.items():
    percentage = sentiment_percentages[sentiment]
    print(f"{sentiment}: {count} articles ({percentage:.2f}%)")

# Optional: Save the results to a CSV file
results = pd.DataFrame({
    'Sentiment': sentiment_counts.index,
    'Count': sentiment_counts.values,
    'Percentage': sentiment_percentages.values
})
results.to_csv('sentiment_analysis_results.csv', index=False)
print("\nSentiment analysis results saved to 'sentiment_analysis_results.csv'") 