import streamlit
import streamlit as st
import nltk
import transformers
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#downloads 
nltk.download('punkt')
nltk.download('stopword')



chatbot = pipeline("text-generation",model ="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would to like to schedule appointment with the Doctor."
    elif "medication " in user_input:
        return "It's important to take prescribed medicines regulary. if you have concerns,consult your doctor."
    else:
        response = chatbot(user_input,max_length=500,num_return_sequences=1)
        return response[0]['generated_text']
    

def main():
    st.title("HealthCare Assistant ChatBot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User:",user_input)
            with st.spinner("Processing your query,Please wait...."):
                response=healthcare_chatbot(user_input)
            st.write("Healthcare Assitant :",response)
            print(response)
        else:
             st.write("Please enter a message to get a response.")
        
    
    
    
main()

