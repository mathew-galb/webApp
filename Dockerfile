# Use an official lightweight Python image
FROM python:3.12-slim  

# Set the working directory
WORKDIR /app  

# Copy project files into the container
COPY . /app  


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt  
 

# Command to run the app
CMD ["python", "app/main.py"]

