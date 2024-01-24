import streamlit as st
import urlshorter

if __name__ == '__main__':

    st.title('This is a Url Shortener application')
    st.subheader("Enter your URL and get your shortened URL,Some time urls are very long so we can't show them on the screen. we can't handle that. So we have created this application to shorten your urls")
    if url := st.text_area('Enter URL'):
        shorted_url = urlshorter.shortener(url)
        st.write(f"shorted url :- {shorted_url}")