

# Chatbot-in-5-min
this project is going to help us in make a chatbot within 5 min by cloing the repo 
by following the step you would be able to make a chatbot in one 5 min 

2. `injection.py` -by runing this script its going to help you to make make a chromadb which is vectore 
1. `main.py` - this is the main chain 

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
echo "OPENAI_API_KEY=SK-23423523N3LKTHIO3UTO2I3U45P23UEFFLKAJBDF" > .env
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





Ensure to review and install all dependencies as mentioned in the `requirements.txt` file.

## Usage


### Injection Middleware

The `injection.py` after runing this script it will allow you to create chromadb

```python
from injection import InjectionMiddleware

# Initialize your application
app = YourApplication()
app.add_middleware(InjectionMiddleware)

def dependency():
    return {"dependency": "injected"}

@app.route("/example")
def example(dep=dependency()):
    return {"message": "This is an example endpoint with dependency injection.", "dependency": dep}
```


### Chain 

The `chain.py` is the chain of conversation with llm 
```python
from chain import ChainMiddleware

# Initialize your application
app = YourApplication()
app.add_middleware(ChainMiddleware)

@app.route("/example")
def example():
    return {"message": "This is an example endpoint with chained requests."}
```

## Running the Application

first run the injection.py file and give it your Directory path where the data is on which you want to create a chatbot 
```
injecion.py
```
then run chain.py which will allow you to create chatbot 

```
injecion.py

```
