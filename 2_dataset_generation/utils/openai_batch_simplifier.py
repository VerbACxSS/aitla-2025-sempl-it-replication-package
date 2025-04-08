import re
from typing import List, Tuple


class BatchSimplifier:
    GPT_4O = "gpt-4o-2024-11-20"
    GPT_4O_MINI = "gpt-4o-mini-2024-07-18"

    def __init__(self, model):
        self.model = model
    
    def preprocess_user_message(self, message: str) -> str:
        return message
    
    def build_messages(self, prompt: str, few_shots: List[Tuple[str, str]], text_to_simplify: str):
        messages = [{"role": "system", "content": prompt}]
        for _input, _output in few_shots:
            messages.append({"role": "user", "content": self.preprocess_user_message(_input)})
            messages.append({"role": "assistant", "content": _output})    
        messages.append({"role": "user", "content": self.preprocess_user_message(text_to_simplify)})
        return messages

    def generate_request(self, custom_id: str, prompt: str, few_shots: List[Tuple[str, str]], text_to_simplify: str):
        return {
            "custom_id": f"{custom_id}", 
            "method": "POST", 
            "url": "/v1/chat/completions", 
            "body": {
                "model": self.model, 
                "messages": self.build_messages(prompt, few_shots, text_to_simplify),
                "temperature": 0.1,
                "top_p": 0.2,
                "max_tokens": 4095,
                "frequency_penalty": 0.0,
                "presence_penalty": 0.0
            }
        }
    
    @staticmethod
    def parse_response(response) -> Tuple[str, str]:
        custom_id = response["custom_id"]
        output = BatchSimplifier.postprocess_output(response['response']['body']['choices'][0]['message']['content'])
        return custom_id, output
    
    @staticmethod
    def postprocess_output(output: str) -> str:
        output = output.replace('**', '')
        return '\n'.join([x.rstrip() for x in output.split('\n')])


class ConnectivesBatchSimplifier(BatchSimplifier):
    def __init__(self, connectives, model):
        super().__init__(model)
        self.connectives = connectives
    
    def preprocess_user_message(self, message: str) -> str:
        connectives_found = []
        for conn in self.connectives:
            results = [m.group() for m in re.finditer(conn, message, re.IGNORECASE)]
            connectives_found.extend(results)
        
        output = "## Testo\n" + message + "\n\n## Connettivi\n"
        if len(connectives_found) == 0:
            output += "[Nessuno]"
        else:
            for c in connectives_found:
                output += f"- {c}\n"
        return output