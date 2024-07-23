import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection
from pandas import DataFrame

url = "https://docs.google.com/spreadsheets/d/1LMzSaBylCm8f0iO_h_Pv3_0e-iDQIbYJh1UfwDmD_6A/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)






def main_page():
    st.title("Welcome back " )
    st.write("")
    st.write("")
    st.title("Your Grades")
    
   
    tab1, tab2,tab3,tab4,tab5 = st.tabs(["News","Math", "English"," History","Science"])
    tab1.title("News")
    tab2.title("Math")
    tab3.title("English")
    tab4.title("History")
    tab5.title("Science")

    with tab1:
        st.header("New Assignments")
        st.write("Math: Pop quiz")
        st.write("English: Read & Write")
        st.write("History: Tea Tax")

        st.header("Recently Graded Assignmenst")
        st.write("Math: Basic trig formulas")
        st.write("English: Indapendent Reading")
        st.write("History: Bostan Tea party")
        st.write("Science: Periodic Table")

   
    with tab2:
        st.header("C-")
       
        data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="1567253166",ttl=5,), range(20))
        data2 = conn.read(spreadsheet=url,worksheet="0",ttl=5,)
        st.dataframe(data2,column_config={},hide_index=True)
        st.line_chart(data1)


     
       
       
    
    with tab3:
        st.header("B-")
        
        data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="1613883537",ttl=5,), range(20))
        data2 = conn.read(spreadsheet=url,worksheet="567677192",ttl=5,)
        st.dataframe(data2,column_config={},hide_index=True)
        st.line_chart(data1)
       
    
    with tab4:
        st.header("B+")

        data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="1676935456",ttl=5,), range(20))
        data2 = conn.read(spreadsheet=url,worksheet="1338869921",ttl=5,)
        st.dataframe(data2,column_config={},hide_index=True)
        st.line_chart(data1)
    
    
    with tab5:
        st.header("F")

        data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="420251096",ttl=5,), range(20))
        data2 = conn.read(spreadsheet=url,worksheet="935720519",ttl=5,)
        st.dataframe(data2,column_config={},hide_index=True)
        st.line_chart(data1)
       
     
     
   
    st.sidebar.markdown("DashBoard")

def page2():
    st.title("Classes ")
   
    tab1, tab2, = st.tabs(["S1", "S2",])
    tab1.title("S1 Classes")
    tab2.title("S2 Classes")

    with tab1:

        data2 = conn.read(spreadsheet=url,worksheet="777992936",ttl=5,)
        st.dataframe(data2,column_config={},hide_index=True)
        


    with tab2:
        
        data2 = conn.read(spreadsheet=url,worksheet="448084952",ttl=5,)
        st.dataframe(data2,column_config={},hide_index=True)

    

    
  
    st.sidebar.markdown("Classes")

    

def page3():
 import http
 from imaplib import _Authenticator
 from xml import dom
 import dotenv
 from pathlib import Path
 import streamlit_authenticator as stauth
 from dotenv import load_dotenv
 import os
 import streamlit as st
 import google.generativeai as genai
 import numpy as np
 import pandas as pd
 import random 


 #------PAGE--------

 
 
 


 #--------SECRETS--------------

 import streamlit as st
 import streamlit_authenticator as stauth
 import yaml
 from yaml.loader import SafeLoader
 import os

 # Define your config here
 

 #----------------CHATBOT----------------

 env_path = r"/Users/ed_chat_bot/chatbot_project/.env"

 load_dotenv(env_path)
 API_KEY = os.getenv('API_KEY')
 print (API_KEY)

 genai.configure(api_key=API_KEY)
 model = genai.GenerativeModel('gemini-pro')
 def generate_content(prompt):
        response = model.generate_content(prompt)
        return response.text

 st.title('Gemini AI Text Generator')
 prompt = st.text_input('Enter a prompt:')
 if st.button('Generate'):
        response = generate_content(prompt)
        st.write (response)
  






page_names_to_funcs = {
    "DashBoard": main_page,
     "Schedule": page2,
     "AI Chat Bot": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
