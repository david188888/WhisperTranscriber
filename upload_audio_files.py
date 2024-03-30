import os
import requests
import json

# 设置文件夹路径和API端点
folder_path = './data'
api_endpoint = 'http://localhost:8010/transcribe/'


transcriptions = {}
# 遍历文件夹中的每个文件
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # 确保是文件而不是文件夹
    if os.path.isfile(file_path):
        print(f'Uploading {filename}...')
        
        # 打开文件并上传
        with open(file_path, 'rb') as f:
            files = {'file': (filename, f)}
            response = requests.post(api_endpoint, files=files)
            
            # 打印响应（可选）
            result = response.json()
            transcriptions[filename] = result.get('转录', 'No transcription available')

pretty_json_output = json.dumps(transcriptions, ensure_ascii=False, indent=4)
# print(pretty_json_output)

with open('transcriptions.json', 'w', encoding='utf-8') as f:
    f.write(pretty_json_output)


