
import pandas as pd
import string
from nltk.corpus import stopwords
import nltk
from time import time

nltk.download("stopwords")

df = pd.read_csv("twitter_training.csv",header=None )# encoding="utf-8")
df=df.head(100)
print(df.head(10))


df.columns =['Number','Name', 'Label', 'Tweets']
print(df['Label'].unique())
df.drop(columns=df.columns[(df == 'Irrelevant').any()])

df['Label']=df['Label'].apply(lambda x: 1 if x=='Positive'  else (-1 if x=='Negative' else 0))
stop=stopwords.words ("english")
def remove_stopwords(Text):
	
	TText=[word.lower() for word in Text.split() if word.lower() not in stop]
	return " ".join(TText)

print(df["Tweets"][1],df["Tweets"][2])

def process_text(text):
    Punctuation=''.join([char for char in text if char not in string.punctuation])
    Punctuation=nltk.tokenize.word_tokenize(Punctuation)
    clean_words=[word for word in Punctuation if word.lower() not in stopwords.words('english')]
    return clean_words
for i in range(len(df['Tweets'])):
	try:
		df["Tweets"][i]=remove_stopwords(df["Tweets"][i])
	except:
		continue
try:
	df["Tweets"]=df["Tweets"].apply(process_text)
except:
	pass
print(df.head(10))
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(df.Tweets,df.Label, test_size=0.15)

from sklearn.feature_extraction.text import CountVectorizer
v=CountVectorizer(analyzer=process_text)
X_trainCount=v.fit_transform(X_train.values.astype('U'))
X_testCount=v.transform(X_test.values.astype('U'))


from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(X_trainCount,y_train)

tweet= input("Texto: ")
TweetsCount=v.transform([tweet])
model.predict(TweetsCount)
print('negative') if model.predict(TweetsCount) == -1 else (print('neutral') if model.predict(TweetsCount) == 0 else(print ('positive')))

tweet= input("Texto: ")
TweetsCount=v.transform([tweet])
model.predict(TweetsCount)
print('negative') if model.predict(TweetsCount) == -1 else (print('neutral') if model.predict(TweetsCount) == 0 else(print ('positive')))