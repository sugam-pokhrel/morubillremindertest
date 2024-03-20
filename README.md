# Your App Name

Welcome to Your App Name! This is a brief guide on how to set up and run the application.

## Prerequisites

- Python 3.x installed on your machine.
- Request module should be of version 2.27.1 as per the requirments.txt file
- Redis installed and running. You can download it from [Redis Downloads](https://redis.io/download).

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/yourapp.git
cd yourapp

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt


# Start Redis (if not already running)
redis-server

# Open three terminals (one for each process):
# Terminal 1: Start Celery Beat for periodic tasks scheduling
celery -A main.celery beat --loglevel=info

# Terminal 2: Start Celery Worker to execute tasks
celery -A main.celery worker --loglevel=info

# Terminal 3: Run the FastAPI application
uvicorn main:app --reload
# morubillremindertest
