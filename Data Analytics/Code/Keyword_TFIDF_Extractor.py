from sklearn.feature_extraction.text import  TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
f = open("C:/Users/dudwo/Desktop/키워드추출/Practice_Abstract.csv", 'r',encoding='utf-8')
lines = f.read()

tf = CountVectorizer()

TF = tf.fit_transform(abstract)
tfidf = TfidfTransformer()
TFIDF = tfidf.fit_transform(TF)


df = pd.DataFrame(TFIDF.toarray().T) # TFIDF 점수 추출
df.to_csv("C:/Users/dudwo/Desktop/키워드추출/TFIDF.csv",encoding='utf-8')
df2 = pd.DataFrame(tf.get_feature_names()) # 키워드 추출
df2.to_csv("C:/Users/dudwo/Desktop/키워드추출/keyword.csv",encoding='utf-8')


f.close()