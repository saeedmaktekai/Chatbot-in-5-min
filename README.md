
---

# Chatbot-in-5-min

Welcome to the Chatbot-in-5-min project! This project aims to help you create a chatbot within just 5 minutes by cloning the repository and following a few simple steps. In no time, you'll have a fully functional chatbot up and running.

## Files Overview

1. **`main.py`** - This is the main chain of the project.
2. **`injection.py`** - Running this script helps you create a ChromaDB, which is a vector database.

## Installation

### Step 1: Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/saeedmaktekai/Chatbot-in-5-min.git
cd Chatbot-in-5-min
```

### Step 2: Create an `.env` File

Create a `.env` file in the root directory of the project and add your OpenAI API key:

```bash
echo "OPENAI_API_KEY=your_openai_api_key" > .env
```

### Step 3: Create and Activate a Virtual Environment

#### For Windows:

```bash
python -m venv myenv
myenv\Scripts\activate
```

#### For MacOS and Linux:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Step 4: Install Dependencies

Ensure you have Python 3.8+ installed. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

Next, create a directory for your project:

```bash
mkdir my_new_directory
```

Ensure to review and install all dependencies as mentioned in the `requirements.txt` file.

## Usage

### Running the Application

1. First, run the `injection.py` file and provide the directory path where your data is stored. This data will be used to create the chatbot. Enter your directory path after running it in the terminal:

    ```bash
    python injection.py
    ```

2. Then, run the `chain.py` script to create your chatbot:

    ```bash
    python chain.py
    ```

For more details and support, visit [MakTek](https://www.maktekai.com).

