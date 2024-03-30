from fastapi import FastAPI, File, UploadFile
import soundfile as sf
import io
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor
import librosa





app = FastAPI()



device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
save_directory = "./models"
processor = AutoProcessor.from_pretrained(save_directory)
model = AutoModelForSpeechSeq2Seq.from_pretrained(save_directory)
model.to(device)
forced_decoder_ids = processor.get_decoder_prompt_ids(language="zh", task="transcribe")



@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File()):
    contents = await file.read()
    waveform, sample_rate = librosa.load(io.BytesIO(contents), sr=16000)
    
    # 将音频数据预处理并且传入模型
    
    input_features = processor(waveform, sampling_rate=sample_rate, return_tensors="pt").input_features.to(device)
    predicted_ids = model.generate(input_features,forced_decoder_ids=forced_decoder_ids)
     
    #解码模型输出
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens= True)
    
    return {"转录": transcription} 

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host = '127.0.0.1', port=8010)    