import streamlit as st
import pandas as pd
from io import BytesIO

# Load CSV file
def load_csv(file):
    data = pd.read_csv(file)
    return data

# Clean and save CSV
def clean_and_save(data):
    # Convert timestamp to datetime
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    
    # Sort data by Timestamp in descending order
    data.sort_values(by='Timestamp', ascending=False, inplace=True)
    
    # Drop duplicates based on 'Nama' column, keeping the last entry
    cleaned_data = data.drop_duplicates(subset=['Nama Lengkap (diisi dengan huruf kapital)'], keep='last')
    
    return cleaned_data

def main():
    st.title("Data Cleaning Web App")

    st.write("Data yang diproses tidak seluruhnya benar.")
    st.write("Silahkan cek ulang data melalui Google Spreadsheet, Excel milik Anda!.")
    st.write("Perhatikan nama file, silahkan rename sesuai format YYMMDD_NAMA SEKOLAH_KELAS_NAMA MT_NAMA MT.")
    
    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Load CSV data
        data = load_csv(uploaded_file)
        
        # Display original data
        st.subheader("Original Data")
        st.write(data)
        
        # Clean and save data
        cleaned_data = clean_and_save(data)
        
        # Display cleaned data
        st.subheader("Cleaned Data")
        st.write(cleaned_data)
        
        # Download cleaned CSV
        csv_buffer = BytesIO()
        cleaned_data.to_csv(csv_buffer, index=False)
        st.download_button("Download Cleaned CSV", data=csv_buffer.getvalue(), file_name='cleaned_data.csv')

if __name__ == "__main__":
    main()
