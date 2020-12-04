FROM python:3

# Install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code to image
COPY src\* .

# Set the image to not run with root
RUN useradd morse -u 8000
USER morse

# Run this script when starting container
CMD ["python", "./main.py"]