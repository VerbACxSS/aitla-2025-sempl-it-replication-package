import os
from typing import List, Tuple
from dotenv import load_dotenv

from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest
from huggingface_hub import snapshot_download

load_dotenv()

class Simplifier:
  
    def __init__(self, model):
        self.llm = LLM(model="unsloth/Qwen2.5-7B-Instruct-bnb-4bit",
                       load_format="bitsandbytes",
                       quantization='bitsandbytes',
                       dtype="half",
                       task="generate",
                       enable_lora=True,
                       max_lora_rank=64,
                       gpu_memory_utilization=0.95,
                       max_model_len=6144,
                       enforce_eager=True)
        self.lora_request = LoRARequest("adapter", 1, lora_path=snapshot_download(repo_id=model))
        self.sampling_params = SamplingParams(temperature=0.1, top_p=0.2, max_tokens=3072, stop=["<|im_end|>"])

    def preprocess_user_message(self, message: str) -> str:
        return message
    
    def postprocess_output(self, output: str) -> str:
        output = output.replace('**', '')
        return '\n'.join([x.rstrip() for x in output.split('\n')])

    def build_messages(self, prompt: str, text_to_simplify: str):
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": self.preprocess_user_message(text_to_simplify)}
        ]
        return messages
    
    def simplify(self, prompt: str, text_to_simplify: str) -> str:
        conversation = self.build_messages(prompt, text_to_simplify)
        response = self.llm.chat(messages=conversation, sampling_params=self.sampling_params, lora_request=self.lora_request)
        return self.postprocess_output(response[0].outputs[0].text)
   

class ConnectivesSimplifier(Simplifier):
    def __init__(self, connectives, model):
        super().__init__(model)
        self.connectives = connectives
    
    def preprocess_user_message(self, message: str) -> str:
        connectives = [x for x in self.connectives if x in message.lower()]
        output = "## Testo\n" + message + "\n\n## Connettivi\n"
        if len(connectives) == 0:
            output += "[Nessuno]"
        else:
            for c in connectives:
                output += f"- {c}\n"
        return output
    