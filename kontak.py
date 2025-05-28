import streamlit as st

def link():
    col1,col2 = st.columns(2)
    with col1:
        st.header('Bangkit Dwiputra Erlangga')
        st.markdown('Email : bangkitdwip13@gmail.com')
        st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/bangkit-dwiputra)", unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;"> A highly motivated and adaptable Electrical Engineering graduate with hands-on experience in manufacturing, preventive maintenance, and process improvement.</div>', unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>Currently transitioning into the field of Data Science, with strong interest in data analysis, statistical testing, and building data-driven solutions. </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>Passionate about applying technical problem-solving skills to uncover insights from data. </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>Actively developing skills in Python, data visualization, and machine learning through independent projects and platforms like Streamlit.", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'> Known for being analytical, fast learner, and consistently eager to explore how data can drive innovation in various industries.</div>", unsafe_allow_html=True)
    with col2:
        st.image('https://drive.google.com/uc?export=view&id=1E-LtFsdXoqNdERqzFJBsp_xIr7Hdug5P',use_container_width=True)
    
