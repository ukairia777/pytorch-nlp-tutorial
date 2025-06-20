# -*- coding: utf-8 -*-
"""랭체인의 두 가지 청킹 방법 wikidocs - 25-06-20.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ONgctUjVzYs32V3n5mkfBghkB6PySheN
"""

pip install langchain_openai langchain_experimental

import urllib.request
from langchain.text_splitter import RecursiveCharacterTextSplitter

urllib.request.urlretrieve("https://raw.githubusercontent.com/lovit/soynlp/master/tutorials/2016-10-20.txt", filename="2016-10-20.txt")

with open("2016-10-20.txt", encoding="utf-8") as f:
    file = f.read()
print('텍스트의 길이:', len(file))

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)

texts = text_splitter.create_documents([file])
print('분할된 청크의 수:', len(texts))

texts[1]

texts[1].page_content

texts[2].page_content

print('1번 청크의 길이:', len(texts[1].page_content))
print('2번 청크의 길이:', len(texts[2].page_content))

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.create_documents([file])
print('분할된 청크의 수:', len(texts))

texts[1].page_content

texts[2].page_content

import os
import urllib.request
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

os.environ['OPENAI_API_KEY'] =  "여러분의 키 값"

urllib.request.urlretrieve("https://raw.githubusercontent.com/chatgpt-kr/openai-api-tutorial/main/ch06/test.txt", filename="test.txt")

with open("test.txt", encoding="utf-8") as f:
    file = f.read()
print('텍스트의 길이:', len(file))

text_splitter = SemanticChunker(OpenAIEmbeddings())
texts = text_splitter.create_documents([file])
print('분할된 청크의 수:', len(texts))

text_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=95,
)
texts = text_splitter.create_documents([file])
print('분할된 청크의 수:', len(texts))

text_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3,
)
texts = text_splitter.create_documents([file])
print('분할된 청크의 수:', len(texts))

text_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="interquartile",
    breakpoint_threshold_amount=1.5
)
texts = text_splitter.create_documents([file])
print('분할된 청크의 수:', len(texts))