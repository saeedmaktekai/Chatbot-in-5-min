from injection import load_from_db
from langchain.chains import create_retrieval_chain
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain_core.prompts import ChatPromptTemplate
vectorstore=load_from_db()
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")


retriever = vectorstore.as_retriever()

#promting
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder

contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)




system_prompt = (
    "You are an assistant for question-answering  "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory



store = {}
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]
conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)
while True:
    # Get user input
    user_input = input("Please enter your question: ")

    # Invoke the conversational_rag_chain function with user input
    result = conversational_rag_chain.invoke(
            {"input": user_input},
            config={
                "configurable": {"session_id": "abc123"}
            }  # constructs a key "abc123" in `store`.
        )
        
    # Print the answer from the result
    print(result["answer"])
        
        # Ask if the user wants to continue
    continue_prompt = input("Do you want to ask another question? (yes/no): ")
    if continue_prompt.lower() != "yes":
        break

# Assuming conversational_rag_chain is already defined and imported

# while True:
#     # Invoke the function\
#     query=input("enter your query : ")
#     result = conversational_rag_chain.invoke(

#         {"input": query},
#         config={
#             "configurable": {"session_id": "abc123"}
#         }  # constructs a key "abc123" in `store`.
#     )
    
#     # Print the answer from the result
#     print(result["answer"])
    
#     # Ask if the user wants to continue
#     continue_prompt = input("Do you want to ask again? (yes/no): ")
#     if continue_prompt.lower() != "yes":
#         break

# while True:
#     query = input("enter your question ")
#     result={"input": query},
#     config={
#         "configurable": {"session_id": "abc123"}
#     },  # constructs a key "abc123" in `store`.
#     print(
#     conversational_rag_chain.invoke(result,
#    ["answer"]))








# retriever=vectoredb.as_retriever()
# retriever = vectoredb.as_retriever(
#     search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.1}
# )

# docs = retriever.invoke("what is fastapi ?")
# # docs= vectoredb.as_retriever()

# from langchain_openai import ChatOpenAI





# chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)


# SYSTEM_TEMPLATE = """
# Answer the user's questions based on the below context. 
# If the context doesn't contain any relevant information to the question, don't make something up and just say "I don't know":

# <context>
# {context}
# </context>
# """

# question_answering_prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             SYSTEM_TEMPLATE,
#         ),
#         MessagesPlaceholder(variable_name="messages"),
#     ]
# )

# document_chain = create_stuff_documents_chain(chat, question_answering_prompt)
#############################################

# while True:
#     # Ask the user for a query
#     query = input("Enter your question (or type 'exit' to quit): ")
    
#     # Check if the user wants to exit
#     if query.lower() == 'exit':
#         print("Exiting the loop. Goodbye!")
#         break
    
#     # Create the dictionary structure dynamically
#     input_data = {
#         "context": docs,
#         "messages": [HumanMessage(content=query)]
#     }
   
#     # Invoke the function with the dynamic input
#     values = document_chain.invoke(input_data)
    
#     # Print or process the returned values as needed
#     print("Response:", values)







