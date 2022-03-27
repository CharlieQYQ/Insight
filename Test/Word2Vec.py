import gensim
import jieba
import numpy as np
from scipy.linalg import norm
import os

model_file = './word2vec/news_12g_baidubaike_20g_novel_90g_embedding_64.bin'
model = gensim.models.KeyedVectors.load_word2vec_format(model_file, binary=True)
print("Model Load")


# 生成停用词
def gen_stop_words() -> list:
    """
    函数名：gen_stop_words
    作用：生成停用词列表
    :return:停用词列表
    """
    with open("./stop_words.txt", "r", encoding='UTF-8') as fp:
        stop_words = [_.strip() for _ in fp.readlines()]
    # 返回停用词列表
    return stop_words


def vector_similarity(s1, s2):
    stop_words = gen_stop_words()

    def sentence_vector(s):
        words = jieba.lcut(s)
        v = np.zeros(64)
        for word in words:
            if word not in stop_words and not word.isspace():
                if model.has_index_for(word):
                    v += model[word]
        v /= len(words)
        return v

    v1, v2 = sentence_vector(s1), sentence_vector(s2)
    return np.dot(v1, v2) / (norm(v1) * norm(v2))


if __name__ == '__main__':
    string = "我是黑社会，有人花钱找我，让我打断你一条腿"
    target = "我是咱这黑社会的，你仇家找我，给我钱让我打断你一条胳膊"

    res = vector_similarity(string, target)
    print(res)
