# 本文件用于测试Word2Vec方法计算文本相似度
# 导入库
import gensim
import gensim.downloader as api
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
import jieba


# 生成停用词
def gen_stop_words() -> list:
    """
    函数名：gen_stop_words
    作用：生成停用词列表
    :return:停用词列表
    """
    with open(os.path.join("stop_words.txt"), "r", encoding='UTF-8') as fp:
        stop_words = [_.strip() for _ in fp.readlines()]
    # 返回停用词列表
    return stop_words


# 分词函数
def text_seg(text: str, stop_words: list = None) -> list:
    """
    函数名：text_seg
    作用：对输入的字符串进行分词处理
    :param text: 带分词字符串
    :param stop_words: 停用词列表
    :return: 分词结果列表
    """
    # 分词结果
    seg_list = []
    if not stop_words:
        stop_words = gen_stop_words()
    # 分词处理
    for each in jieba.cut(text):
        if each not in stop_words and not each.isspace():
            seg_list.append(each.lower())
    # 返回分词结果列表
    return seg_list


# 加载模型
model = api.load("glove-twitter-200")


def word_avg(model, words):
    return np.mean([model.get_vector(word) for word in words], axis=0)


s1 = "我是黑社会有人出两万块钱让我打断你一条腿"
s2 = "我是黑社会的，有人出钱让我弄折你一胳膊"
s1 = word_avg(model, text_seg(s1))    # 中文需要分词
s2 = word_avg(model, text_seg(s2))
print(cosine_similarity(s1.reshape(1, -1), s2.reshape(1, -1)))     # 用2维数组表示行向量

