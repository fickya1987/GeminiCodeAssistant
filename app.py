import streamlit as st
import os
import sqlite3
import google.generativeai as gen 
import pandas as pd
from prompts import javascript_prompt,python_prompt,sql_prompt
from dotenv import load_dotenv

load_dotenv()  # Loading environment variable

# Configuration
gen.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Google Gemini model 
def gemini_response(question, prompt):
    model = gen.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt+question])
    return response.text

# Retrieving query
def query(sql_query, db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(sql_query)
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

#streamlit configuration
st.set_page_config(
    page_title="SQL, Python and JavaScript Assistant",
    page_icon="👨‍💻",
    layout="centered"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title-text {
        font-size: 37px; /* Size for title */
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
        -webkit-background-clip: text;
        color: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)

selected_option=st.sidebar.selectbox("Select Language",("SQL","Python","JavaScript"))

st.markdown('<h1 class="title-text">SQL, Python, and JavaScript Assistant👨‍💻</h1>', unsafe_allow_html=True)


if selected_option=="SQL":
    # User input for the English text to be converted to SQL
    st.header(":blue[English to SQL Conversion 📊]")
    user_english_text = st.text_area("Enter your English text:")

    # Path to your SQLite database
    db_path = "student.db"

    if st.button("Submit"):
        if user_english_text:
            # Generate SQL query using the gemini model
            generated_sql_query = gemini_response(user_english_text, sql_prompt)
            st.write("Generated SQL Query:")
            st.code(generated_sql_query, language='sql')
            
            # Fetch the query result from the database
            try:
                result = query(generated_sql_query, db_path)
                
                if result:
                    # Get column names from the database schema
                    conn = sqlite3.connect(db_path)
                    c = conn.cursor()
                    c.execute(generated_sql_query)
                    columns = [description[0] for description in c.description]
                    conn.close()
                    
                    # Create a DataFrame to display the results in a tabular format
                    df = pd.DataFrame(result, columns=columns)
                    st.write("Query Result:")
                    st.dataframe(df)
                else:
                    st.write("No results found.")
            except sqlite3.Error as error:
                st.error(f"Error executing query: {error}")
        else:
            st.warning("Please enter the English text to convert to SQL.")

if selected_option=="Python":
    # User input for the English text to be converted to Python
    st.header(":blue[English to Python Code Converter 🐍]")
    user_input = st.text_area("Enter your English text:")

    if st.button("Convert"):
        if user_input:
            try:
                python_code = gemini_response(user_input,python_prompt)
                st.code(python_code, language="python")
            except Exception as e:
                st.error(f"Error generating Python code: {e}")
        else:
            st.warning("Please enter the English text to convert.")

if selected_option=="JavaScript":
    # User input for the English text to be converted to JavaScript 
    st.header(":blue[English to JavaScript Code Converter]")
    user_input = st.text_area("Enter your English text:")

    if st.button("Convert"):
        if user_input:
            try:
                js_code = gemini_response(user_input,javascript_prompt)
                st.code(js_code, language="javascript")
            except Exception as e:
                st.error(f"Error generating JavaScript code: {e}")
        else:
            st.warning("Please enter the English text to convert.")
            