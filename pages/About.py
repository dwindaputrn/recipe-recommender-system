import streamlit as st
import codecs
import streamlit.components.v1 as components

#page config
st.set_page_config(
    page_title="Recipes Recommendation by Epiktetus",
    page_icon="https://code.iconify.design/2/2.2.1/iconify.min.js",
    layout="wide",
    initial_sidebar_state="collapsed"
)

#st.set_option('public_filetypes', 'pdf, csv, xls, jpg')

HtmlFile = open("about.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height=1500, width=2150, scrolling=True)

#about = open("about.html")
#components.html(about.read())
