from langchain_ollama import OllamaLLM
import config

model_name = config.LLM_MODEL[0]

model = OllamaLLM(model=model_name)

result = model.invoke(input="Hello, how are you?")

print(result)