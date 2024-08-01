from flask import Flask
import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_lottie import st_lottie
from contextlib import redirect_stderr
from operator import methodcaller
from pickletools import read_uint1
from wsgiref.util import request_uri
from flask import Flask, request, jsonify, render_template, request, redirect, url_for
import pickle
import numpy as np
import pandas as pd
import math

app = Flask(__name__)


new_df = pd.read_pickle('rest_dicti.pkl')
data = pd.read_pickle('data.pkl')

rest_names = new_df['name'].values
option = st.selectbox('Select the preferred restuarant?',rest_names)

        
similarity = pickle.load(open('similarity.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
