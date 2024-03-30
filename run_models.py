import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

models = [
    "mistralai/Mistral-7B-Instruct-v0.2",  # Mistral
    "Qwen/Qwen1.5-72B-Chat",  # Qwen 1.5
    "meta-llama/Llama-2-7b",  # Llama 2
    "databricks/dbrx-instruct",  # DBRX
    "01-ai/Yi-34B-200K",  # Yi
    "xai-org/grok-1",  # Grok
]

prompts = [
    "What is the capital of France?",
    "Explain the concept of artificial intelligence in simple terms.",
    "Write a short story about a robot who dreams of becoming human.",
    "What are the benefits of regular exercise?",
    "How can we reduce our carbon footprint to combat climate change?",
]

for model_name in models:
    print(f"Running model: {model_name}")
    print("---")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    for prompt in prompts:
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        output = model.generate(input_ids, max_length=100)
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        print(f"Prompt: {prompt}")
        print(f"Generated text: {generated_text}")
        print("---")

    print("\n")