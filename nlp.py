import json
import spacy
from collections import Counter
import pandas as pd

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Read the JSON file
with open('tweets.json', 'r') as f:
    tweets_data = json.load(f)

# Extract entities and calculate their frequency
entity_counter = Counter()
sentiments = {}  # To store sentiments of authors towards entities

for tweet in tweets_data:
    author = tweet['author']
    text = tweet['text']
    
    doc = nlp(text)
    
    # Extract entities and update the counter
    entities = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'PRODUCT']]  # Consider only ORG and PRODUCT entities
    entity_counter.update(entities)
    
    # Calculate sentiment/polarity using a simple rule-based approach
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


