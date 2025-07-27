import json

# 수정할 노트북 파일 경로 (현재 디렉토리의 파일이면 파일명만 입력)
notebook_path = '19-04. bert_next_sentence_prediction.ipynb'  # 이 부분을 실제 파일명으로 변경하세요

# 노트북 파일 읽기
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook_content = json.load(f)

# 'widgets' 항목 삭제
if 'metadata' in notebook_content and 'widgets' in notebook_content['metadata']:
    del notebook_content['metadata']['widgets']
    print("'widgets' 항목이 성공적으로 삭제되었습니다.")
else:
    print("'widgets' 항목을 찾을 수 없습니다.")

# 수정된 노트북 저장
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, indent=2)
    
print(f"노트북 {notebook_path}이(가) 수정되었습니다.")