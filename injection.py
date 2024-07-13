# importing all libraries 

# import all important libraries 
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from dotenv import load_dotenv
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
import os
def env_load():
    load_dotenv()
    if load_dotenv()==True:
        openai_api=os.getenv("OPENAI_API_KEY")
        print(f"env is loaded here is the api key {openai_api}")
    else:  
        print("env is not loaded ")

def load_data(path):
    loader = DirectoryLoader(path)
    documents = loader.load()
    if len(documents) != 0:
        print(f"Data is loaded \nThe length of loaded data is {len(documents)}")
    else:
        print("No data loaded.")
    return documents
def load_and_chunk(path):
    # split it into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(load_data(path))
    #creating a database in local run if you wanna create one in your local machine 
    Chroma.from_documents(docs, embeddings, persist_directory="./db")
def load_from_db():
    vectoredb=Chroma(persist_directory="./db", embedding_function=embeddings)
    # docs = vectoredb.similarity_search(query)
    # print(docs[0].page_content)
    return vectoredb
    

    
def main():
    env_load()
# /Users/saeedanwar/Desktop/youtube_video/data
    path=input("enter file path")
    load_and_chunk(path)
    # now we can check if database is created then we can load
    #data from it 
    query="what is fastapi ?"
    load_from_db()

    return  


if __name__ == '__main__':
    main()



