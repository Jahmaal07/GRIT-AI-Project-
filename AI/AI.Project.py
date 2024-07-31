import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection
from pandas import DataFrame

# The google sheet connection 
url = "https://docs.google.com/spreadsheets/d/1LMzSaBylCm8f0iO_h_Pv3_0e-iDQIbYJh1UfwDmD_6A/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)

# Sidebar Logo 
logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Infosys_logo.svg/2560px-Infosys_logo.svg.png"
st.sidebar.image(logo_url, use_column_width=True)


# The Main Page ( News & Classes)
def main_page():
    st.title("Welcome back " )
    st.write("")
    st.write("")
    st.title("Your Grades")
    
   # Making the tabs 
    tab1, tab2,tab3,tab4,tab5 = st.tabs(["News","Math", "English"," History","Science"])
    
    # The title of the Tabs
    tab1.title("News")
    tab2.title("Math")
    tab3.title("English")
    tab4.title("History")
    tab5.title("Science")

    # News Tab 
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

   # Math Tab
    with tab2:
        st.header("C-")
       
       # The code for taking the Google sheet info (ttl = time lag between the google sheet and the app)
       #  worksheet=( Page number from the google sheet)
        data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="1567253166",ttl=5,), range(20))
        data2 = conn.read(spreadsheet=url,worksheet="0",ttl=5,)
        data3= pd.DataFrame(conn.read(spreadsheet=url,worksheet="595065738",ttl=5,))
        
        st.dataframe(data2,hide_index=True)
        st.line_chart(data1)
        st.subheader(" Unit Proficiency")
        st.bar_chart(data3, y_label="Units", x_label="Percentage", horizontal=True )

    # English Tab
    with tab3:
        st.header("B-")
        
        # The code for taking the Google sheet info (ttl = time lag between the google sheet and the app)
       #  worksheet=( Page number from the google sheet)
        data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="1613883537",ttl=5,), range(20))
        data2 = conn.read(spreadsheet=url,worksheet="567677192",ttl=5,)
        data3= pd.DataFrame(conn.read(spreadsheet=url,worksheet="213868417",ttl=5,))
        
        st.dataframe(data2,hide_index=True)
        st.line_chart(data1)
        st.subheader(" Unit Proficiency")
        st.bar_chart(data3, y_label="Units", x_label="Percentage", horizontal=True )
       
       
    # History Tab
    with tab4:
        st.header("B+")

        # The code for taking the Google sheet info (ttl = time lag between the google sheet and the app)
       #  worksheet=( Page number from the google sheet)
        data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="1676935456",ttl=5,), range(20))
        data2 = conn.read(spreadsheet=url,worksheet="1338869921",ttl=5,)
        data3= pd.DataFrame(conn.read(spreadsheet=url,worksheet="1207730077",ttl=5,))
       
        st.dataframe(data2,hide_index=True)
        st.line_chart(data1)
        st.subheader(" Unit Proficiency")
        st.bar_chart(data3, y_label="Units", x_label="Percentage", horizontal=True )
        
    # Scinece Tab
    with tab5:
        st.header("F")

        # The code for taking the Google sheet info (ttl = time lag between the google sheet and the app)
       #  worksheet=( Page number from the google sheet)
        data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="420251096",ttl=5,), range(20))
        data2 = conn.read(spreadsheet=url,worksheet="935720519",ttl=5,)
        data3= pd.DataFrame(conn.read(spreadsheet=url,worksheet="237625423",ttl=5,))
        
        st.dataframe(data2,hide_index=True)
        st.line_chart(data1)
        st.subheader(" Unit Proficiency")
        st.bar_chart(data3, y_label="Units", x_label="Percentage", horizontal=True )
       
     
     
   
    st.sidebar.markdown("DashBoard")

# The Schedule page
def page2():
    st.title("Schedule")
   
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
    
# AI Chat Bot
def page3():

# The name of the pages ( What the name will be on the app)
page_names_to_funcs = {
    "DashBoard": main_page,
     "Schedule": page2,
     "AI Chat Bot": page3,
}

# Putting the pages on the side bar 
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

