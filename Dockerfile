FROM python:3.11

WORKDIR /train

# Salin seluruh folder train ke image
COPY train/ /train/

# Install wget dan curl (tanpa menggunakan requirements.txt)
RUN apt-get update \
 && apt-get install -y --no-install-recommends wget curl \
 && rm -rf /var/lib/apt/lists/*

# Jalankan task.py
ENTRYPOINT ["python", "task.py"]
