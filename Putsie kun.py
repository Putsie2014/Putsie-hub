import streamlit as st

# --- 1. CONFIGURATIE ---
st.set_page_config(page_title="Putsie Studios", layout="wide")

# --- 2. THE ULTIMATE PUTSIE DESIGN ---
st.markdown("""
<style>
    /* De bewegende achtergrond */
    .stApp {
        background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #00d2ff);
        background-size: 400% 400%;
        animation: gradient 10s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Titel Styling */
    .main-title {
        font-size: 70px !important;
        font-weight: 800;
        text-align: center;
        color: white;
        text-shadow: 0px 0px 20px #00d2ff;
        margin-bottom: 10px;
        animation: slideIn 1s ease-out;
    }

    /* De Transities */
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(-50px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Grote Knoppen (Cards) */
    .portal-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        transition: 0.4s;
        cursor: pointer;
        text-decoration: none;
        display: block;
        color: white !important;
    }
    .portal-card:hover {
        transform: scale(1.05);
        background: rgba(255, 255, 255, 0.2);
        box-shadow: 0px 0px 30px rgba(0, 210, 255, 0.5);
        border-color: #00d2ff;
    }

    .card-icon { font-size: 50px; margin-bottom: 15px; }
    .card-title { font-size: 28px; font-weight: bold; margin-bottom: 10px; }
    .card-desc { font-size: 16px; opacity: 0.8; }

</style>
""", unsafe_allow_html=True)

# --- 3. DE CONTENT ---
st.markdown('<h1 class="main-title">PUTSIE Studios 🌎</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:white; font-size:20px; margin-bottom:50px;">Welkom in het universum van Elliot. Kies je bestemming.</p>', unsafe_allow_html=True)

# Maak kolommen voor je verschillende "apps"
col1, col2, col3 = st.columns(3)

with col1:
    # HIER MOET DE URL VAN JE EDUCATION APP KOMEN
    # Als je hem op Streamlit Cloud hebt gezet, plak je die link hier:
    edu_url = "https://putsieeducation.streamlit.app"
    
    st.markdown(f"""
        <a href="{edu_url}" target="_self" class="portal-card">
            <div class="card-icon">🎓</div>
            <div class="card-title">Putsie EDUCATION</div>
            <div class="card-desc">Frans leren, chatten met de AI leraar en munten verdienen.</div>
        </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="portal-card" style="opacity: 0.6; cursor: not-allowed;">
            <div class="card-icon">🎮</div>
            <div class="card-title">Putsie GAMES</div>
            <div class="card-desc">Binnenkort beschikbaar: De vetste games van de klas.</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="portal-card" style="opacity: 0.6; cursor: not-allowed;">
            <div class="card-icon">📱</div>
            <div class="card-title">Putsie SOCIAL</div>
            <div class="card-desc">Binnenkort beschikbaar: Jouw eigen klas-social media.</div>
        </div>
    """, unsafe_allow_html=True)

# --- 4. FOOTER ---
st.write("---")
st.markdown('<p style="text-align:center; color:gray;">© 2024 Putsie Company - Built by Elliot and Olive</p>', unsafe_allow_html=True)
