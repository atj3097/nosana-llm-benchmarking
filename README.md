

![Nosana Logo](img/nosana_logo.png)
## Nosana Model Benchmarking


### What is Nosana?

Nosana is a decentralized computing network designed to offer cloud services at a fraction of the cost, leveraging the Solana blockchain for secure, fast, and scalable computing resources. It enables developers to run CI/CD pipelines, perform compute-intensive tasks, and more, all within a decentralized ecosystem.


### Purpose of This Project

This project aims to benchmark various AI models using the Nosana network, providing insights into performance, efficiency, and scalability. By leveraging a Docker container environment, we ensure consistency, reproducibility, and ease of deployment across the decentralized nodes of the Nosana network.


### Models Benchmarked
| Model Name | Description |
|------------|-------------|
| mistralai/Mistral-7B-Instruct-v0.2 | Mistral: |
| Qwen/Qwen1.5-72B-Chat | Qwen 1.5: |
| meta-llama/Llama-2-7b | Llama 2: |
| databricks/dbrx-instruct | DBRX: |
| 01-ai/Yi-34B-200K | Yi: |
| xai-org/grok-1 | Grok: |



### Docker Container

The Docker container is built on an Ubuntu 22.04 base image with CUDA support, ensuring compatibility with GPU-accelerated tasks for AI model benchmarking. The container includes Python 3, pip, PyTorch, and the Hugging Face Transformers library, which are essential for running the models.# nosana-llm-benchmarking
