🎯 Goal
Create a simple REST API using Python Flask.

Use a free language model (all-MiniLM-L6-v2) to convert movie descriptions into vectors.

Integrate this API into an ASP.NET Core application for semantic storage and querying.

🧰 1. Set Up Python Environment
✅ Step 1: Install Python
Go to the official website: https://www.python.org/downloads

Download Python version 3.10 or above.

During installation, make sure to check the option “Add Python to PATH”.

🔍 Verify the installation
Open CMD or PowerShell and run:
python --version
Example output: Python 3.10.13

🧱 2. Create a Virtual Environment
mkdir embedding_api
cd embedding_api
python -m venv venv
venv\Scripts\activate  # Windows

📦 3. Install Required Packages
pip install flask sentence-transformers numpy

🚀 4. Run the Flask API
In the directory where app.py is located, run:

python app.py

✅ If successful, you’ll see output like:

Running on http://0.0.0.0:5005

✅ How to fix: running scripts is disabled on this system

🔐 Step 1: Open PowerShell as Administrator

Click Start

Type PowerShell

Right-click → Run as administrator

⚙️ Step 2: Temporarily Allow Script Execution
In the PowerShell window (running as admin), type the following command:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

When prompted with “Do you want to change the execution policy?”, type Y and press Enter.

