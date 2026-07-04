# COVID-19 CDC Twitter Stance Detection

## Objective

The objective of this project is to analyze how users responded to official CDC communications during the COVID-19 pandemic by classifying replies according to their stance toward the CDC. Rather than determining whether a tweet is about COVID-19 or measuring its overall sentiment, the goal is to identify whether users express supportive, neutral, or critical positions in response to official public health messaging.

## Methodology

### Model Selection

A review of recent NLP literature was conducted to identify an appropriate modeling approach for stance detection on Twitter. Prior research consistently shows that transformer-based models outperform traditional machine learning methods and earlier deep learning architectures on social media classification tasks. Because Twitter language is highly informal and COVID-19 introduced domain-specific terminology, **COVID-Twitter-BERT (CT-BERT)** was selected as the primary transformer model.

### Data Collection

Official CDC posts were collected using Twitter/X focused searches covering three major phases of the pandemic:

* **2020:** Initial outbreak and lockdowns
* **2021:** Vaccine rollout
* **2022:** Transition toward endemic management

For each period, searches targeted key public health topics (e.g., COVID, masks, vaccines, boosters, and Omicron) while restricting results to posts from the official CDC account (`@CDCgov`). Replies to the selected CDC posts were then collected using the **data-slayer/twitter-comments** actor on Spiffy.

### Data Annotation

To create labeled data for supervised learning, approximately 20% of the collected replies were randomly selected using `scikit-learn` and manually annotated. Each reply is assigned one of three stance labels:

* **Supportive**
* **Neutral**
* **Critical**

The remaining unlabeled replies will be used for model inference after training.

## Models

### CT-BERT

The primary model is **COVID-Twitter-BERT (CT-BERT)**, a transformer model pretrained on approximately 160 million COVID-19-related tweets. Its domain-specific pretraining enables it to better capture COVID-related terminology and Twitter-specific language patterns than general-purpose language models.

### TF-IDF + Logistic Regression

As a classical machine learning baseline, tweets will also be represented using **Term Frequency–Inverse Document Frequency (TF-IDF)** features and classified with **Logistic Regression**. This baseline provides a computationally efficient point of comparison against the transformer-based approach and helps quantify the performance gains achieved by CT-BERT.
