# Arayüz stilleri ve ortak UI bileşenleri burada geliştirilecek.

import streamlit as st


def apply_style():
    st.markdown("""
    <style>

    :root {
        --bg: linear-gradient(135deg, #0f172a 0%, #111827 100%);
        --text: #f8fafc;
        --muted: #cbd5e1;
    }

    .stApp {
        background: var(--bg);
        color: var(--text);
    }

    .stApp,
    .stApp p,
    .stApp span,
    .stApp label,
    .stApp div {
        color: #f8fafc;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background: #0b1120 !important;
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] * {
        color: #f8fafc !important;
        opacity: 1 !important;
    }

    /* HERO */
    .hero-box {
        background: linear-gradient(135deg, #3b82f6, #8b5cf6, #ec4899);
        padding: 30px;
        border-radius: 24px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 35px rgba(0,0,0,0.4);
    }

    .hero-box * {
        color: white !important;
    }

    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 6px;
    }

    .subtitle {
        font-size: 1rem;
        opacity: 0.95;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 12px;
        color: #ffffff !important;
    }

    .input-label {
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 6px;
        margin-top: 10px;
        color: #e0f2fe !important;
    }

    /* CARDS */
    .metric-card,
    .day-card,
    .info-card,
    .meal-card {
        background: linear-gradient(145deg, #111827, #1f2937);
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.35);
        color: #f8fafc !important;
    }

    .metric-card {
        padding: 20px;
        text-align: center;
        transition: 0.2s;
    }

    .metric-card:hover {
        transform: translateY(-4px);
    }

    .metric-title {
        color: #e5e7eb !important;
        font-size: 0.9rem;
        margin-bottom: 8px;
    }

    .metric-value {
        font-size: 1.6rem;
        font-weight: 800;
        color: #ffffff !important;
    }

    .day-card {
        padding: 22px;
        line-height: 1.8;
        border-left: 6px solid #ec4899;
    }

    .info-card {
        padding: 18px;
        line-height: 1.7;
    }

    .meal-card {
        padding: 16px;
        margin-bottom: 10px;
    }

    .metric-card *,
    .day-card *,
    .info-card *,
    .meal-card * {
        color: #f8fafc !important;
    }

    /* BUTTON */
    div[data-testid="stButton"] > button {
        width: 100%;
        border-radius: 14px;
        border: none;
        padding: 13px;
        font-weight: 700;
        font-size: 0.95rem;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        color: white !important;
        transition: 0.2s;
    }

    div[data-testid="stButton"] > button:hover {
        transform: scale(1.02);
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        color: white !important;
    }

    /* INPUTS */
    input,
    textarea {
        background: #111827 !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.18) !important;
    }

    input::placeholder,
    textarea::placeholder {
        color: #d1d5db !important;
        opacity: 1 !important;
    }

    /* NUMBER INPUT BUTTON AREA */
    div[data-testid="stNumberInput"] button {
        background: #e5e7eb !important;
        color: #111827 !important;
    }

    div[data-testid="stNumberInput"] button * {
        color: #111827 !important;
    }

    /* SELECTBOX */
    div[data-baseweb="select"] > div {
        background: #111827 !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.18) !important;
    }

    div[data-baseweb="select"] * {
        color: #ffffff !important;
    }

    /* EXPANDER */
    .streamlit-expanderHeader {
        background: #111827 !important;
        border-radius: 12px;
        color: white !important;
        font-weight: 600;
    }

    .streamlit-expanderHeader * {
        color: white !important;
    }

    /* ALERT */
    div[data-testid="stAlert"] {
        border-radius: 14px;
    }

    /* CHATBOX */
    div[data-testid="stChatMessage"],
    div[data-testid="stChatMessage"] *,
    div[data-testid="stChatMessageContent"],
    div[data-testid="stChatMessageContent"] * {
        color: #f8fafc !important;
        opacity: 1 !important;
    }

    /* CHAT INPUT CONTAINER */
    div[data-testid="stChatInput"] {
        background: transparent !important;
    }

    div[data-testid="stChatInput"] > div {
        background: #111827 !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 18px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.35);
    }

    div[data-testid="stChatInput"] textarea {
        background: transparent !important;
        color: #ffffff !important;
        border: none !important;
    }

    div[data-testid="stChatInput"] textarea::placeholder {
        color: #e5e7eb !important;
        opacity: 1 !important;
    }

    div[data-testid="stChatInput"] button {
        background: linear-gradient(90deg, #3b82f6, #8b5cf6) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
    }

    div[data-testid="stChatInput"] button * {
        color: white !important;
    }

    /* RADIO */
    div[role="radiogroup"] label,
    div[role="radiogroup"] label * {
        color: #f8fafc !important;
        opacity: 1 !important;
    }

    /* MARKDOWN */
    [data-testid="stMarkdownContainer"],
    [data-testid="stMarkdownContainer"] * {
        color: #f8fafc !important;
        opacity: 1 !important;
    }

    /* SCROLLBAR */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-thumb {
        background: #64748b;
        border-radius: 10px;
    }
    /* CHAT ALT BEYAZ ALANI ZORLA KOYU YAP */
section[data-testid="stChatInput"] {
    background: #0f172a !important;
}

section[data-testid="stChatInput"] > div {
    background: #0f172a !important;
}

section[data-testid="stChatInput"] div {
    background-color: #0f172a !important;
}

/* CHAT INPUT YAZARKEN GÖRÜNÜR OLSUN */
section[data-testid="stChatInput"] textarea {
    background-color: #111827 !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    caret-color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    border-radius: 14px !important;
}

section[data-testid="stChatInput"] textarea::placeholder {
    color: #cbd5e1 !important;
    -webkit-text-fill-color: #cbd5e1 !important;
    opacity: 1 !important;
}

/* GÖNDER BUTONU */
section[data-testid="stChatInput"] button {
    background: linear-gradient(90deg, #3b82f6, #8b5cf6) !important;
    color: #ffffff !important;
    border-radius: 12px !important;
}

section[data-testid="stChatInput"] button * {
    color: #ffffff !important;
}
    </style>
    """, unsafe_allow_html=True)