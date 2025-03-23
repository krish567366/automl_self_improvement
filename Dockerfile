# Build stage  
FROM python:3.10-slim as builder  
COPY requirements.txt .  
RUN pip install --user -r requirements.txt  

# Runtime stage  
FROM python:3.10-slim  
COPY --from=builder /root/.local /root/.local  
COPY . /app  
WORKDIR /app  

ENV PATH=/root/.local/bin:$PATH  
CMD ["uvicorn", "src.automl.api.app:app", "--host", "0.0.0.0", "--port", "8000"]  