# Culinary Compass

## Enhancing food app suggestions with dynamic, behavior-based methods using advanced filtering and clustering techniques.

Creating a restaurant discovery system using content-based filtering, collaborative filtering, and hierarchical clustering to adapt to evolving user preferences and locations, addressing limitations of current apps. This approach aims to offer more accurate and relevant dining options tailored to individual tastes and situational contexts.

Dataset - https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants

# Architecture

![Architecture](https://github.com/Pranav-Bidve/personalized-dining-navigator/blob/main/img/arch.png)

* Users provide feedback on the Zomato website, including ratings, liked cuisines, suggested improvements, and location.
* Feedback from all users is compiled into a dataset.
* The dataset is used to train a machine learning model.
* The trained model employs collaborative filtering to make recommendations for new users based on similar user preferences.

# Model Description
  
* Created tags from user reviews to capture key themes and concepts.
* Applied PorterStemmer for stemming to reduce words to their base forms.
* Used Bag of Words (NLP technique) for text vectorization, converting text data into numerical vectors.
* Removed stop words and created tokens with CountVectorizer.
* Extracted the 5,000 most frequent words from all tags combined using CountVectorizer.
* Calculated vector distances using cosine similarity to address limitations of high-dimensional Euclidean distance.

# Demonstration

![Hi](https://github.com/Pranav-Bidve/culinary-compass/blob/main/img/welcome_page.png)
![Hi](https://github.com/Pranav-Bidve/culinary-compass/blob/main/img/scroll.png)
![Hi](https://github.com/Pranav-Bidve/culinary-compass/blob/main/img/choice.png)
![Hi](https://github.com/Pranav-Bidve/culinary-compass/blob/main/img/recomm_1.png)
![Hi](https://github.com/Pranav-Bidve/culinary-compass/blob/main/img/recomm_2.png)
![Hi](https://github.com/Pranav-Bidve/culinary-compass/blob/main/img/recomm_3.png)


  





