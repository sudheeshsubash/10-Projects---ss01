import streamlit as st
from bs4 import BeautifulSoup
import requests



def get_tag_and_filter_it(soup=None):

    collect_elements = [soup]
    i = 1
    while tag_name:= st.text_input("Enter tag name",key=f"key_{i}"):
        tag_split = tag_name.split(',')

        if len(tag_split) == 1:
            new_soup = collect_elements[-1].find_all(tag_name)
                
        elif len(tag_split) == 2 and 'class' in tag_split[1].split("=")[0]:
            new_soup = collect_elements[-1].find_all(tag_split[0],class_=tag_split[1].split('=')[1])
                
        elif len(tag_split) == 2 and id in tag_split[1]:
            new_soup = collect_elements[-1].find_all(tag_split[0],id=tag_split[1].split('=')[1])
            
        st.code(new_soup,'html')
        i += 1



            
def main():
    """Gets user input URL, makes request, checks response, and parses HTML.
    
    This function allows the user to enter a URL, makes a GET request to that URL, 
    checks that the response status is 200 OK, parses the HTML with BeautifulSoup,
    and passes the parsed HTML to another function for further processing.
    
    Args:
      None
    
    Returns:
      None
    """
    
    if url:= st.text_input('Enter Url',key='url'):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        try:
            response = requests.get(url,headers=headers)
        except Exception as e:
            st.write(f"{e}")

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            get_tag_and_filter_it(soup)



if __name__ == '__main__':
    
    st.title('Web Scraper application')
    st.text('Enter URL and get filtered HTML Elements')
    
    main()


















    # collect_elements = [soup]
    
    # if tag_name := st.text_input("Enter tag name",key=f"key_{tag_key}"):
    #     tag_split = tag_name.split(',')
    #     if len(tag_split) == 1:
    #         new_soup = collect_elements[-1].find_all(tag_name)
    #         st.code(new_soup,'html')
    #         if st.button("Select Element",key=f"buttonkey_{tag_key+1000}"):
    #             collect_elements.append(new_soup)
    #         if st.button("SelectPrevious Element",key=f"buttonkey_{tag_key+100}"):
    #             collect_elements.pop()
                
        # elif tag_split[1].split('=')[0] == 'class':
        #     new_soup = soup.find_all(tag_split[0],class_=tag_split[1].split('=')[1])
        #     print(tag_split[1].split('=')[1])
        #     st.code(new_soup,'html')
        #     if st.button("Select",key=f"buttonkey_{tag_key+1000}"):
        #         get_tag_and_filter_it(new_soup,tag_key+100)
        #     else:
        #         get_tag_and_filter_it(soup,tag_key+1)
            
        # elif tag_split[1].split('=')[0] == 'id':
        #     new_soup = soup.find_all(tag_split[0],id=tag_split[1].split('=')[1])
        #     st.code(new_soup,'html')
        #     if st.button("Select",key=f"buttonkey_{tag_key+1000}"):
        #         get_tag_and_filter_it(new_soup,tag_key+100)
        #     else:
        #         get_tag_and_filter_it(soup,tag_key+1)