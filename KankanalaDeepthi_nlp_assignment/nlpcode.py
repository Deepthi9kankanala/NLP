import json
import spacy
from collections import Counter
import pandas as pd

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Read the JSON file (replace 'tweets.json' with your JSON file path)
with open('/tweets.json', 'r') as f:
    tweets_data = json.load(f)

# Initialize counters and sentiment dictionary
entity_counter = Counter()
sentiments = {}

# Process each tweet (tweet_id is the numeric identifier)
for tweet_id, tweet in tweets_data.items():
    author = tweet['tweet_author']
    text = tweet['tweet_text']
    
    doc = nlp(text)
    
    # Extract entities and update the counter
    entities = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'PRODUCT']]
    entity_counter.update(entities)
    
    # Calculate sentiment/polarity (you can replace this with more advanced sentiment analysis)
    sentiment = 'Positive' if 'good' in text or 'tasty' in text else 'Negative'
    
    for entity in entities:
        if entity not in sentiments:
            sentiments[entity] = {}
        sentiments[entity][author] = sentiment

# Prepare and save Objective 1 CSV
objective1_data = [{'entity': entity, 'frequency': freq} for entity, freq in entity_counter.items()]
objective1_df = pd.DataFrame(objective1_data)
objective1_df.to_csv('objective1.csv', index=False)

# Prepare and save Objective 2 CSV
objective2_data = []
for entity, author_sentiments in sentiments.items():
    for author, sentiment in author_sentiments.items():
        overall_polarity = sentiment
        objective2_data.append({'entity': entity, 'author_name': author, 'overall_polarity': overall_polarity})

objective2_df = pd.DataFrame(objective2_data)
objective2_df.to_csv('objective2.csv', index=False)