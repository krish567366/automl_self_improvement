# API Reference

## Authentication
### `POST /token`
- **Description**: Obtain JWT access token.
- **Request Body**:
  ```json
  {
    "username": "admin",
    "password": "secret"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "eyJhbGci...",
    "token_type": "bearer"
  }
  ```

## Core Endpoints
### `POST /train`
- **Description**: Launch automated training job.
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "dataset_path": "s3://bucket/data",
    "target_metric": "f1_score",
    "constraints": {"max_training_time": 3600}
  }
  ```
- **Response**:
  ```json
  {
    "job_id": "a1b2c3",
    "monitor_url": "/jobs/a1b2c3"
  }
  ```

## Python SDK
```python
from automl_sdk import Client

client = Client(api_key="your-api-key")

# Start training
job = client.train(
    dataset="cifar10",
    objective="accuracy",
    strategy="hybrid"  # BO + RL
)

# Monitor job
print(client.get_status(job.id))
```