import streamlit as st
st.set_page_config(page_title="My First Website",page_icon=":tada:",layout="wide")

st.subheader("Hey its Me Hanzala :wave:")
st.title ("I am a Junior Developer from Pakistan")
st.write ("A passionate developer eager to leran how to develop and deploy website to keen my knowledge as a developer want to enhance my skills")
st.write ("[Learn more >] (https://github.com/HanzalaWahid)" )


with st.container():
    st.write
    left_column,right_column  = st.columns([4,1])  # Create two columns with equal width

with left_column:
    st.header ('About')                            # Add a title for this section
    st.markdown('''
                **About me**
                
                I'm Wahid Hanzala and I'm currently pursuing my Bachelor of Science in Artificial Intelligence at Dawood University of Engineering &  Technology (DUET). My I am a junior developer who is passionate about learning Python programming languages and technologies. My main
                Domain is Data Science  and I'm currently learning Python programming language My main interest lies in Data Visualization and Deep Learning.
                I'm Hanzala Wahid, a junior developer who is passionate about coding
                ''')

                