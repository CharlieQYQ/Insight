# 本文件用于测试Bag of Words方法计算文本相似度

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def bow_cosine(str1: str, str2: str):
    vectorizer = CountVectorizer()
    vectorizer.fit([str1, str2])
    x = vectorizer.transform([str1, str2])
    return cosine_similarity(x[0], x[1])


s1 = "我是黑社会有人出两万块钱让我打断你一条腿"
s2 = "我是黑社会的，有人出钱让我弄折你一胳膊"

print(bow_cosine(s1, s2))
