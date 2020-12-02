FROM python:3

# Port argument
ARG LISTEN_PORT
ENV LISTEN_PORT=${LISTEN_PORT}

# Install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code to image
COPY src\* .

# Run this script when starting container
EXPOSE ${LISTEN_PORT}
CMD ["python", "./main.py"]