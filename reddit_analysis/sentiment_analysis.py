import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
#import torch

# TODO: Need to preprocess text to make this function work
# def getAverageScoreWithBERT(submissions):
#     sumOfScores = 0.0
#     num_scores_analyzed = 0.0
#     for submission in submissions:
#         text = submission.title + submission.selftext
#         sentiment_score = float(getScoreWithBERT(text))
#         num_scores_analyzed = num_scores_analyzed + 1.0
#         sumOfScores = sumOfScores + sentiment_score
#     averageScore = sumOfScores / num_scores_analyzed
#     return averageScore

# TODO: Need to preprocess text to make this function work
# def getScoreWithBERT(text):
#     tokenizer = AutoTokenizer.from_pretrained("vinai/bertweet-base", use_fast=False)
#     model = AutoModelForSequenceClassification.from_pretrained("vinai/bertweet-base", num_labels=2)
#     model.eval()

#     encoded_input = tokenizer(text, padding=True, truncation=True, return_tensors="pt")

#     with torch.no_grad():
#         outputs = model(**encoded_input)
#         logits = outputs.logits
#         predicted_class = torch.argmax(logits, dim=1).item()
#     return predicted_class

# # Download the VADER lexicon
nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

def getAverageScoreWithVADER(submissions):
    sumOfScores = 0.0
    num_scores_analyzed = 0.0
    for submission in submissions:
        text = submission.title + submission.selftext
        sentiment_score = float(getScoreWithVADER(text))
        num_scores_analyzed = num_scores_analyzed + 1.0
        sumOfScores = sumOfScores + sentiment_score
    averageScore = sumOfScores / num_scores_analyzed
    return averageScore

def getScoreWithVADER(text):
   sentiment_score = sid.polarity_scores(text)
   return sentiment_score['compound']

