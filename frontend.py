import streamlit as st
import requests

st.title("Food Prices Scraper")

url = st.text_input("Enter the URL to scrape:")

if st.button("Scrape"):
    if url:
        with st.spinner("Scraping..."):
            url = "https://rebel-foods-bot-backend.onrender.com/scrape"
            response = requests.post(url, json={"url": "https://example.com"})
            if response.status_code == 200:
                result = response.json()
                st.write("Response status:", response.status_code)
                st.write("Response text:", response.text)
                if "data" in result:
                    st.success(f"Scraped data from {result['platform'].title()}")
                    st.write(result["restaurant"], result["city"])
                    st.dataframe(result["data"])
                else:
                    st.error(result.get("error", "Unknown error"))
            else:
                st.error("Failed to connect to backend.")
