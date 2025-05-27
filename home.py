import streamlit as st



import streamlit as st

st.set_page_config(page_title="Portofolio")

st.sidebar.title('Homepage')
page = st.sidebar.radio('Pilih halaman:', ['Home', 'Projek','Kontak'])

if page == 'Home':
    st.markdown("<h1 style='text-align: center;'>Welcome To My Portofolio</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Data Scientist Enthusiast</h2>", unsafe_allow_html=True)

elif page == 'Projek':
    import projek
    projek.projek()

elif page == 'Kontak':
    import kontak
    kontak.link()