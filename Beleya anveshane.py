# %%
import os

# Create /home/sample_data
os.makedirs("/home/bomma/Lihaan", exist_ok=True)

print("Folder created:", os.path.exists("/home/bomma/Lihaan"))


# %%

import os
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
from threading import Lock

# ---------------------------
# Read secrets ONLY from environment variables
# (GitHub Secrets will provide these)
# ---------------------------
ACCESS_KEY = os.environ["R2_ACCESS_KEY"]
SECRET_KEY = os.environ["R2_SECRET_KEY"]
ACCOUNT_ID = os.environ["R2_ACCOUNT_ID"]
BUCKET = os.environ["R2_BUCKET"]

# Object paths
remote_key = "Desktop/Projects.zip"
local_path = "/home/bomma/Lihaan/Projects.zip"

# Create S3 client (Cloudflare R2)
s3 = boto3.client(
    "s3",
    endpoint_url=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name="auto",
    config=Config(signature_version="s3v4")
)

# ---------------------------
# Progress tracker
# ---------------------------
class ProgressPercentage:
    def __init__(self):
        self.downloaded = 0
        self.lock = Lock()

    def __call__(self, bytes_amount):
        with self.lock:
            self.downloaded += bytes_amount
            print(f"\rDownloaded {self.downloaded} bytes", end="")

# ---------------------------
# Download file
# ---------------------------
try:
    print("Starting download...")
    s3.download_file(
        BUCKET,
        remote_key,
        local_path,
        Callback=ProgressPercentage()
    )
    print("\nDownload completed successfully")

except ClientError as e:
    print("\nDownload failed:", e)

except Exception as e:
    print("\nUnexpected error:", e)


# %%
import zipfile
import os

# Zip file path
zip_path = "/home/bomma/Lihaan/Projects.zip"

# Folder where zip exists
extract_dir = "/home/bomma/Lihaan"

try:
    # Open and extract the zip file
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_dir)

    # Delete the zip file after extraction
    os.remove(zip_path)

    print("Unzip completed and zip file deleted successfully.")

except Exception as e:
    print("Error:", e)


# %%

import os
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
from threading import Lock

# ---------------------------
# Read secrets ONLY from environment variables
# (GitHub Secrets will provide these)
# ---------------------------
ACCESS_KEY = os.environ["R2_ACCESS_KEY"]
SECRET_KEY = os.environ["R2_SECRET_KEY"]
ACCOUNT_ID = os.environ["R2_ACCOUNT_ID"]
BUCKET = os.environ["R2_BUCKET"]

# Object paths
remote_key = "Desktop/Database/Day wise price.db"
local_path = "/home/bomma/Lihaan/Projects/Day wise price Analysis/Day wise price.db"

# Create S3 client (Cloudflare R2)
s3 = boto3.client(
    "s3",
    endpoint_url=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name="auto",
    config=Config(signature_version="s3v4")
)

# ---------------------------
# Progress tracker
# ---------------------------
class ProgressPercentage:
    def __init__(self):
        self.downloaded = 0
        self.lock = Lock()

    def __call__(self, bytes_amount):
        with self.lock:
            self.downloaded += bytes_amount
            print(f"\rDownloaded {self.downloaded} bytes", end="")

# ---------------------------
# Download file
# ---------------------------
try:
    print("Starting download...")
    s3.download_file(
        BUCKET,
        remote_key,
        local_path,
        Callback=ProgressPercentage()
    )
    print("\nDownload completed successfully")

except ClientError as e:
    print("\nDownload failed:", e)

except Exception as e:
    print("\nUnexpected error:", e)


# %%
print("part 2 codes start here")

# %%
import subprocess
import os

# Path to the script
script_path = "/home/bomma/Lihaan/Projects/codes/all.py"

# Get the folder of the script
script_dir = os.path.dirname(script_path)

# Log file path (same folder)
log_path = os.path.join(script_dir, "all.log")

# Open log file and redirect output
with open(log_path, "w") as log_file:
    subprocess.run(
        ["python3", script_path],
        stdout=log_file,   # save normal output
        stderr=log_file,   # save errors
        check=False
    )


# %%
import zipfile
import os

# File path
log_file = "/home/bomma/Lihaan/Projects/codes/all.log"

# Zip file path (same folder)
zip_file = log_file.replace(".log", ".zip")

# Create zip file
with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(log_file, arcname=os.path.basename(log_file))

# Print confirmation
print("Zip file created")


# %%
import shutil
import os

# Folder path to delete
folder_path = "/home/bomma"

# Check if folder exists
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)  # Delete folder and all contents
    print("Folder deleted successfully.")
else:
    print("Folder does not exist.")



