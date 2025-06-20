# -*- coding: utf-8 -*-
"""ChatOpenAI and Memory.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BYtIBXJxjFL52YBlw4u17XlhNLXUTr96
"""

pip install langchain_community langchain_openai

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.tracers.stdout import ConsoleCallbackHandler

os.environ['OPENAI_API_KEY'] = "여러분의 키 값"

# 객체 생성
llm = ChatOpenAI(
    temperature=0.1,  # 창의성 (0.0 ~ 2.0)
    max_tokens=2048,  # 최대 토큰수
    model_name="gpt-4o",  # 모델명
)

# 질의내용
question = "세종대왕이 누구인지 설명해주세요"
# 질의
result = llm.invoke(question)
print(result.content)

# 질문 템플릿 형식 정의
template = "{who}가 누구인지 설명해주세요"

# 템플릿 완성
prompt = PromptTemplate(
        template=template, input_variables=['who']
    )
print(prompt)

print(prompt.format(who="오바마"))

# 연결된 체인 생성
llm_chain = prompt | llm
result = llm_chain.invoke({"who":"이순신 장군"})
print(result.content)

result = llm_chain.invoke({"who":"이순신 장군"},
                          config={"callbacks": [ConsoleCallbackHandler()]})

# 프롬프트 템플릿 생성
template = """아래는 사람과 AI의 친근한 대화입니다. AI의 이름은 위키독스봇입니다. 대화 문맥을 바탕으로 친절한 답변을 진행하세요.

Current Conversation:
{history}

Human: {input}
AI:"""

prompt = PromptTemplate(
        template=template, input_variables=['history', 'input']
    )

# llm 객체를 새로 선언하고, 프롬프트 템플릿과 llm 객체를 연결합니다.
llm = ChatOpenAI(model_name="gpt-4o")
chain = prompt | llm

store = {}
session_id = "test"

if session_id not in store:
    store[session_id] = ChatMessageHistory()
session_history = store[session_id]

with_message_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: session_history,
    input_messages_key="input",
    history_messages_key="history"
)

result = with_message_history.invoke(
    {"input": "당신은 어디에서 만들었습니까?"},
    config={"configurable": {"session_id": "test"}},
)
print(result.content)

result = with_message_history.invoke(
    {"input": "푸른 바다를 주제로 감성적이고 짧은 시를 하나 지어주세요"},
    config={"configurable": {"session_id": "test"}},
)
print(result.content)

result = with_message_history.invoke(
    {"input": "석양을 주제로도 해줘"},
    config={"configurable": {"session_id": "test"}},
)
print(result.content)

print(store)