import streamlit as st
import pickle

try:
    with open('movie_review_analyzer.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Error: Model file 'movie_review_analyzer.pkl' not found.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.set_page_config(page_title="🎬 Movie Review Analyzer", page_icon="🎥", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        .stTextArea textarea {
            background-color: black;
            border-radius: 10px;
            border: 1px solid #ccc;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 0.5em 1em;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

st.title(' 🎬  Movie Review Analyzer')
st.markdown("""
            

This app uses a Multinomial Naive Bayes model (trained via a Sklearn Pipeline) 
to classify whether a review is **Positive**  or **Negative**.

            
            """)


review_input = st.text_area(
    "Enter a review below for classification:",
    "the movie was engaging"
)


if st.button('🔍 Classify review'):
    if review_input:
        
        prediction = model.predict([review_input])
        
       
        result_label = 'POSITIVE' if prediction == 1 else 'NEGATIVE'
        
        
        st.subheader("Classification Result:")
        
        if prediction == 1:
            st.success(f"✅ **{result_label}**")
            
        else:
            st.error(f"🚨 **{result_label}**")
            
        st.write("---")
        
        
    else:
        st.warning("Please enter a review to classify.")