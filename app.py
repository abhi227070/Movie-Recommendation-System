import streamlit as st
import pickle
import pandas as pd
import requests
import random


st.set_page_config(page_title="Movie Recommendation System",page_icon=":tada:",layout="wide")

movie_dict=pickle.load(open("movie_dict.pkl","rb"))
movie=pd.DataFrame(movie_dict)
similarity=pickle.load(open("similarity.pkl","rb"))

def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style\style.css")



def fetch_data(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=c1a0fd94adf3e2100677929be4361d07&language=en-U".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data["poster_path"]

def recommend(name):
    index = movie[movie['title'] == name].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    recommended_movies=[]
    recommended_poster=[]
    for i in distances[1:16]:
        recommended_movies.append(movie.iloc[i[0]].title)
        recommended_poster.append(fetch_data(movie.iloc[i[0]].movie_id))
    return recommended_movies,recommended_poster

#Header section

with st.container():

    st.title("Movie Recommendation System")



    option = st.selectbox(
        'How would you like to be contacted?',
        movie["title"].values)
    if st.button('Recommend'):
        name,poster=recommend(option)
        col1,col2,col3,col4,col5 = st.columns(5)

        with col1:
            st.image(poster[0])
            st.text(name[0])
            

        with col2:
            st.image(poster[1])
            st.text(name[1])
            

        with col3:
            st.image(poster[2])
            st.text(name[2])
            

        with col4:
            st.image(poster[3])
            st.text(name[3])
            

        with col5:
            st.image(poster[4])
            st.text(name[4])
            

        with col1:
            st.image(poster[5])
            st.text(name[5])
            

        with col2:
            st.image(poster[6])
            st.text(name[6])
            

        with col3:
            st.image(poster[7])
            st.text(name[7])
            

        with col4:
            st.image(poster[8])
            st.text(name[8])
            

        with col5:
            st.image(poster[9])
            st.text(name[9])
            

        with col1:
            st.image(poster[10])
            st.text(name[10])
            

        with col2:
            st.image(poster[11])
            st.text(name[11])
            
        
        with col3:
            st.image(poster[12])
            st.text(name[12])
            

        with col4:
            st.image(poster[13])
            st.text(name[13])
            

        with col5:
            st.image(poster[14])
            st.text(name[14])
            
    else:

        random_number = []
        random_poster = []
        # Set a length of the list to 10
        for i in range(0,30):

            # any random numbers from 0 to 1000
            random_number.append(random.randint(0, 4804))

        random_movies = []
        random_id = []

        for i in random_number:
            random_movies.append(movie_dict['title'][i])

        for i in random_number:
            random_id.append(movie_dict['movie_id'][i])

        for i in random_id:
            random_poster.append(fetch_data(i))

                
                
        col1,col2,col3,col4,col5 = st.columns(5)

        with col1:
            st.image(random_poster[0])
            st.text(random_movies[0])
            

        with col2:
            st.image(random_poster[1])
            st.text(random_movies[1])
            

        with col3:
            st.image(random_poster[2])
            st.text(random_movies[2])
            

        with col4:
            st.image(random_poster[3])
            st.text(random_movies[3])
            

        with col5:
            st.image(random_poster[4])
            st.text(random_movies[4])
            

        with col1:
            st.image(random_poster[5])
            st.text(random_movies[5])
            

        with col2:
            st.image(random_poster[6])
            st.text(random_movies[6])
            

        with col3:
            st.image(random_poster[7])
            st.text(random_movies[7])
            

        with col4:
            st.image(random_poster[8])
            st.text(random_movies[8])
            

        with col5:
            st.image(random_poster[9])
            st.text(random_movies[9])
            

        with col1:
            st.image(random_poster[10])
            st.text(random_movies[10])
            

        with col2:
            st.image(random_poster[11])
            st.text(random_movies[11])
            
                
        with col3:
            st.image(random_poster[12])
            st.text(random_movies[12])
            

        with col4:
            st.image(random_poster[13])
            st.text(random_movies[13])
            

        with col5:
            st.image(random_poster[14])
            st.text(random_movies[14])
        with col1:
            st.image(random_poster[15])
            st.text(random_movies[15])
            

        with col2:
            st.image(random_poster[16])
            st.text(random_movies[16])
            

        with col3:
            st.image(random_poster[17])
            st.text(random_movies[17])
            

        with col4:
            st.image(random_poster[18])
            st.text(random_movies[18])
            

        with col5:
            st.image(random_poster[19])
            st.text(random_movies[19])
            

        with col1:
            st.image(random_poster[20])
            st.text(random_movies[20])
            

        with col2:
            st.image(random_poster[21])
            st.text(random_movies[21])
            
                
        with col3:
            st.image(random_poster[22])
            st.text(random_movies[22])
            

        with col4:
            st.image(random_poster[23])
            st.text(random_movies[23])
            

        with col5:
            st.image(random_poster[24])
            st.text(random_movies[24])
        with col1:
            st.image(random_poster[25])
            st.text(random_movies[25])
            

        with col2:
            st.image(random_poster[26])
            st.text(random_movies[26])
            

        with col3:
            st.image(random_poster[27])
            st.text(random_movies[27])
            

        with col4:
            st.image(random_poster[28])
            st.text(random_movies[28])
            

        with col5:
            st.image(random_poster[29])
            st.text(random_movies[29])


# Footer part

with st.container():
    st.write("---")
    st.subheader("Get in contect with me")
    st.write("##")

    contact_form="""<form action="https://formsubmit.co/abhijeetmaharana77@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your e-mail" required>
     <textarea name="message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button>
    </form>"""

    left_column,right_column=st.columns(2)

    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)



with st.container():
    st.write("---")
    st.write("##")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.write("2023 © Movie-Recommendation System | All Rights Reserved.")
    with col3:
        st.write("      Privacy Policy")
        st.write("      Terms and Conditions")
        st.write("      Copyright")
            






        
        

    
