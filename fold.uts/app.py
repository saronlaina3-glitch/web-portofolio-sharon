import streamlit as st

# 1. Pengaturan Dasar Halaman
st.set_page_config(page_title="Portofolio Unyu", page_icon="🌸", layout="centered")

# 2. Desain Tema Blackpink (CSS Custom)
st.markdown("""
<style>
    /* Mengubah warna background utama menjadi hitam/gelap */
    .stApp {
        background-color: #121212;
        color: #FFE4E1; /* Warna teks pink muda */
    }
    
    /* Mengubah warna judul dan subjudul menjadi Hot Pink */
    h1, h2, h3, h4 {
        color: #FF69B4 !important; 
        font-family: 'Comic Sans MS', cursive, sans-serif; /* Font yang lebih santai */
    }

    /* Mengubah warna Tab Menu */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #FFB6C1; 
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        color: #FF1493 !important;
        border-bottom-color: #FF1493 !important;
    }

    /* Desain kotak untuk daftar pengalaman */
    .kotak-pengalaman {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #FF69B4; /* Garis aksen pink di kiri */
        margin-bottom: 15px;
        color: white;
        box-shadow: 2px 2px 10px rgba(255, 105, 180, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# 3. Bagian Judul Atas
st.title("✨ Website Portofolio Sharon ✨")
st.subheader("Welcome to My Space!")
st.write("---")

# 4. Membuat Navigasi Menu (Tab)
tab1, tab2 = st.tabs(["🏠 Home", "👩‍💻 Profile & Experience"])

# --- ISI MENU HOME ---
with tab1:
    st.markdown("### Halo! Selamat datang di website pribadiku. 👋")
    st.write("Silakan klik tab **Profile & Experience** di atas untuk melihat proyek-proyek teknik elektronika dan sistem kontrol yang pernah aku kerjakan.")")

# --- ISI MENU PROFILE ---
with tab2:
    st.markdown("### 🛠️ My Projects & Experience")
    st.write("Berikut adalah rekam jejak proyek yang pernah aku kembangkan:")

    # Menggunakan HTML khusus agar tampilan kotaknya sesuai dengan CSS di atas
    st.markdown("""
    <div class="kotak-pengalaman">
        <h4>🤖 Line Follower</h4>
        <p>Merakit dan memprogram robot otonom yang dapat mengikuti jalur atau garis lintasan secara presisi menggunakan pembacaan sensor inframerah.</p>
    </div>
    
    <div class="kotak-pengalaman">
        <h4>📟 Embedded System</h4>
        <p>Pengembangan sistem tersemat menggunakan mikrokontroler. Salah satu proyek utamaku adalah mendesain <b>Smart Lock System</b> menggunakan Arduino Uno (ATmega328P). Sistem ini dilengkapi dengan matriks Keypad untuk memasukkan kata sandi (menggunakan urutan kode spesifik 1, 2, 4, 7) dan layar LCD untuk menampilkan status penguncian pintu.</p>
    </div>
    
    <div class="kotak-pengalaman">
        <h4>🎛️ Instrumentasi</h4>
        <p>Berpengalaman dalam melakukan kalibrasi instrumen, pembacaan sinyal sensor, dan memastikan akurasi data pada berbagai alat ukur elektronika.</p>
    </div>
    
    <div class="kotak-pengalaman">
        <h4>⚙️ Sistem Control</h4>
        <p>Merancang logika kendali otomatis, seperti pembuatan <b>Sistem Irigasi Sekuensial</b> untuk lahan pertanian. Sistem ini dirancang untuk mendistribusikan air dari toren ke beberapa zona secara bergantian berdasarkan pembacaan sensor kelembapan tanah. Terdapat juga sistem pengaman otomatis di mana semua katup akan tertutup jika sensor mendeteksi turunnya hujan.</p>
    </div>
    
    <div class="kotak-pengalaman">
        <h4>🐍 Program Python</h4>
        <p>Menggunakan Python untuk pemrosesan logika, automasi tugas, hingga merancang antarmuka web interaktif berbasis data seperti website portofolio yang sedang kamu lihat saat ini.</p>
    </div>
    """, unsafe_allow_html=True)