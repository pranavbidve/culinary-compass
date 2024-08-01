import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import cv2
import math


background_image_url = 'C:\\Users\\bidve\\OneDrive\\Desktop\\Projects\\Zomato Project\\Reccomender\\bg.jpg'


st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url('{background_image_url}') no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)



def load_lottie(url):
    r = requests.get(url)
    if r.status_code!=200:
        st.write("dasdfswlk")
    return r.json()

lottie_coding = load_lottie("https://lottie.host/fe563ee9-79db-442e-9ddd-0bf00117a227/ri1R11uXjv.json")



def load_lottiefile(filepath: str): 
    with open(filepath, "r") as f:
        return json.load(f)


st.markdown(
    """
    <style>
        /* Title */
        .title {
            color: #FF5733;
            font-family: Arial, sans-serif;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }
        
        /* Separator */
        .separator {
            width: 100%;
            height: 2px;
            background-color: #FFC300;
            margin: 20px 0;
        }
        
        /* Select box */
        .select-box select {
            width: 100%;
            padding: 10px;
            font-family: Arial, sans-serif;
            font-size: 18px;
            border: 2px solid #FF5733;
            border-radius: 5px;
            background-color: #F4F4F4;
            color: #333;
        }
        
        /* Background image */
        body {
            background-image: url('C:\\Users\\bidve\\OneDrive\\Desktop\\Projects\\Zomato Project\\Reccomender\\bg.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<p class='title'>Culinary Compass</p>", unsafe_allow_html=True)
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

new_df = pd.read_pickle('data\\rest_dicti.pkl') 
data = pd.read_pickle('data\\data.pkl')

rest_names = new_df['name'].values
# user_text = st.text_input("Enter your location:")
option = st.selectbox('Select the preferred restaurant?', rest_names)


        
similarity = pickle.load(open('data\\similarity.pkl', 'rb'))

indices = []

def recomm(res):
            res_ind = data[data['name'] == res].index[0]
            res_list = sorted(list(enumerate(similarity[res_ind])), reverse = True, key = lambda x: x[1])[1:6]

            recommended_res = []
            res_links = []
            for i in res_list:
                ind = i[0]
                # st.write(ind)   
                indices.append(ind)                       
                recommended_res.append(ind)
      
            return recommended_res


        
name = []
location = []
rating = []
neigh = []
restype = []
priceran = []
url = []

# locations=pd.DataFrame({"Name":data['location'].unique()})

if st.button('Recommend'):
    st.title('Top 5 Restaurants')
    recomendations = recomm(option)


    for i in recomendations:
        name.append(data.iloc[i][1])
        location.append(data.iloc[i][-4][0])
        rating.append(data.iloc[i][4])
        neigh.append(data.iloc[i][-5][0])
        restype.append(data.iloc[i][-6][0])
        priceran.append(data.iloc[i][7])
        url.append(data.iloc[i][0])
        


st_lottie(lottie_coding, height=300, key="coding")

df = pd.read_pickle('data\\df.pkl')

build = df.loc[indices]




















# col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg")

# with col4:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg")

# with col5:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg")


# data_df = pd.DataFrame(
#     {
#         "apps": [
#             "https://www.zomato.com/bangalore/wow-momo-church-street-bangalore",
#             "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
#             "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
#             "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
#         ],
#     }
# )

# st.data_editor(
#     data_df,
#     column_config={
#         "apps": st.column_config.ImageColumn(
#             "Preview Image", help="Streamlit app preview screenshots"
#         , width = 'large')
#     },
#     hide_index=True,
# )


import streamlit as st
import pandas as pd

def display_restaurants(restaurants):
    st.write("<style>div.row-widget.stRadio > div{flex-direction:row;}</style>", unsafe_allow_html=True)
    for index, row in restaurants.iterrows():
        if index % 2 == 0:
            background_color = "#0E2A47"  # Dark blue
        else:
            background_color = "#341C4E"  # Dark purple
        
        st.markdown(f"""
        <div style='
            background: linear-gradient(45deg, {background_color} 0%, {background_color} 45%, #1a1a1a 100%);
            color: #FFFFFF; /* White text on dark background */
            padding: 20px;
            border-radius: 15px; /* Rounded edges */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
            font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif;
            font-size: 18px;
            font-style: italic;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: transform 0.3s ease-in-out;
            cursor: pointer;
            ' onmouseover="this.style.transform='scale(1.05)';" onmouseout="this.style.transform='scale(1)';">
            <div style='margin-left: 20px; font-family: Georgia, serif;'>
                <h2 style='margin-bottom: 0; font-style: italic;'>{row['Name']}</h2>
                <p><strong>📍 Location:</strong> <span style="font-style: italic; color: #007bff;">{row['Location']}</span></p>
                <p><strong>⭐ Rating:</strong> <span style="color: #28a745;">{'⭐' * math.ceil(float(row['Rating']))}</span></p>
                <p><strong>🏘️ Neighborhood:</strong> <span style="font-style: italic; color: #007bff;">{row['Neighborhood']}</span></p>
                <p><strong>🍽️ Type:</strong> <span style="font-style: italic; color: #007bff;">{row['Type']}</span></p>
                <p><strong>💰 Price Range:</strong> <span style="font-style: italic; color: #007bff;">{row['Price Range']}</span></p>
                <p><strong>🍽️ Visit:</strong> <a href="{row['Visit']}" target="_blank" style="font-style: italic; color: #007bff;">Visit Restaurant</a></p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Sample data
data = {
    'Name': name,
    'Location': location,
    'Rating': rating,
    'Neighborhood': neigh,
    'Type': restype,
    'Price Range': priceran,
    'Visit': url
}

restaurants_df = pd.DataFrame(data)



# Set page width
st.markdown(
    """
    <style>
        .reportview-container .main .block-container {
            max-width: 1000px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

display_restaurants(restaurants_df)


from IPython.display import HTML
HTML("""
<style>
h1,h2,h3 {
	margin: 1em 0 0.5em 0;
	font-weight: 600;
	font-family: 'Titillium Web', sans-serif;
	position: relative;  
	font-size: 36px;
	line-height: 40px;
	padding: 15px 15px 15px 2.5%;
	color: #13003A;
	box-shadow: 
		inset 0 0 0 1px rgba(53,86,129, 1), 
		inset 0 0 5px rgba(53,86,129, 1),
		inset -250px 0 35px #FADFFF;
	border-radius: 0 10px 0 15px;
	background: #fff
    
}
</style>
""")




