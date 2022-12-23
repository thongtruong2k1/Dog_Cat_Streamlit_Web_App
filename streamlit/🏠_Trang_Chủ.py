import streamlit as st

import numpy as np
from PIL import Image

st.set_page_config("Animals Store", page_icon="dog", layout="wide")
sideb = st.sidebar
sideb.markdown("Hello")

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

st.markdown("""
            <style>
                .overlay{position: absolute;
                        display: flex;
                        top: 0;
                        bottom: 0;
                        left: 0;
                        right: 5;
                        align-items: center;
                        justify-content: center;
                        flex-direction: column;
                        color: white;
                        text-align: center;
                        }
                        .overlay .videoButtonWrapper{
                            flex-direction: row;
                            margin-bottom: 10px;
                        }
                        .videoBackgroundWrapper{position: relative; width: 100%;}
                        .videoBackground{width: 100%;}
                        .tooltip:hover .tooltiptext {
                            visibility: visible;
                }
                #container {
                    width: 100vw;
                    height: 100vh;
                    text-align: center;
                    overflow: hidden;
                }
                #videobcg {
                    width: inherit;
                    height: inherit;
                    -o-filter: brightness(70%);
                    filter: brightness(70%);
                    object-fit: cover;  
                    transform: scale(1.04);
                }
            </style>
            <div id="container">
                <video id="videobcg" preload="" playsinline="" autoplay="" muted="" loop="" class="stvideo">
                    <source src="https://dogily.vn/wp-content/uploads/2021/10/dogilybanner002.mp4" type="video/mp4">
                </video>
                <div class="overlay" >
                    <h1 style="font-size: 5rem" class="text-warning"><b>Dogily Farm & Petshop</b></h1>
                    <p style="font-size: 1.25rem" class="text-light" class="ml-14">
                        <strong>Dogily</strong> là thương hiệu đầu tiên tại Việt Nam xây dựng thành công <strong>hệ sinh thái khép kín</strong> gồm các Trang trại nhập khẩu, nhân giống chó mèo cảnh, chuỗi siêu thị thú cưng, Phòng khám thú y, dịch vụ Spa &amp; Grooming tại <strong>Tphcm, Hà Nội &amp; Đà Lạt</strong><br>
                    </p>
                </div>
            </div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="container section-title-container" style="margin-bottom:0px;">
    <h2 class="section-title section-title-center">
        <b></b>
        <span class="section-title-main" style="font-size:150%;">Giống chó cảnh</span>
        <b></b>
    </h2>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-+sLIOodYLS7CIrQpBjl+C7nPvqq+FbNUBDunl/OZv93DB7Ln/533i8e/mZXLi/P+" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
