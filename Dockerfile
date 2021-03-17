FROM python:3.9-slim

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install -r requirements.txt

# gunicorn with one worker process and 8 threads.
CMD exec gunicorn --bind :8000 --workers 1 --threads 8 --timeout 0 main:app