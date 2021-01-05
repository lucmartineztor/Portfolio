import numpy as np
import classifier as cd
from nltk.sentiment  import SentimentIntensityAnalyzer

x="It was a charming and beatiful day"
y="It was a horrible experience"
z="I have nothing to say. Normal so far"

sid=SentimentIntensityAnalyzer()
resultados=sid.polarity_scores(x)
print (resultados)