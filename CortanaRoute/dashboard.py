import streamlit as st
import pandas as pd

# Function to load CSV
def load_csv(file):
    return pd.read_csv(file)

# Streamlit app
st.title("Opps Finder")
st.sidebar.title("Your copilot for sales")
# Drag and Drop for CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

# Check if file is uploaded
if uploaded_file is not None:
    # Load CSV file into a dataframe
    df = load_csv(uploaded_file)
    
    # Display search bar
    search_term = st.text_input("Enter the keyword to search")

    # Search and return result
    if st.button("Search"):
        # Filter rows containing the search term in any column
        result = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        
        if not result.empty:
            st.write("Matching row(s):")
            st.dataframe(result)
        else:
            st.write("No matching row found.")
else:
    st.write("Please upload a CSV file.")
