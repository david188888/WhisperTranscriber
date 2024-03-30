from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
import torch

object_model = "openai/whisper-medium"
save_directory = "./models"
# 加载模型和处理器
processor = AutoProcessor.from_pretrained(object_model)
model = AutoModelForSpeechSeq2Seq.from_pretrained(object_model)



# 将模型和处理器保存到本地文件夹
processor.save_pretrained(save_directory)
model.save_pretrained(save_directory)

print("模型已保存到本地文件夹:", save_directory)


print(type(model))
print("--------------")
print(f"the model is {model.config.decoder_start_token_id}")
print("--------------")
print(f"the input shape of the model is {model.config.encoder_ffn_dim}")




