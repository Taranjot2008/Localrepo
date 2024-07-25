<<<<<<< HEAD
from PIL import Image #type: ignore
import requests # type: ignore
import streamlit as st # type: ignore
from streamlit_lottie import st_lottie #type: ignore
=======
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
>>>>>>> ee6530670af54fb26e2ec568363e63e95cfb90c2

st.set_page_config(page_title='My Webpage',page_icon=':tada:',layout='wide')

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#use local css 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css("style/style.css")
#Header Section
with st.container():
    st.subheader('Hi my name is Taranjot Singh:wave:')
    st.title('A Student from Yarmouth')
    st.write('Hi I am Taranjot singh. I am a student from Yarmouth Nova scotia and I like python and coding programs')
    st.write('[About me>](https://www.youtube.com/watch?v=-3d1PB3SU3c)')

#---Loading Assets--
lottie_coding=load_lottieurl('https://lottie.host/e8004bfa-a698-4049-ab64-12e759568e1a/YWITA3L5iY.json')
img_contact_form=Image.open('images/lotus-evija-top-gear-test-2.jpg')

#content Section 
with st.container():
    st.write('----')
    left_column, right_column= st.columns(2)
    with left_column:
        st.header('About me')
        st.write('##')
        st.write("""
                This section is about me. I have few hobbies which are being a backyard astronomer,
                football, coding and studying. I have made few research papers which are on blackbody radiation,
                fluid dynamics and quantum gravity and many more.
                """)
        st.write('[My papers>](https://www.youtube.com/watch?v=-3d1PB3SU3c)')
    with right_column:
        st.lottie(lottie_coding , height='100', key='coding')

#putting images and text along with it
with st.container():
    st.write('---')
    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader('I love Cars also this is an image of an koenigsegg jesko')
        st.write('##')
        st.write("""
                I love cars""")
        st.markdown('[Link>](https://www.youtube.com/watch?v=-3d1PB3SU3c)')

#contact information
with st.container():
    st.write('---')
    st.header('Get in touch with me:')
    st.write('##')

    contact_form="""
                <input type="hidden" name="_captcha" value="false">
                <form action="https://formsubmit.co/taranjotscience@gmail.com" method="POST">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email address" required>
                <textarea name="message" placeholder="Your message" required></textarea>
                <button type="submit">Send</button></form>
                """
    left_column, right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
