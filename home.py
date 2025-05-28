import streamlit as st

st.set_page_config(page_title="Portofolio")

st.sidebar.title('Homepage')
page = st.sidebar.radio('Pilih halaman:', ['Home', 'Projek','Tentang Saya'])

if page == 'Home':
    st.markdown("<h1 style='text-align: center;'>Welcome To My Portofolio</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Data Science Enthusiast</h2>", unsafe_allow_html=True)

elif page == 'Projek':
    import projek
    projek.projek()

elif page == 'Tentang Saya':
    import kontak
    kontak.link()
