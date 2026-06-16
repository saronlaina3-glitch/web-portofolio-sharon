import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Sharon | Portfolio", page_icon="🖤", layout="centered")

# 2. Desain Tema Blackpink Profesional
st.markdown("""
<style>
    .stApp { background-color: #0d0d0d; color: #f8f9fa; }
    h1, h2, h3, h4 { color: #ff69b4 !important; font-family: sans-serif; }
    .kotak-pengalaman {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #ff69b4;
        margin-bottom: 15px;
    }
    .info-kontak {
        background-color: #262626;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Header
st.title("Sharon | Engineering Portfolio")
st.markdown("---")

# 4. Navigasi
tab1, tab2 = st.tabs(["🏠 Home", "👩‍💻 Professional Profile"])

# --- ISI MENU HOME ---
with tab1:
    st.markdown("### Profile Overview")
    
    # Bagian Data Kontak
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
    Throughout my academic journey, I have been actively involved in various organizations, committees, and competitions, 
    which have significantly enhanced my leadership, communication, teamwork, and problem-solving skills.
    """)

# --- ISI MENU PROFILE ---
with tab2:
    st.markdown("### Technical Expertise & Projects")

    st.markdown("""
    <div class="kotak-pengalaman">
        <h4>🤖 Robotics: Line Follower</h4>
        <p>Developed an autonomous robot capable of precise path navigation using infrared sensor arrays and closed-loop control algorithms.</p>
    </div>
    
    <div class="kotak-pengalaman">
        <h4>📟 Embedded Systems: Smart Security</h4>
        <p>Designed a smart door lock system using Arduino Uno, integrated with a 4x4 matrix keypad for sequential password authentication and LCD status display.</p>
    </div>
    
    <div class="kotak-pengalaman">
        <h4>🎛️ Industrial Instrumentation</h4>
        <p>Experienced in sensor calibration, signal acquisition, and data validation to ensure high accuracy in electronic measurement systems.</p>
    </div>
    
    <div class="kotak-pengalaman">
        <h4>⚙️ Control Systems: Smart Irrigation</h4>
        <p>Engineered an automated sequential irrigation system for agricultural lands, utilizing soil moisture sensors to optimize water distribution efficiency.</p>
    </div>
    
    <div class="kotak-pengalaman">
        <h4>🐍 Python Programming</h4>
        <p>Proficient in using Python for system logic automation, data processing, and developing interactive web-based interfaces and technical portfolios.</p>
    </div>
    """, unsafe_allow_html=True)