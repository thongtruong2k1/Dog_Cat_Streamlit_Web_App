import streamlit as st
import sqlite3
from sqlite3 import Error

st.set_page_config("Animals Store", page_icon="dog", layout="wide")
st.markdown("""<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">""", unsafe_allow_html=True)

st.markdown("""
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="/"><img width="200" height="100" src="https://dogily.vn/wp-content/uploads/2020/07/dogily-logo.png" class="header_logo header-logo entered lazyloaded" alt="Dogily Petshop – Bán chó mèo cảnh, thú cưng Tphcm, Hà nội" data-lazy-src="https://dogily.vn/wp-content/uploads/2020/07/dogily-logo.png" data-ll-status="loaded"></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="/"><b>Home</b> <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/Danh_Mục_Sản_Phẩm"><b>Danh Mục Sản Phẩm</b></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/Giỏ_Hàng"><b>Giỏ Hàng</b></a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
""", unsafe_allow_html=True)


tab1, tab2= st.tabs(["Cat", "Dog"])

AvatarStyle = [ 
    "adventurer", 
    "adventurer-neutral", 
    "avataaars",
    "big-ears",
    "big-ears-neutral",
    "big-smile",
    "bottts", 
    "croodles",
    "croodles-neutral",
    "female",
    "human",
    "male"
]

def write_animals(name, image):
    return st.markdown(f"""
            <div class="text-center">
                <h3 style='text-align: center; color: black;'>Cat {count}</h3>
                <a href='http://localhost:8501/Chi_Tiết_Sản_Phẩm'>
                    <img src='https://avatars.dicebear.com/api/{avatar}/15.jpg'>
                </a>
                <p style='text-align: left; color: black;'>
                    <br><b>Giống</b>: Ai Cập <br>
                    <b>Giới tính</b>: Đực <br>
                    <b>Vacxin</b>: Đã tiêm <br>
                    <b>Tuổi</b>: 2 </br>
                </p>
            </div>
            """, unsafe_allow_html=True)

with tab1:
    st.header("Chọn loại mèo mà bạn thích")
    col1, col2, col3 = tab1.columns(3)
    count = 1
    max = 10
    with col1:
        for avatar in AvatarStyle[:4]:
            write_animals(count, avatar)
            # st.markdown(f"<h3 style='text-align: center; color: black;'>Cat {count}</h3>", unsafe_allow_html=True)
            # st.markdown(f"<a href='http://localhost:8501/Chi_Tiết_Sản_Phẩm'><img src='https://avatars.dicebear.com/api/{avatar}/15.jpg'></a>", unsafe_allow_html=True)
            # st.markdown(f"<p style='text-align: left; color: black;'><b>Giống</b>: Ai Cập<br> <b>Màu sắc</b>: Trắng<br><b>Giới tính</b>: Đực<br><b>Tuổi</b>: 2</br></p>", unsafe_allow_html=True)
            st.markdown("----------------------------------")
            count += 3

    with col2:
        count = 2
        for avatar in AvatarStyle[4:8]:
            write_animals(count, avatar)
            st.markdown("----------------------------------")
            count += 3

    with col3:
        count = 3
        for avatar in AvatarStyle[8:]:
            write_animals(count, avatar)  
            st.markdown("----------------------------------")
            count += 3

with tab2:
    st.header("Chọn loại chó mà bạn thích")

    col1, col2, col3 = tab2.columns(3)
    count = 1
    max = 10
    with col1:
        for avatar in range(4):
            write_animals(count, avatar)
            st.markdown("----------------------------------")
            count += 3

    with col2:
        count = 2
        for avatar in range(4):
            write_animals(count, avatar)
            st.markdown("----------------------------------")
            count += 3

    with col3:
        count = 3
        for avatar in range(4):
            write_animals(count, avatar)
            st.markdown("----------------------------------")
            count += 3

st.markdown("""
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-+sLIOodYLS7CIrQpBjl+C7nPvqq+FbNUBDunl/OZv93DB7Ln/533i8e/mZXLi/P+" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)