import streamlit as st
from streamlit_option_menu import option_menu
import time
from PIL import Image
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="BMI Calculator", page_icon=":herb:")

#INPUT CSS
with open('css file.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#SIDEBAR MENU
with st.sidebar:
     selected = option_menu("Main Menu", ["Home", 'BMI Calculator','Tentang BMI', 'Tips','Tentang Kami'], 
        icons=['house', 'calculator','book', 'heart', 'inbox'], menu_icon="cast")
     selected

#Menghitung BMI
def hitung_bmi(berat_badan, tinggi_badan):
    if tinggi_badan == 0:
        return None
    bmi = berat_badan / ((tinggi_badan/100) ** 2)
    return bmi


#Menghitung BBI
def hitung_bbi(jenis_kelamin, tinggi_badan):
    if jenis_kelamin == "Pria":
        bbi = (tinggi_badan - 100) - ((tinggi_badan - 100) * 10 / 100)
    elif jenis_kelamin == "Wanita":
        bbi = (tinggi_badan - 100) - ((tinggi_badan - 100) * 15 / 100)
    else:
        bbi = None
    if bbi is not None and bbi <= 0:
        bbi = None
        st.warning('Pastikan semua kolom terisi', icon="⚠️")

    return bbi

#Nilai BMI
def nilai_bmi(bmi):
    if bmi is None:
        return "Tidak dapat dihitung"
    elif bmi < 17.0:
        return "Kekurangan BB Tingkat Berat"
    elif bmi < 18.5:
        return "Kekurangan BB Tingkat Ringan"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Kelebihan BB Tingkat Ringan"
    else:
        return "Kelebihan BB Tingkat Berat"
    
#Keterangan BMI
def keterangan(bmi):
    if bmi is None:
        return "Pastikan kolom sudah terisi semua"
    elif bmi < 17.0:
        return "Hasil perhitungan menunjukkan bahwa Anda memiliki berat badan kurang atau tergolong kurus sekali. Hasil ini berdasarkan angka BMI Anda berada di bawah 17,0."
    elif bmi < 18.5:
        return "Hasil perhitungan menunjukkan bahwa Anda memiliki berat badan kurang atau tergolong kurus. Hasil ini berdasarkan angka BMI Anda berada di bawah 18.5."
    elif bmi < 25:
        return "Hasil perhitungan menunjukkan bahwa Anda memliki berat badan normal. Hasil ini berdasarkan angka BMI Anda yang ada di antara angka 18.5 sampai 25,0. Memiliki berat badan ideal bisa menjadi salah satu cara untuk menjaga kesehatan tubuh secara keseluruhan. Anda juga bisa terhindar dari berbagai risiko penyakit berbahaya."
    elif bmi < 30:
        return "Hasil perhitungan menunjukkan bahwa Anda memiliki berat badan berlebih atau gemuk. Hasil ini berdasarkan angka BMI Anda yang ada di antara angka 25,1 sampai 27,0"
    else:
        return "Hasil perhitungan menunjukkan bahwa Anda memiliki berat badan berlebih atau obesitas. Hasil ini berdasarkan angka BMI Anda lebih dari 27,0."

if selected == "Home":
   st.markdown("<h1 style='font-family: Georgia; text-align: center; color: white;'>Welcome to BMI Calculator</h1>", unsafe_allow_html=True)

   url = "https://assets2.lottiefiles.com/packages/lf20_yczklbgc.json"
   response = requests.get(url)
   animation = response.json()
   
   st_lottie(animation)

   st.write("<p style='font-family: Georgia; text_align: justify; color: white;'>Alat ini digunakan untuk mengidentifikasi apakah berat badan Anda termasuk dalam kategori ideal atau tidak. Kalkulator ini dapat digunakan oleh seseorang yang berusia 18 tahun ke atas.</p>", unsafe_allow_html=True)
   
   
if selected == "BMI Calculator":
   st.markdown("<h1 style='font-family: Georgia; text-align: center; color: white;'>BMI Calculator</h1>", unsafe_allow_html=True)
   jenis_kelamin = st.radio(
    "Pilih jenis kelamin",
    ('Pria', 'Wanita'))
   tinggi_badan = st.number_input("Masukkan tinggi badan Anda (dalam cm): ", min_value=0.00, format="%.2f")
   berat_badan = st.number_input("Masukkan berat badan Anda (dalam kg): ", min_value=0.00, format="%.2f")
   Tombol = st.button("Hitung")


   #Tombol ditekan
   if Tombol:
      with st.spinner('Please wait'):
         time.sleep(1)
         tinggi_badan = float("%.2f" % tinggi_badan)
         berat_badan = float("%.2f" % berat_badan)

         bbi = hitung_bbi(jenis_kelamin, tinggi_badan)
         bmi = hitung_bmi(berat_badan, tinggi_badan)

   #Output data
      with st.container():
         if bbi is not None:
            st.write("Berat badan ideal Anda adalah :", bbi, "kg.")
         if bmi is not None:
            st.write("Indeks Massa Tubuh (BMI) Anda adalah :", bmi)
            st.write("Nilai BMI Anda termasuk kategori :", nilai_bmi(bmi))
            st.write(keterangan(bmi))
         if st.button('Ulang'):
            with st.spinner('Please wait'):
               time.sleep(1)

#SIDEBAR MENU
if selected == "Tentang BMI":
   st.markdown("<h1 style='font-family: Georgia; text-align: center; color: white;'>Apa Itu BMI?</h1>", unsafe_allow_html=True)
   st.write("<p style='font-family: Georgia; text-align: justify; color: white;'>BMI atau Body Mass Index adalah indeks yang digunakan untuk mengukur proporsi antara berat badan dan tinggi badan seseorang. BMI diperoleh dari perbandingan antara berat badan dalam kilogram (kg) dengan tinggi badan dalam meter (m) yang dikuadratkan. BMI digunakan sebagai penilaian awal apakah seseorang memiliki berat badan yang sehat atau tidak.</p>"
            , unsafe_allow_html=True)
   st.write("<p style='font-family: Georgia; text-align: justify; color: white;'>BMI biasanya digunakan untuk menilai risiko terjadinya penyakit terkait kelebihan atau kekurangan berat badan, seperti diabetes, penyakit jantung, dan beberapa jenis kanker. Berdasarkan hasil BMI, seseorang dapat dikategorikan ke dalam kelompok berat badan yang sehat, kekurangan berat badan, kelebihan berat badan, atau obesitas.</p>"
            , unsafe_allow_html=True)
   
   st.write("<br></br>", unsafe_allow_html=True)

   st.markdown("<h1 style='font-family: Georgia; text-align: center; color: white;'>Apa yang perlu dilakukan setelah mengetahui hasil BMI?</h1>", unsafe_allow_html=True)
   st.write("<p style='font-family: Georgia; text-align: justify; color: white;'>Perlu diingat bahwa BMI tidak selalu menjadi indikator yang akurat untuk menentukan apakah seseorang memiliki berat badan yang sehat atau tidak. Terdapat faktor-faktor lain seperti komposisi tubuh dan massa otot yang perlu dipertimbangkan. BMI dapat Anda gunakan sebagai titik acuan mengenai masalah berat badan Anda. Oleh karena itu, sebaiknya Anda berkonsultasi dengan dokter atau ahli gizi untuk menentukan apakah BMI Anda sudah sehat atau masih perlu diperbaiki.</p>"
          , unsafe_allow_html=True)
   
if selected == "Tips":
   st.markdown("<h1 style='font-family: Georgia; text-align: center; color: white;'>Tips Menjaga Berat Badan Ideal</h1>", unsafe_allow_html=True)

   st.markdown("<h4 style='font-family: Georgia; color: white;'>1. Perhatikan asupan</h4>", unsafe_allow_html=True)
   st.write("<p style='font-family: Georgia; text-align: justify; color: white;'>Mulailah untuk menghindari makanan tinggi kalori, seperti soda, makanan yang banyak mengandung gula, dan juga fast food. Ubahlah kebiasaan tersebut dengan perbanyak konsumsi buah sayuran. Buah dan sayuran mengandung banyak serat, vitamin, dan mineral yang baik untuk tubuh dan membantu menjaga berat badan ideal.</p>"
         , unsafe_allow_html=True)

   st.markdown("<h4 style='font-family: Georgia; color: white;'>2. Olahraga </h4>", unsafe_allow_html=True)
   st.write("<p style='font-family: Georgia; text-align: justify; color: white;'>Olahraga membantu membakar kalori dan meningkatkan metabolisme tubuh. Tidak perlu berolahraga berat, jalan kaki pun sudah dapat dikatakan sebagai olahraga. </p>"
         , unsafe_allow_html=True)

   st.markdown("<h4 style='font-family: Georgia; color: white;'>3. Tidur yang cukup</h4>", unsafe_allow_html=True)
   st.write("<p style='font-family: Georgia; text-align: justify; color: white;'>Kurang tidur dapat mempengaruhi hormon yang mengatur nafsu makan dan metabolisme tubuh. Cobalah untuk tidur yang cukup, minimal 7-8 jam setiap malam.</p>", unsafe_allow_html=True)


   st.markdown("<h4 style='font-family: Georgia; color: white;'>4. Kurangi stress</h4>", unsafe_allow_html=True)
   st.write("<p style='font-family: Georgia; text-align: justify; color: white;'>Stres dapat mempengaruhi hormon yang mengatur nafsu makan dan dapat menyebabkan penumpukan lemak di perut. Cobalah untuk mengurangi stres dengan melakukan aktivitas yang menyenangkan</p>", unsafe_allow_html=True)
   
   st.markdown("<h4 style='font-family: Georgia; color: white;'>5. Memenuhi kebutuhan cairan tubuh</h4>", unsafe_allow_html=True)
   st.write("<p style='font-family: Georgia; text-align: justify;color: white;'>Minum air akan meningkatkan rasa kenyang dan membantu menjaga asupan kalori tetap terkendali, terutama jika minum satu atau dua gelas sebelum makan. Selain itu, minum air putih telah terbukti sedikit meningkatkan kalori yang dibakar sepanjang hari.</p>", unsafe_allow_html=True)

if selected == 'Tentang Kami':
   st.markdown("<h1 style='font-family: Georgia; text-align: center; color: white;'>Tentang Kami</h1>", unsafe_allow_html=True)

   st.write("<p style='font-family: Georgia; text-align: justify; color: white;'>Kami dari kelompok 6 kelas 1E Penjaminan Mutu Industri Pangan Politeknik AKA Bogor. Kalkulator BMI kami dirancang untuk membantu Anda menghitung berat badan ideal Anda dan memberikan saran tentang cara mencapainya. Kami memahami bahwa setiap orang memiliki kebutuhan yang berbeda, dan itulah mengapa kami menyediakan sumber daya yang dapat disesuaikan dengan kebutuhan Anda. Jangan ragu untuk menghubungi kami untuk memberi kritik dan saran. </p>"
          , unsafe_allow_html=True)
   font_size = "20px"

   #image
   ismi = Image.open('ismi.jpg')
   silmi = Image.open('silmi.jpeg')
   eka = Image.open('eka.jpeg')
   talitha = Image.open('talitha.jpeg')
   raja = Image.open('raja.jpeg')

   # display the images in a row
   col1, col2, col3, col4, col5= st.columns(5)

   with col1:
      st.image(ismi, use_column_width=True)
      st.caption(f"<span style='font-size:{font_size}; font-family: Georgia'>Ismi Maharani (2220459)</span>", unsafe_allow_html=True)

   with col2:
      st.image(raja, use_column_width=True)
      st.caption(f"<span style='font-size:{font_size}; font-family: Georgia'>Raja Nur Falah (2220483)</span>", unsafe_allow_html=True)

   with col3:
      st.image(silmi, use_column_width=True)
      st.caption(f"<span style='font-size:{font_size}; font-family: Georgia'>Silmi Arijah (2220488)</span>", unsafe_allow_html=True)

   with col4:
      st.image(eka, use_column_width=True)
      st.caption(f"<span style='font-size:{font_size}; font-family: Georgia'>Sri Rizka Nurwahidah (2220490)</span>", unsafe_allow_html=True)

   with col5:
      st.image(talitha, use_column_width=True)
      st.caption(f"<span style='font-size:{font_size}; font-family: Georgia'>Talitha Dias Azzahra (2220492)</span>", unsafe_allow_html=True)


# Menambahkan footer pada Streamlit
footer = """
<footer style='text-align: center;'>
    <hr>
    <p>&copy; Kelompok 6</p>
</footer>
"""
st.write(footer, unsafe_allow_html=True)
