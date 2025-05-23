import pandas as pd
import json

# CSV 파일 경로 지정
csv_file_path = "movies_metadata.csv"  # 본인 파일 경로로 변경하세요
json_file_path = "product.json"

# CSV 파일을 DataFrame으로 읽기
df = pd.read_csv(csv_file_path, low_memory=False)

# DataFrame을 JSON 형식으로 변환 (레코드별로 나열된 형태)
json_data = df.to_json(orient='records', lines=True)

# JSON 파일로 저장
with open(json_file_path, 'w', encoding='utf-8') as f:
    f.write(json_data)

print(f"JSON 파일로 저장 완료: {json_file_path}")