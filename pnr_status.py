import streamlit as st
import requests

st.title("🚆 Railway PNR Status Checker")

st.markdown("Check the status of an Indian Railways PNR using RapidAPI.")

api_key = st.text_input("Enter RapidAPI Key (x-rapidapi-key)", type="password")
pnr_number = st.text_input("Enter 10-digit PNR Number")

if st.button("Check Status"):
    if not api_key:
        st.error("Please enter your RapidAPI Key.")
    elif not pnr_number or len(pnr_number) != 10:
        st.error("Please enter a valid 10-digit PNR Number.")
    else:
        with st.spinner("Fetching status..."):
            url = f"https://irctc-indian-railway-pnr-status.p.rapidapi.com/getPNRStatus/{pnr_number}"

            headers = {
                "x-rapidapi-key": api_key,
                "x-rapidapi-host": "irctc-indian-railway-pnr-status.p.rapidapi.com"
            }

            try:
                response = requests.get(url, headers=headers)

                if response.status_code == 200:
                    st.success("Status fetched successfully!")
                    st.json(response.json())
                else:
                    st.error(f"Error fetching status. Status code: {response.status_code}")
                    try:
                        st.json(response.json())
                    except:
                        st.text(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
