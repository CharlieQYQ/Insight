# 本文件用于测试Text2Vec方法计算文本相似度

import time
from text2vec import SBert
from sentence_transformers.util import cos_sim, semantic_search

start = time.time()
embedder = SBert()
corpus = ["我是黑社会有人出两万块钱让我打断你一条腿", "这是一条测试短信，这是一条测试短信，这是一条测试短信。", "您儿子现在我手上、要想活命赶紧打 10 万元钱到我账户，否则就等着收尸吧", "家长您好,请参考以下各地高校招生录取分数线*****"]
querys = ["我是黑社会的，有人出钱让我弄折你一胳膊"]

print(corpus)
print(querys)


corpus_embedding = embedder.encode(corpus)

for query in querys:
    query_embedding = embedder.encode(query)
    hits = semantic_search(query_embedding, corpus_embedding, top_k=3)
    print("Query:", query)
    print("Top 3 most similar sentence in corpus: ")
    hit = hits[0]
    for h in hit:
        print(corpus[h['corpus_id']], "(Simi_Score: {:.4f})".format((h['score'])))

stop = time.time()
print("用时：", stop-start)
