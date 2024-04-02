import requests
import json


api_url = 'http://whisper.kirisame.cc:8010/transcribe'


with open('./data/55114876.wav','rb') as f:
    audio = {'file': f}
    response = requests.post(api_url, files=audio)
    
    result = json.loads(response.text)
    print(result)
    print(response.status_code)
    print('-------------')

    
    if response.status_code == 200:
        print('Transcription:', result['转录'])
    else:
        print('Error:', result)
        
# Output:
