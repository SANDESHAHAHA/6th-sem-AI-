import streamlit as st 
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib 


model = joblib.load("news_model.joblib")


st.title("News categorization and Recommendation system")
st.markdown("---")

st.markdown("### Enter the article for its categorization ")

article = st.text_area("Enter the article")

col1,col2,col3,col4,col5 = st.columns(5)
with col1:
    st.metric("Politics","") 
with col2:
    st.metric("Business","") 
with col3:
    st.metric("Tech","") 
with col4:
    st.metric("Entertainment","") 
with col5:
    st.metric("Sport","") 



btn = st.button("show prediction ")
if btn:
    if article.strip() == "":
        st.warning("Please enter a news article before predicting !")
    else:
       prediction = model.predict([article])
       st.write(prediction)