# Public Sentiment Analysis Toward Official COVID-19 Publications Using Natural Language Processing (NLP) Techniques

**Course:** IE7500  
**Group 10**

**Authors**
- Ruthie Orona
- Geovany Silva
- Luce Trinh
- Sabrina Valcin

---

# 1. Project Description

The objective of this project is to analyze public reactions and comments expressed on social media in response to official publications issued by public health organizations, primarily the Centers for Disease Control and Prevention (CDC) and the World Health Organization (WHO), during the COVID-19 pandemic.

The goal is to develop an NLP model capable of understanding public opinion and emotional responses to official health communications, allowing health authorities to better evaluate how different communication strategies influence public behavior.

Specifically, the project will analyze emotions such as:

- Fear
- Trust
- Frustration
- Anger
- Denial
- Acceptance
- Pandemic fatigue
- Institutional distrust

Additionally, the study will compare reactions to different types of official publications, including:

- Vaccines
- Masks
- Lockdowns
- Health recommendations
- Statistical reports

---

# 2. Problem Statement

Pandemics represent one of the greatest challenges faced by public health organizations.

During COVID-19, organizations such as the CDC and WHO continuously published recommendations through digital platforms.

However, public responses varied considerably, ranging from strong support to distrust and rejection.

Understanding these reactions is essential because public perception directly affects:

- Compliance with preventive measures
- Vaccine acceptance
- Public trust in health institutions

This project applies Natural Language Processing techniques to identify emotional patterns and changes in public sentiment over time.

---

# 3. Dataset Selection

Since no existing dataset fully captures public responses to official CDC and WHO publications, a custom dataset will be constructed.

## Data Selection

- Language: English
- Time period: Major COVID-19 milestones
- Source: Official CDC and WHO publications
- Platform: Twitter/X

## Expected Dataset

Approximately **8,000 comments** collected from:

- @CDCgov
- @WHO

Example hashtags:

- #COVID19
- #VaxUp
- #CDCRecommendations

### Dataset attributes

| Variable | Description |
|-----------|-------------|
| Timestamp | Date of publication |
| Raw_Text | Original user comment |

---

# 4. Expected Outcomes

The primary objective is to build a multi-class sentiment classification model capable of detecting changes in public trust.

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## Expected Deliverables

- Sentiment Trend Map
- Feature Importance Analysis
- Comparative evaluation of Word2Vec, GloVe and CBOW embeddings

---

# References

- Centers for Disease Control and Prevention (2026)
- World Health Organization (2023)
- TwitterTrend.co (2024)