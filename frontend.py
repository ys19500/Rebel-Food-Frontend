import streamlit as st
import requests

st.title("Food Prices Scraper")

url = st.text_input("Enter the URL to scrape:")

if st.button("Scrape"):
    if url:
        with st.spinner("Scraping..."):
            response = requests.post("https://rebel-foods-bot-backend.onrender.com/scrape", json={"url": url})
            if response.status_code == 200:
                result = response.json()
                if "data" in result:
                    st.success(f"Scraped data from {result['platform'].title()}")
                    st.write(result["restaurant"], result["city"])
                    st.dataframe(result["data"])
                else:
                    st.error(result.get("error", "Unknown error"))
            else:
                st.error("Failed to connect to backend.")
