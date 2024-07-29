# Personalized Dining Navigator

## Enhancing food app suggestions with dynamic, behavior-based methods using advanced filtering and clustering techniques.

Creating a restaurant discovery system using content-based filtering, collaborative filtering, and hierarchical clustering to adapt to evolving user preferences and locations, addressing limitations of current apps. This approach aims to offer more accurate and relevant dining options tailored to individual tastes and situational contexts.

* Created tags from user reviews to capture key themes and concepts.
* Applied PorterStemmer for stemming to reduce words to their base forms.
* Used Bag of Words (NLP technique) for text vectorization, converting text data into numerical vectors.
* Removed stop words and created tokens with CountVectorizer.
* Extracted the 5,000 most frequent words from all tags combined using CountVectorizer.
* Calculated vector distances using cosine similarity to address limitations of high-dimensional Euclidean distance.





