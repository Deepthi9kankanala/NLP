## Natural Language Processing Assignment: By BlackBucks 

# You are given a JSON file (tweets.json) that contains tweets (sentences) along with the name of the author.

- Objective 1: Get the most frequent entities from the tweets.

- Objective 2: Find out the sentiment/polarity of each author towards each of the entities.

# Sample Input:

Assume we have only 4 tweets:

- Tweet1 by Author1: Pink Pearl Apples are tasty but Empire Apples are not.
- Tweet2 by Author2: Empire Apples are very tasty.
- Tweet3 by Author3: Pink Pearl Apples are not tasty.
- Tweet4 by Author1: Pink Pearl Apples smells really good.

# Sample output:
- Entities in the topics extracted: Share a CSV with extracted entities and the frequency of the  extracted entity from all the tweets in the following format

 #  objective1.csv
- entity frequency
- Pink Pearl Apples 2
- Empire Apples 2

# Sentiment/polarity of Authors: Share a CSV file with predicted sentiment values with extracted entities as columns and unique authors as rows. See the example CSV below.

# Objective2.csv

- entity author_name overall_polarity
- Pink Pearl Apples Author1 Positive
- Empire Apples Author1 Negative
- Empire Apples Author2 Positive
- Pink Pearl Apples Author3 Negative

Downloading and reading the JSON file:

Get the JSON file here: 

https://drive.google.com/file/d/1U7HYZlvCRUr1ucDq_ActCkjPefmYGu_c/view?usp=sharing

Instructions:

Make sure to discuss the following aspects in a text document:

# Document your approach to solve the problem, discussing the difficulties and how your proposed solution tackles them.

- 1.Data Preprocessing: 
Text data often requires thorough preprocessing to clean and tokenize it effectively. This solution assumes that the input JSON data is well-structured and doesn't require additional preprocessing like removing special characters, stopwords, or handling emojis.
 - 2.Sentiment Analysis: 
The solution uses a simple rule-based approach for sentiment analysis based on the presence of certain keywords ("good," "tasty"). This approach might not be accurate for complex sentiment analysis, especially when dealing with more nuanced sentiments.
- 3.Entity Extraction: 
The solution uses spaCy's entity recognition for extracting entities from text. While spaCy is effective for common entities, it might not capture domain-specific or rare entities accurately.
 
# Discuss the technique used and the reason why you have chosen it.

- 1.spaCy: The spaCy library is utilized for entity recognition and natural language processing. It provides an efficient way to extract entities and perform linguistic analysis.
- 2.Counter: The Counter class is used to efficiently count the occurrences of different entities. This allows for quick extraction of the most frequent entities.
- 3.Pandas: The pandas library is used to handle and manipulate data in tabular form, making it easier to create CSV files from processed data.

# Discuss the shortcomings or mistakes of your proposed solution with a few examples.
- 1.spaCy: spaCy is a widely used NLP library known for its speed and accuracy. It's chosen here for its entity recognition capabilities.
- 2.Rule-Based Sentiment Analysis: For the purpose of this example, a simple rule-based sentiment analysis approach is used due to its simplicity. More advanced sentiment analysis methods like using pre-trained models might require more resources and time for integration.
- 3.Counter and Pandas: These libraries provide efficient data manipulation and aggregation, which is crucial for counting entities and preparing CSV files.

# If there are any shortcomings or mistakes, discuss how you would go about tackling them given more resources and time.
- 1.Limited Sentiment Analysis: The rule-based sentiment analysis is limited to the presence of a few keywords ("good," "tasty"). It won't capture complex sentiments or account for negations or context.
 - 2.No Named Entity Recognition Tuning: The entity recognition is based on spaCy's pre-trained model, which might not be tuned to domain-specific entities.
# Potential Improvements:
- 1.Advanced Sentiment Analysis: Implement more advanced sentiment analysis techniques using pre-trained sentiment analysis models, such as BERT, which can capture complex sentiments and context.
- 2.Custom Entity Recognition: Fine-tune a named entity recognition model on domain-specific data to accurately extract relevant entities.
- 3.Error Handling: Implement robust error handling to handle cases where entities are not recognized or sentiment analysis fails.
- 4.	Data Preprocessing: Extend data preprocessing to handle cleaning and tokenization, which are essential for accurate analysis.
- 5.	Data Visualization: Visualize the extracted insights using charts or graphs to provide a clearer understanding of the results.



## Output
![image](https://github.com/Deepthi9kankanala/NLP/assets/85917308/54a63a2a-2aac-4e6b-a5d9-beff840c615c)
![image](https://github.com/Deepthi9kankanala/NLP/assets/85917308/7d5ce272-d41d-443c-bc9c-a2244c879c83)


