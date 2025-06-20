# -*- coding: utf-8 -*-
"""RAG 이해하기 - wikidocs 25-06-20.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F2-vl9x1fdCnT33PaAamW5vYrRB3RB43
"""

pip install -U langchain-community

import numpy as np
from numpy import dot
from numpy.linalg import norm

def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

vec1 = np.array([0,1,1,1])
vec2 = np.array([1,0,1,1])
vec3 = np.array([2,0,2,2])

print('벡터1과 벡터2의 유사도 :',cos_sim(vec1, vec2))
print('벡터1과 벡터3의 유사도 :',cos_sim(vec1, vec3))
print('벡터2와 벡터3의 유사도 :',cos_sim(vec2, vec3))

import os
import numpy as np
from numpy import dot
from numpy.linalg import norm
import pandas as pd
from langchain.embeddings import OpenAIEmbeddings

os.environ['OPENAI_API_KEY'] = "여러분의 키 값"

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
query_result = embeddings.embed_query('저는 배가 고파요')
print(query_result)

data = ['저는 배가 고파요',
        '저기 배가 지나가네요',
        '굶어서 허기가 지네요',
        '허기 워기라는 게임이 있는데 즐거워',
        '스팀에서 재밌는 거 해야지',
        '스팀에어프라이어로 연어구이 해먹을거야']

df = pd.DataFrame(data, columns=['text'])
df

def get_embedding(text):
  return embeddings.embed_query(text)

df['embedding'] = df.apply(lambda row: get_embedding(
        row.text,
    ), axis=1)
df

def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

def return_answer_candidate(df, query):
    query_embedding = get_embedding(
        query
    )
    df["similarity"] = df.embedding.apply(lambda x: cos_sim(np.array(x),
                                                            np.array(query_embedding)))
    top_three_doc = df.sort_values("similarity",
                                ascending=False).head(3)
    return top_three_doc

sim_result = return_answer_candidate(df, '아무것도 안 먹었더니 꼬르륵 소리가 나네')
sim_result