import pandas as pd
from sentiment_analysis import getScoreWithVADER
import matplotlib.pyplot as plt

def createScatterPlot(df):
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=df.index, y=df['Score'], marker='o', color='blue', s=50)
    ax.set_xlabel('Submission #')
    ax.set_ylabel('Score')
    ax.set_title('Submission Scores')
    return fig


def createDataFrame(submissions):
     i = 1
     dict = {'Submission text': [], 'Score': []}
     index = []
     for submission in submissions:
        dict['Submission text'].append(submission.title);
        dict['Score'].append(getScoreWithVADER(submission.title))
        index.append(i)
        i+=1
     df = pd.DataFrame(dict, index=index)
     return df




