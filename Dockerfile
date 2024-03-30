FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

RUN pip3 install torch transformers

WORKDIR /app

COPY run_models.py /app/

CMD ["python3", "run_models.py"]