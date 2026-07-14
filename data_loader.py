import json
import os

# data 폴더의 파일을 읽어오는 함수
def load_json_data(filename):
    file_path = os.path.join("data", filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)