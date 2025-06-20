# -*- coding: utf-8 -*-
"""RAG 데이터셋 EDA - wikidocs 25-06-20.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k-ma3OJrJuBur4t1nQwdkfA5qPedSSaT
"""

pip install datasets

import numpy as np
import matplotlib.pyplot as plt
from datasets import load_dataset

dataset = load_dataset("iamjoon/klue-mrc-ko-rag-dataset")

df = dataset['train'].to_pandas()
df = df[['question', 'search_result', 'answer', 'extracted_ref_numbers', 'type']]
df.head()

print('데이터 타입 종류:',df['type'].unique())

print('5번 샘플의 타입:', df['type'].loc[5])
print('5번 샘플의 질문:', df['question'].loc[5])

print('5번 샘플의 답변:', df['answer'].loc[5])

print('5번 샘플의 답변에서 인용한 문서 번호:', df['extracted_ref_numbers'].loc[5])

print('5번 샘플의 검색 결과 개수:', len(df['search_result'].loc[5]))

print('5번 샘플의 검색 결과 중 세번째 문서:', df['search_result'].loc[5][2])

df['search_result_len'] = df['search_result'].apply(len)
df['extracted_ref_len'] = df['extracted_ref_numbers'].apply(len)

def plot_lengths_by_type(df, plot_type):
    """
    특정 type의 데이터에 대해 extracted_ref_len과 search_result_len의 분포를 시각화하고 값 출력.

    Parameters:
    df (pd.DataFrame): 데이터프레임
    plot_type (str): 시각화할 데이터의 type 값 (예: 'qa', 'summarize' 등)
    """
    # 유효한 type 값인지 검증
    if plot_type not in df['type'].unique():
        print(f"'{plot_type}'는 유효하지 않은 타입입니다. 데이터프레임에 존재하는 타입을 확인하세요.")
        return

    # 해당 type의 데이터만 필터링하고 전체 개수 계산
    df_type = df[df['type'] == plot_type]
    total_count = len(df_type)

    # 길이별 값 계산
    # extracted_ref_len: 실제 인용된 문서의 개수
    # search_result_len: 검색으로 조회된 문서의 개수
    extracted_counts = df_type['extracted_ref_len'].value_counts().sort_index()
    search_counts = df_type['search_result_len'].value_counts().sort_index()

    # 분석 결과 출력
    # 전체 데이터 수와 각 길이별 분포를 출력
    print(f"타입: {plot_type}")
    print(f"전체 데이터 수: {total_count:,}개")
    print("\n문서 인용 분포:")
    for length, count in extracted_counts.items():
        print(f"{length}개의 문서를 인용한 샘플: {count}개")
    print("\n검색된 문서 분포:")
    for length, count in search_counts.items():
        print(f"검색 문서로 {length}개가 존재하는 경우: {count}개")

    # 시각화를 위한 subplot 생성
    # figsize(5, 2.5): 적당한 크기의 그래프를 위한 설정
    fig, axes = plt.subplots(1, 2, figsize=(5, 2.5))

    # 두 그래프 사이의 간격 설정 (타이틀이나 레이블이 겹치지 않도록)
    plt.subplots_adjust(wspace=0.6)

    # 왼쪽 그래프: 인용된 문서 수 분포
    extracted_counts.plot(
        kind='bar',
        ax=axes[0],
        xlabel='extracted_ref_len',  # 인용된 문서의 개수
        ylabel='Count',             # 해당 개수의 출현 빈도
        grid=True                   # 격자 표시
    )

    # 오른쪽 그래프: 검색된 문서 수 분포
    search_counts.plot(
        kind='bar',
        ax=axes[1],
        xlabel='search_result_len',  # 검색된 문서의 개수
        ylabel='Count',             # 해당 개수의 출현 빈도
        grid=True                   # 격자 표시
    )

    # 그래프의 레이아웃 자동 조정
    plt.tight_layout()
    plt.show()

plot_lengths_by_type(df, 'mrc_question')

plot_lengths_by_type(df, 'mrc_question_with_1_to_4_negative')

print('데이터의 유형:', df['type'].loc[787])
print('질문:', df['question'].loc[787])
print('답변:', df['answer'].loc[787])
print('답변에서 인용한 문서:', df['extracted_ref_numbers'].loc[787])

plot_lengths_by_type(df, 'synthetic_question')

print('데이터의 유형:', df['type'].loc[1285])
print('질문:', df['question'].loc[1285])

plot_lengths_by_type(df, 'paraphrased_question')

print('데이터의 유형:', df['type'].loc[1480])
print('질문:', df['question'].loc[1480])
print('답변:', df['answer'].loc[1480])
print('답변에서 인용한 문서:', df['extracted_ref_numbers'].loc[1480])

plot_lengths_by_type(df, 'no_answer')