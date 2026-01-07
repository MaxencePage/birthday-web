import streamlit as st
import json
import os

# ========================================
# PAGE CONFIGURATION
# ========================================
st.set_page_config(
    page_title="For Mon Ciel ♡",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========================================
# CSS INJECTION (Themes & Styles)
# ========================================
def inject_custom_css():
    st.markdown("""
    <style>
    /* Special badge di tengah atas foto */
    .special-badge-box {
        position: absolute;
        left: 50%;
        top: -22px;
        transform: translateX(-50%);
        background: #fffbe9;
        color: #8E24AA;
        border: 2.5px solid #BA68C8;
        border-radius: 16px;
        font-weight: 700;
        font-size: 1.08rem;
        box-shadow: 0 2px 12px #BA68C855;
        padding: 6px 18px;
        text-align: center;
        letter-spacing: 0.5px;
        z-index: 2;
        margin-top: 20px;
    }
    
    /* Date badge di akhir */
    .date-badge-box {
        background: #fffbe9;
        color: #8E24AA;
        border: 2.5px solid #BA68C8;
        border-radius: 16px;
        font-weight: 700;
        font-size: 1.15rem;
        box-shadow: 0 4px 16px #BA68C855;
        padding: 10px 25px;
        text-align: center;
        letter-spacing: 0.5px;
        display: inline-block;
        margin: 0 auto;
    }
    
    /* Border untuk semua gambar galeri */
    .stImage img {
        border: 2.5px solid #E1BEE7;
        border-radius: 14px;
        box-shadow: 0 2px 10px #BA68C822;
        background: #fff;
        padding: 2px;
    }
    /* Glowing border untuk foto utama */
    .highlighted-photo-glow {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto 18px auto;
        width: fit-content;
    }
    .highlighted-photo-glow img {
        border: 5px solid #BA68C8;
        border-radius: 20px;
        box-shadow: 0 0 32px 8px #BA68C8, 0 0 80px 0 #fffbe9;
        background: #fff;
        max-width: 350px;
        width: 100%;
        height: auto;
        display: block;
        margin: 0 auto;
        z-index: 1;
    }
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Quicksand:wght@400;500;600&display=swap');
    
    /* Hide Streamlit Default Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Global Styling */
    .stApp {
        background: linear-gradient(135deg, #E0BBE4 0%, #D4A5D8 25%, #E8D5F2 50%, #F5F0FA 75%, #FFFFFF 100%);
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Animated Background */
    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .stApp {
        background-size: 200% 200%;
        animation: gradient-shift 15s ease infinite;
    }
    
    /* Glassmorphism Card Style */
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        padding: 40px;
        box-shadow: 0 8px 32px rgba(138, 43, 226, 0.15);
        text-align: center;
        max-width: 300px;
        margin: 0 auto;
    }
    
    /* iOS Message Bubble */
    .message-bubble {
        background: rgba(255, 255, 255, 0.45);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 30px;
        margin: 0 auto 25px auto;
        max-width: 450px;
        border: 1.5px solid rgba(186, 104, 200, 0.3);
        box-shadow: 0 10px 40px rgba(138, 43, 226, 0.2);
    }
    
    .message-header {
        font-size: 0.85rem;
        color: #7B2CBF;
        font-weight: 600;
        margin-bottom: 10px;
        font-family: 'Quicksand', sans-serif;
        border-bottom: 1px solid rgba(123, 44, 191, 0.1);
        padding-bottom: 8px;
    }
    
    .message-text {
        font-size: 1.1rem;
        color: #4A148C;
        line-height: 1.6;
        margin: 15px 0;
    }
    
    /* Custom Button Styling */
    .stButton {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
    }
    
    div[class*="st-emotion-cache"] .stButton {
        align-items: center !important;
    }
    
    .stButton, [class*="st-emotion-cache"] {
        align-items: center !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #BA68C8 0%, #9C27B0 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 15px 40px;
        font-size: 1.1rem;
        font-weight: 600;
        font-family: 'Quicksand', sans-serif;
        box-shadow: 0 6px 20px rgba(156, 39, 176, 0.4);
        transition: all 0.3s ease;
        cursor: pointer;
        display: block !important;
        width: fit-content !important;
        margin: 0 auto !important;
        padding: 15px 40px !important;
        height: auto !important;
        min-height: auto !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(156, 39, 176, 0.6);
        background: linear-gradient(135deg, #AB47BC 0%, #8E24AA 100%);
        border-color: white;
    }
    
    /* Hero Section */
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        color: #6A1B9A;
        margin-bottom: 10px;
        text-align: center;
        font-family: 'Poppins', sans-serif;
        text-shadow: 2px 2px 8px rgba(138, 43, 226, 0.2);
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: #8E24AA;
        text-align: center;
        margin-bottom: 40px;
        font-family: 'Quicksand', sans-serif;
        font-weight: 500;
    }
    
    /* Warranty Status Badge */
    .warranty-badge {
        background: linear-gradient(135deg, #E1BEE7 0%, #CE93D8 100%);
        color: #4A148C;
        padding: 12px 25px;
        border-radius: 50px;
        font-size: 0.95rem;
        font-weight: 600;
        text-align: center;
        margin: 30px auto;
        max-width: fit-content;
        box-shadow: 0 4px 15px rgba(138, 43, 226, 0.25);
    }
    
    /* Warranty Card */
    .warranty-card {
        background: rgba(255, 255, 255, 0.35);
        backdrop-filter: blur(10px);
        border-radius: 18px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 6px 25px rgba(138, 43, 226, 0.15);
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .warranty-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(138, 43, 226, 0.3);
    }
    
    .warranty-icon {
        font-size: 3rem;
        margin-bottom: 15px;
    }
    
    .warranty-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #6A1B9A;
        margin-bottom: 10px;
    }
    
    .warranty-desc {
        font-size: 0.95rem;
        color: #7B2CBF;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    
    /* Button Wrapper */
    .button-wrapper {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
        margin-top: 15px !important;
    }
    
    .button-wrapper .stButton {
        width: fit-content !important;
        flex: 0 0 auto !important;
        justify-content: center !important;
    }
    
    .button-wrapper .stButton > button {
        width: fit-content !important;
        display: block !important;
    }
    
    /* Success Message */
    .success-message {
        background: linear-gradient(135deg, #C8E6C9 0%, #A5D6A7 100%);
        color: #1B5E20;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        margin-top: auto;
        margin-bottom: 25px;
        animation: fadeIn 0.5s ease;
    }
    
    /* Photo Gallery */
    .gallery-container {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 40px;
        margin: 40px auto;
        max-width: 700px;
        box-shadow: 0 8px 32px rgba(138, 43, 226, 0.15);
    }
    
    .gallery-title {
        font-size: 2rem;
        font-weight: 700;
        color: #6A1B9A;
        text-align: center;
        font-family: 'Poppins', sans-serif;
    }
    
    .gallery-image-wrapper {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 10px 40px rgba(138, 43, 226, 0.2);
        margin-bottom: 20px;
    }
    
    .gallery-caption {
        text-align: center;
        color: #6A1B9A;
        font-size: 1rem;
        font-weight: 600;
        font-family: 'Quicksand', sans-serif;
        margin-bottom: 20px;
        padding: 10px;
    }
    
    .gallery-counter {
        text-align: center;
        color: #8E24AA;
        font-size: 0.9rem;
        margin-bottom: 15px;
        font-family: 'Quicksand', sans-serif;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* BACK TO TOP BUTTON - ALWAYS VISIBLE */
    .floating-back-to-top {
        position: fixed !important;
        bottom: 60px !important;
        right: 30px !important;
        width: 56px !important;
        height: 56px !important;
        background: linear-gradient(135deg, #BA68C8 0%, #9C27B0 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 50% !important;
        font-size: 28px !important;
        line-height: 56px !important;
        text-align: center !important;
        cursor: pointer !important;
        box-shadow: 0 6px 20px rgba(156, 39, 176, 0.5) !important;
        transition: all 0.3s ease !important;
        z-index: 999999 !important;
        display: block !important;
        text-decoration: none !important;
        font-weight: bold !important;
    }
    
      .floating-back-to-top:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px rgba(156, 39, 176, 0.7) !important;
        background: linear-gradient(135deg, #AB47BC 0%, #8E24AA 100%) !important;
    }
    
    .floating-back-to-top:active {
        transform: translateY(0) !important;
    }
    
    /* Responsive Design */
    @media (max-width: 600px) {
        .glass-card, .message-bubble {
            width: 90%;
            padding: 25px;
        }
        
        .hero-title { font-size: 2rem; }
        .hero-subtitle { font-size: 1rem; }
        .warranty-card { margin-bottom: 20px; }
        .stButton > button { padding: 12px 30px; font-size: 1rem; }
        
        .floating-back-to-top {
            bottom: 60px !important;
            right: 20px !important;
            width: 50px !important;
            height: 50px !important;
            font-size: 24px !important;
            line-height: 50px !important;
        }
    }
                
    /* CUSTOM EXPANDER STYLING */
    /* Kotak luar expander */
    [data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.45);
        backdrop-filter: blur(10px);
        border: 1.5px solid #BA68C8; /* Warna border ungu */
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(138, 43, 226, 0.1);
        overflow: hidden; /* Supaya radius tidak bocor */
    }
    
    /* Header (Bagian yang diklik) */
    .streamlit-expanderHeader {
        font-family: 'Quicksand', sans-serif;
        font-weight: 600;
        color: #6A1B9A; /* Ungu gelap */
        background-color: rgba(255, 255, 255, 0.2);
        border-bottom: 1px solid rgba(186, 104, 200, 0.2);
    }
    
    /* Isi Text di dalam */
    [data-testid="stExpanderDetails"] {
        color: #4A148C;
        font-family: 'Poppins', sans-serif;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Icon panah kecil */
    .streamlit-expanderHeader svg {
        fill: #6A1B9A !important; /* Warna panah */
    }
                
    /* ========================================= */
    /* GAYA KHUSUS EXPANDER (VERSI FINAL ANTI-HITAM) */
    /* ========================================= */
    
    /* 1. Styling Judul (Header) - MENANGANI SEMUA KONDISI KLIK */
    .streamlit-expanderHeader, 
    div[data-testid="stExpander"] summary,
    div[data-testid="stExpander"] summary:hover,
    div[data-testid="stExpander"] summary:focus,
    div[data-testid="stExpander"] summary:active,
    div[data-testid="stExpander"] details[open] summary {
        color: #4A148C !important;  /* Tetap Ungu Gelap, JANGAN berubah hitam */
        font-family: 'Quicksand', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding-left: 10px !important;
        background-color: transparent !important; /* Hilangkan highlight abu-abu saat klik */
    }

    /* 2. HILANGKAN Panah Bawaan (Biar tidak error jadi teks) */
    div[data-testid="stExpander"] summary svg,
    .streamlit-expanderHeader svg {
        display: none !important;
    }

    /* 3. Styling Kotak Luar */
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.45) !important;
        border: 2px solid #BA68C8 !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 12px rgba(138, 43, 226, 0.15) !important;
    }

    /* 4. Styling Isi Teks (Konten di dalam) */
    div[data-testid="stExpanderDetails"] {
        color: #333 !important; /* Warna teks isi (Hitam/Abu) */
        border-top: 1px solid rgba(186, 104, 200, 0.3);
        padding-top: 10px !important;
    }
                
    /* ========================================= */
    /* GAYA KHUSUS TOMBOL LINK (External Link)   */
    /* ========================================= */
    .link-card-container {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(10px);
        border: 2px solid #BA68C8;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        max-width: 500px;
        margin: 20px auto;
        box-shadow: 0 8px 32px rgba(138, 43, 226, 0.15);
        transition: transform 0.3s ease;
    }

    /* Tombol Link Custom */
    .custom-link-btn {
        background: linear-gradient(135deg, #BA68C8 0%, #9C27B0 100%);
        color: white !important; /* Paksa putih */
        text-decoration: none !important; /* Hilangkan garis bawah */
        border-radius: 50px;
        padding: 15px 40px;
        font-size: 1.1rem;
        font-weight: 600;
        font-family: 'Quicksand', sans-serif;
        box-shadow: 0 6px 20px rgba(156, 39, 176, 0.4);
        display: inline-block;
        margin-top: 15px;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }

    .custom-link-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(156, 39, 176, 0.6);
        background: linear-gradient(135deg, #AB47BC 0%, #8E24AA 100%);
        border: 2px solid white;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ========================================
# STATE MANAGEMENT
# ========================================
if 'page' not in st.session_state:
    st.session_state.page = 'intro'

if 'claimed_warranties' not in st.session_state:
    st.session_state.claimed_warranties = []

# ========================================
# MEDIA LOADING FUNCTION (WITH CACHING)
# ========================================
@st.cache_data
def load_media_config():
    """Load media URLs from config file with caching"""
    try:
        config_path = os.path.join(os.path.dirname(__file__), 'media_config.json')
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config.get('media', [])
    except FileNotFoundError:
        # Fallback jika config belum ada
        return [
            {'type': 'image', 'url': 'https://via.placeholder.com/600x400?text=Memories+1'},
            {'type': 'image', 'url': 'https://via.placeholder.com/600x400?text=Memories+2'},
            {'type': 'image', 'url': 'https://via.placeholder.com/600x400?text=Memories+3'},
        ]

# ========================================
# STATE 1: THE INCOMING MESSAGE (INTRO)
# ========================================
def show_intro_page():
    # CSS HACK UTK TENGAH LAYAR
    st.markdown("""
    <style>
    div[data-testid="stAppViewContainer"] > .main > .block-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        padding-top: 0rem;
        padding-bottom: 0rem;
        max-width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

    # Message Bubble Container
    st.markdown("""
    <div class="message-bubble">
        <div class="message-header">
            📱 Pesan Baru<br>
            <strong>Dari:</strong> Mon Chéri<br>
            <strong>Untuk:</strong> Mon Ciel ♡
        </div>
        <div class="message-text">
            ✨ Ada kiriman paket garansi untuk tahun 2026<br>
            Khusus untuk seseorang yang special 💜
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Center button Logic
    col1, col2, col3 = st.columns([1, 2, 1])
    if 'loading_open_message' not in st.session_state:
        st.session_state.loading_open_message = False

    with col2:
        if not st.session_state.loading_open_message:
            if st.button("Buka Pesan 💌"):
                st.session_state.loading_open_message = True
                st.rerun()
        elif st.session_state.loading_open_message:
            with st.spinner('Membuka pesan spesial...'):
                import time
                time.sleep(1.5)
            st.session_state.page = 'main'
            st.session_state.loading_open_message = False
            st.rerun()

# ========================================
# STATE 2: THE CELEBRATION & WARRANTY
# ========================================
def show_main_page():
    # Background music setup
    if 'music_playing' not in st.session_state:
        st.session_state.music_playing = True

    # Audio player (autoplay)
    try:
        audio_file = open('music.mp3', 'rb')
        import base64
        audio_base64 = base64.b64encode(audio_file.read()).decode()
        audio_html = f'''
        <audio id="hidden-audio" src="data:audio/mp3;base64,{audio_base64}" {'autoplay' if st.session_state.music_playing else ''} loop style="display:none;"></audio>
        <script>
        var audio = document.getElementById('hidden-audio');
        if (audio) {{
            {'audio.play();' if st.session_state.music_playing else 'audio.pause();'}
        }}
        </script>
        '''
        st.markdown(audio_html, unsafe_allow_html=True)
    except:
        pass  # Skip if music file not found

    # Reset layout CSS untuk main page
    st.markdown("""
    <style>
    div[data-testid="stAppViewContainer"] > .main > .block-container {
        display: block;
        padding-top: 5rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # BACK TO TOP BUTTON - INJECT DI AWAL
    st.markdown("""
    <a href="#top" class="floating-back-to-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;">↑</a>
    <div id="top"></div>
    """, unsafe_allow_html=True)

    # Trigger balloons on first load
    if 'balloons_shown' not in st.session_state:
        st.balloons()
        st.session_state.balloons_shown = True
    
    # Hero Section
    st.markdown("""
    <div class="hero-title">
        Happy Birthday, <br>Febe Grace. 🎂
    </div>
    <div class="hero-subtitle">
        Semoga 15 Februari ini seindah warna Lilac kesukaanmu.
    </div>
    """, unsafe_allow_html=True)
    
    # Warranty Status Badge
    st.markdown("""
    <div class="warranty-badge">
        ✅ Status: Active Lifetime • Authorized by Mon Chéri
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Warranty Cards
    st.markdown("<h2 style='text-align: center; color: #6A1B9A; font-family: Poppins;'>💝 Premium Friendship Warranty</h2>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    warranties = [
        {
            'icon': '🎧',
            'title': 'Listening Ear',
            'description': 'Untuk curhat kapanpun, 24/7 available.',
            'key': 'listening'
        },
        {
            'icon': '🍜',
            'title': 'Bakso Buddy',
            'description': 'Siap nemenin makan bakso kapan aja!',
            'key': 'bakso'
        },
        {
            'icon': '🛠️',
            'title': 'Tech & Life Support',
            'description': 'Bantuan teknis dan support kehidupan.',
            'key': 'support'
        },
        {
            'icon': '🎬',
            'title': 'Watch Buddy',
            'description': 'Nonton bareng film/series favorit.',
            'key': 'watch'
        }
    ]
    
    columns = [col1, col2, col3, col4]
    
    for idx, warranty in enumerate(warranties):
        with columns[idx]:
            st.markdown(f"""
            <div class="warranty-card">
                <div class="warranty-icon">{warranty['icon']}</div>
                <div class="warranty-title">{warranty['title']}</div>
                <div class="warranty-desc">{warranty['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown('<div class="button-wrapper">', unsafe_allow_html=True)
            button_key = f"claim_{warranty['key']}"
            
            # Cek apakah sudah diklaim
            is_claimed = warranty['key'] in st.session_state.claimed_warranties
            
            if st.button("Klaim Garansi" if not is_claimed else "Terima Kasih", key=button_key, disabled=is_claimed):
                st.session_state.claimed_warranties = [warranty['key']]
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            
            if is_claimed:
                st.markdown("""
                <div class="success-message">
                    ✅ Klaim Berhasil!<br>
                    Screenshot kartu ini dan kirim ke Mon chéri untuk redeem.
                </div>
                """, unsafe_allow_html=True)
    
    # ========================================
    # PHOTO GALLERY / MEMORIES SECTION
    # ========================================
    st.markdown("<br>", unsafe_allow_html=True)

    # Footer Message langsung tampil di atas galeri
    st.markdown("""
    <div style="
        text-align: center; 
        color: #6A1B9A; 
        font-size: 1.1rem; 
        font-family: 'Quicksand', sans-serif;
        font-weight: 500;
        line-height: 1.8;
        padding: 30px 25px;
        margin-bottom: 30px;
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 8px 32px rgba(138, 43, 226, 0.15);
        border: 1px solid rgba(186, 104, 200, 0.3);
    ">
        <em style="color: #8E24AA;">"Meskipun sudah bukan pasangan, kamu tetap seseorang yang special.<br>
        Selamat ulang tahun, Mon Ciel. Semoga tahun ini penuh kebahagiaan!"</em><br>
        <strong style="color: #6A1B9A; font-size: 1.15rem; margin-top: 10px; display: inline-block;">— Mon Chéri 💜</strong>
    </div>
    """, unsafe_allow_html=True)

    # Load media dari config (JSON)
    media_list = load_media_config()
    st.markdown("""
    <div class="gallery-container">
        <div class="gallery-title">📸 Our Memories</div>
    </div>
    """, unsafe_allow_html=True)

    if not media_list:
        st.warning("Belum ada media. Update media_config.json dengan foto/video URLs.")
    else:
        # Ambil hanya gambar (skip video untuk layout ini)
        images = [m['url'] for m in media_list if m['type'] == 'image']
        
        # Foto yang ingin di-highlight
        highlight_url = None
        for img in images:
            if 'Images/IMG_20250621_181933.jpg' in img or 'IMG_20250621_181933.jpg' in img:
                highlight_url = img
                break
        
        # Jika tidak ditemukan, fallback ke index 5 atau placeholder
        if not highlight_url:
            highlight_url = images[5] if len(images) > 5 else 'https://via.placeholder.com/350x500?text=Special'
        
        # Buat list images_lain tanpa yang di-highlight
        images_lain = [img for img in images if img != highlight_url]
        
        # Pastikan jumlah images_lain minimal 11
        while len(images_lain) < 11:
            images_lain.append('https://via.placeholder.com/400x500?text=Photo')

        # Tukar posisi foto 1 dan foto 2 (index 0 dan 1)
        if len(images_lain) >= 2:
            images_lain[0], images_lain[1] = images_lain[1], images_lain[0]

        # Layout: 12 foto, 1 utama di tengah, 11 mengelilingi
        # Baris 1: 3 foto, semua 340px
        cols = st.columns([1,1,1])
        for i in range(3):
            with cols[i]:
                st.image(images_lain[i], width=340)

        # Baris 2: 2 foto 340px, 1 besar di tengah (highlight 400px), 2 foto 340px
        cols = st.columns([1,1,2,1,1])
        with cols[0]:
            st.image(images_lain[3], width=340)
        with cols[1]:
            st.image(images_lain[4], width=340)
        with cols[2]:
            st.markdown('<div class="special-badge-box">✨ Special ✨</div>', unsafe_allow_html=True)
            st.image(highlight_url, width=400)
        with cols[3]:
            st.image(images_lain[5], width=340)
        with cols[4]:
            st.image(images_lain[6], width=340)

        # Baris 3: 3 foto 340px
        cols = st.columns([1,1,1])
        for i in range(7,10):
            with cols[i-7]:
                st.image(images_lain[i], width=340)

        # Baris 4: 1 foto 340px di tengah bawah
        cols = st.columns([3,1,3])
        with cols[1]:
            st.image(images_lain[10], width=340)

        # Jika ada video, tampilkan di bawah galeri
        videos = [m['url'] for m in media_list if m['type'] == 'video']
        if videos:
            st.markdown('<br><b>Video Kenangan</b>', unsafe_allow_html=True)
            for v in videos:
                st.video(v)
   
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col_x1, col_x2, col_x3 = st.columns([1, 1, 1])
    
    with col_x2:
        with st.expander("💌 P.S. Klik untuk membuka pesan"):
            st.markdown("""
            <div style="text-align: justify; color: #4A148C; padding: 10px; max-width: 700px;">
            <b>Dear Febe,</b>
            <br><br>
            <b>I love you.</b><br>
            I love you more than anything.<br>
            I love you more than myself.<br>
            I will always love you.<br>
            I will love you till the end of my time.<br>
            No words can express how much I love you.<br>
            I will always be here for you no matter what.<br>
            I will stay.
            <br><br>
            <b>I miss you.</b><br>
            I miss you more than I can put into words.<br>
            I miss our talks, your stories,<br>
            and everything in between.<br>
            No matter how much time passes,<br>
            a part of me will always miss you.<br>
            I'm still here, and I'll always be.
            <br><br>
            <b>Always, Mon Chéri.</b>
            </div>
            """, unsafe_allow_html=True)

    # 1. Tentukan Link dan Teks
    target_url = "https://gumpalan-story.streamlit.app/" # Ganti link ini
    button_text = "📖 Baca Ceritamu"
    card_title = "🌙 The Dream You Once Shared"
    card_desc = "Apakah kamu masih ingat, <br>" \
                "mimpi yang pernah kamu ceritakan itu?<br>" \
                "Aku mencoba menangkap kepingan-kepingan ceritamu dan menyusunnya kembali menjadi sebuah kisah abadi. <br>" \
                "Selamat membaca imajinasiku tentang mimpimu. <br>  " \
                "Anggap saja ini oleh-oleh dari alam bawah sadarmu."

    # 2. Render HTML Card
    st.markdown(f"""
    <div class="link-card-container">
        <div style="font-size: 3rem; margin-bottom: 10px;">🎁</div>
        <div style="
            font-size: 1.5rem; 
            font-weight: 700; 
            color: #6A1B9A; 
            font-family: 'Poppins', sans-serif;
            margin-bottom: 10px;
        ">
            {card_title}
        </div>
        <div style="
            font-size: 1rem; 
            color: #4A148C; 
            margin-bottom: 25px; 
            line-height: 1.5;
        ">
            {card_desc}
        </div>
        <a href="{target_url}" target="_blank" class="custom-link-btn">
            {button_text} ➜
        </a>
    </div>
    """, unsafe_allow_html=True)
                    
    # ========================================
    # FINAL MESSAGE WITH LOVE
    # ========================================
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        text-align: center; 
        color: #6A1B9A; 
        font-size: 1.15rem; 
        font-family: 'Quicksand', sans-serif;
        font-weight: 500;
        line-height: 1.8;
        padding: 40px 20px;
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        max-width: 700px;
        margin: 0 auto 60px auto;
        box-shadow: 0 8px 32px rgba(138, 43, 226, 0.15);
        border: 1px solid rgba(186, 104, 200, 0.3);
    ">
        <div style="font-style: italic; margin-bottom: 20px;">
            "Made with the deepest love.<br>
            Loved you yesterday, loving you still,<br>
            always have, always will.<br>
            My door and my heart remain open.<br>
            Forever and ever."
        </div>
        <div style="font-size: 2.5rem; margin-top: 15px; animation: heartbeat 1.5s ease-in-out infinite;">
            💜
        </div>
    </div>
    
    <style>
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        25% { transform: scale(1.1); }
        50% { transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # ========================================
    # DATE BADGE - TAMBAHAN BARU
    # ========================================
    st.markdown("""
    <div style="text-align: center; margin: 40px auto 80px auto;">
        <div class="date-badge-box">
            ✨ 05.07.25 ✨
        </div>
    </div>
    """, unsafe_allow_html=True)

# ========================================
# MAIN APPLICATION
# ========================================
def main():
    inject_custom_css()
    
    if st.session_state.page == 'intro':
        show_intro_page()
    elif st.session_state.page == 'main':
        show_main_page()

if __name__ == "__main__":
    main()