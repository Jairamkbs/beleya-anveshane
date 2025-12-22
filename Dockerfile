# 1️⃣ Use small Python base image
FROM python:3.12-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy requirements first (for faster build)
COPY requirements.txt .

# 4️⃣ Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy your Python file
COPY "Beleya anveshane.py" app.py

# 6️⃣ Command to run your script
CMD ["python", "app.py"]
