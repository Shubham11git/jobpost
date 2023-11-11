import streamlit as st
import pandas as pd
import requests
import pip
pip.main(["install", "openpyxl"])
# Function to convert Excel to JSON
def convert_excel_to_json(file):
    df = pd.read_excel(file)
    json_data = df.to_json(orient="records", lines=True)
    return json_data
#hello
# Function to submit JSON data to the API
def submit_to_api(json_data, api_key):
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }
    url = 'https://bypnetwork.jobboard.io/api/v1/jobs.json'
    response = requests.post(url, data=json_data, headers=headers)
    print(response,"responseresponseresponse")
    return response

def main():
    st.title("Job Post")

    # File upload
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])

    # Array to store JSON data
    json_data_array = []

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.dataframe(df)

        # Convert DataFrame to JSON
        json_data = convert_excel_to_json(uploaded_file)
        json_data_array.append(json_data)  # Push JSON data to the array

        # Display JSON data
        # st.write("JSON Data:", json_data)

        # API Key input
        api_key = st.text_input("Enter your API Key", type="password")

        # Submit button
        if st.button("Submit to API") and api_key:
            try:
                # Loop through the array and submit each JSON data to the API
                for data in json_data_array:
                    response = submit_to_api(data, api_key)

                    if response.status_code == 200:
                        st.success("JSON data submitted successfully to the API!")
                    else:
                        st.error(f"Failed to submit JSON data to the API. Status code: {response.status_code}")
            except Exception as e:
                st.error(f"Error submitting JSON data to the API: {e}")

if __name__ == "__main__":
    main()

#end  here