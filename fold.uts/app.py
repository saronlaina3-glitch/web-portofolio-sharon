import streamlit as st

# 1. Pengaturan Dasar Halaman
st.set_page_config(page_title="Sharon - Portfolio", page_icon="🖤", layout="centered")

# 2. Desain Tema Blackpink Profesional (CSS Custom)
st.markdown("""
<style>
    /* Mengubah warna background utama menjadi hitam elegan */
    .stApp {
        background-color: #0d0d0d;
        color: #f8f9fa;
    }
    
    /* Menggunakan font profesional */
    h1, h2, h3, h4 {
        color: #ff69b4 !important; 
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* Warna Tab yang lebih tenang */
    .stTabs [data-baseweb="tab"] {
        color: #888888; 
    }
    .stTabs [aria-selected="true"] {
        color: #ff69b4 !important;
        border-bottom-color: #ff69b4 !important;
    }

    /* Desain kartu proyek yang bersih */
    .kotak-pengalaman {
        background-color: #1a1a1a;
        padding: 25px;
        border-radius: 10px;
        border-left: 4px solid #ff69b4;
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .kotak-pengalaman:hover {
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# 3. Bagian Header
st.title("Sharon | Engineering Portfolio")
st.markdown("---")

# 4. Navigasi
tab1, tab2 = st.tabs(["🏠 Home", "👩‍💻 Professional Profile"])

# --- ISI MENU HOME ---
with tab1:
    st.markdown("### Profile Overview")
    st.write("""
    Selamat datang di portofolio profesional saya. 
    Laman ini merangkum keahlian teknis dan pengalaman saya di bidang Teknik Elektro dan Sistem Kontrol. 
    Fokus saya adalah pada pengembangan sistem cerdas, otomasi, dan efisiensi sistem berbasis mikrokontroler.
    """)

# --- ISI MENU PROFILE ---
with tab2:
    st.markdown("### Technical Expertise & Projects")

    st.markdown("""
    <div class="kotak-pengalaman">
        <h4>🤖 Robotics: Line Follower</h4>
        <p>Pengembangan robot otonom dengan algoritma kontrol presisi untuk navigasi lintasan menggunakan sensor inframerah.</p>
    </div>
    
    <div class="kotak-pengalaman">
        <h4>📟 Embedded Systems: Smart Security</h4>
        <p>Perancangan sistem akses keamanan pintu berbasis Arduino Uno, meliputi antarmuka Keypad (matriks 4x4) dan verifikasi kata sandi sekuensial.</p>
    </div>
    
    <div class="kotak-pengalaman">
        <h4>🎛️ Industrial Instrumentation</h4>
        <p>Implementasi kalibrasi sensor dan akuisisi data elektronika untuk meningkatkan akurasi pembacaan parameter fisik.</p>
    </div>
    
    <div class="kotak-pengalaman">
        <h4>⚙️ Control Systems: Smart Irrigation</h4>
        <p>Perancangan sistem kontrol otomatis berbasis kelembapan tanah untuk manajemen air lahan pertanian secara sekuensial dan efisien.</p>
    </div>
    
    <div class="kotak-pengalaman">
        <h4>🐍 Python Programming</h4>
        <p>Pemanfaatan Python untuk automasi logika sistem, pemrosesan data, serta pengembangan antarmuka web interaktif (seperti portofolio ini).</p>
    </div>
    """, unsafe_allow_html=True)