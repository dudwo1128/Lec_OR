from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
stop_words = set(stopwords.words('english'))
f = open("C:/Users/dudwo/Desktop/Practice_Abstract.csv", 'r',encoding='utf-8')
w = open("C:/Users/dudwo/Desktop/Abstract_lemmas.csv",'a',encoding='utf-8')
lines = f.readlines()
stemmer= PorterStemmer()
lematizer = WordNetLemmatizer()
for line in lines:
    pat_num = line[0:7]
    abstract = line[8:]
    token = word_tokenize(abstract)
    tokens_without_stopwords = [i for i in token if not i in stop_words]
    lemmas = [lematizer.lemmatize(token) for token in tokens_without_stopwords]
    total = [pat_num,lemmas]
    w.writelines(str(total))
    #w.writelines(',')
    #w.writelines(total[1])
    w.writelines('\n')
    #print(total)
w.close()
f.close()