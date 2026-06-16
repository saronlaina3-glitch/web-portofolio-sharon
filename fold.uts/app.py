import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Sharon | Portfolio", page_icon="🖤", layout="centered")

# 2. Desain Tema Colorful & Blackpink (CSS Custom)
st.markdown("""
<style>
    .stApp { background-color: #0d0d0d; color: #f8f9fa; }
    
    /* Judul dengan Gradient Warna */
    .gradient-text {
        background: -webkit-linear-gradient(45deg, #FF69B4, #FF1493, #8A2BE2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 3em;
    }
    
    /* Kotak Pengalaman dengan Border Warna-warni */
    .kotak-pengalaman {
        background: linear-gradient(145deg, #1a1a1a, #262626);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid transparent;
        border-left: 5px solid #FF69B4;
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .kotak-pengalaman:hover {
        border: 2px solid #FF1493;
        box-shadow: 0 0 15px rgba(255, 20, 147, 0.5);
    }
    
    .info-kontak {
        background: rgba(255, 105, 180, 0.1);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #FF69B4;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Header
st.markdown('<h1 class="gradient-text">Sharon | Engineering Portfolio</h1>', unsafe_allow_html=True)
st.markdown("---")

# 4. Navigasi
tab1, tab2 = st.tabs(["🏠 Home", "👩‍💻 Professional Profile"])

# --- ISI MENU HOME ---
with tab1:
    st.markdown("### Profile Overview")
    
    st.markdown("""
    <div class="info-kontak">
        📞 <b>Phone:</b> 082283924162 <br>
        📧 <b>Email:</b> sharon24trse@mahasiswa.pcr.ac.id <br>
        📍 <b>Address:</b> Jln. Rowosari, Rumbai, Pekanbaru
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    I am an active undergraduate student of Electronics Engineering Technology at Politeknik Caltex Riau. 
    My professional interests lie in electronics, control systems, Internet of Things (IoT), and automation technology. 
    Throughout my academic journey, I have been actively involved in various organizations, committees, and competitions.
    """)

# --- ISI MENU PROFILE ---
with tab2:
    st.markdown("### Technical Expertise & Projects")

    # Daftar Proyek dengan warna unik
    proyek = [
        ("🤖 Robotics: Line Follower", "Developed an autonomous robot using infrared arrays and closed-loop control algorithms."),
        ("📟 Embedded Systems: Smart Security", "Designed a smart door lock system using Arduino Uno, 4x4 keypad, and LCD display."),
        ("🎛️ Industrial Instrumentation", "Experienced in sensor calibration, signal acquisition, and data validation."),
        ("⚙️ Control Systems: Smart Irrigation", "Engineered an automated sequential irrigation system for agricultural lands."),
        ("🐍 Python Programming", "Proficient in Python for system logic automation, data processing, and web interfaces.")
    ]

    for title, desc in proyek:
        st.markdown(f'''
        <div class="kotak-pengalaman">
            <h4 style="color: #FFB6C1;">{title}</h4>
            <p>{desc}</p>
        </div>
        ''', unsafe_allow_html=True)