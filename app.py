import datetime
import streamlit as st
from openai import OpenAI

from database import (
    create_tables,
    save_user_profile,
    get_user_profile,
    add_weight,
    get_last_weight,
    save_daily_log,
    get_last_daily_log,
    save_meal_log,
    get_today_meals,
    get_weight_history
)
from auth import register_user, login_user
from diet import (
    bmi_hesapla,
    bmi_durumu,
    kalori_hesapla,
    makro_stratejisi,
    haftalik_plan,
    filtrele_ogunler
)
from meals import ogun_onerisi
from exercise import egzersiz_onerisi, adim_kalorisi
from tracking import gunluk_puanla, su_uyarisi, uyku_uyarisi
from ui import apply_style


# db hazırla
create_tables()

# sayfa ayarı
st.set_page_config(page_title="Diyet Asistanı", page_icon="🥗", layout="wide")
apply_style()


# session
if "login" not in st.session_state:
    st.session_state.login = False
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "username" not in st.session_state:
    st.session_state.username = None


# giriş / kayıt
if not st.session_state.login:
    st.markdown("""
    <div class="hero-box">
        <div class="main-title">🔐 Giriş / Kayıt</div>
        <div class="subtitle">Sistemi kullanmak için giriş yap veya yeni hesap oluştur.</div>
    </div>
    """, unsafe_allow_html=True)

    secim = st.radio("Seçim", ["Giriş", "Kayıt"], horizontal=True)

    if secim == "Kayıt":
        u = st.text_input("Kullanıcı adı", key="reg_user")
        p = st.text_input("Şifre", type="password", key="reg_pass")

        if st.button("Kayıt Ol"):
            ok, msg = register_user(u, p)
            if ok:
                st.success(msg)
            else:
                st.error(msg)

    else:
        u = st.text_input("Kullanıcı adı", key="log_user")
        p = st.text_input("Şifre", type="password", key="log_pass")

        if st.button("Giriş Yap"):
            user = login_user(u, p)
            if user:
                st.session_state.login = True
                st.session_state.user_id = user[0]
                st.session_state.username = user[1]
                st.rerun()
            else:
                st.error("Kullanıcı adı veya şifre hatalı.")

    st.stop()


# ortak veriler
st.sidebar.title("Menü")
sayfa = st.sidebar.radio(
    "Sayfa",
    ["Dashboard", "Profil", "Diyet Planı", "Egzersiz Planı", "Günlük Takip"]
)

st.sidebar.success(f"Giriş yapan: {st.session_state.username}")

if st.sidebar.button("Çıkış Yap"):
    st.session_state.login = False
    st.session_state.user_id = None
    st.session_state.username = None
    st.rerun()

profil = get_user_profile(st.session_state.user_id)
son_kilo = get_last_weight(st.session_state.user_id)
son_gunluk = get_last_daily_log(st.session_state.user_id)
bugun = str(datetime.date.today())


# dashboard
if sayfa == "Dashboard":

    st.markdown("""
    <div class="hero-box">
        <div class="main-title">Dashboard</div>
        <div class="subtitle">Günlük özet ve kişisel plan</div>
    </div>
    """, unsafe_allow_html=True)
       

    # --- ÜST METRİKLER ---
    col1, col2, col3 = st.columns(3)

# --- KİLO ---
    with col1:
     st.markdown(f"""
    <div class="metric-card" style="border-left: 5px solid #3b82f6;">
        <div class="metric-title">Güncel Kilo</div>
        <div class="metric-value">{son_kilo if son_kilo else '-'} kg</div>
    </div>
    """, unsafe_allow_html=True)

# --- SU ---
    with col2:
     st.markdown(f"""
    <div class="metric-card" style="border-left: 5px solid #22c55e;">
        <div class="metric-title">Su</div>
        <div class="metric-value">{son_gunluk['su'] if son_gunluk else '-'} L</div>
    </div>
    """, unsafe_allow_html=True)

# --- PUAN ---
    with col3:
     st.markdown(f"""
    <div class="metric-card" style="border-left: 5px solid #8b5cf6;">
        <div class="metric-title">Günlük Puan</div>
        <div class="metric-value">{son_gunluk['gunluk_puan'] if son_gunluk else '-'}</div>
    </div>
    """, unsafe_allow_html=True)

    # --- GÜNLÜK DİYET PLANI ---
    if profil and son_kilo:
        st.markdown('<div class="section-title">Bugünün Diyet Planı</div>', unsafe_allow_html=True)

        hedef = "Kilo Vermek"  # istersen sonra profil'e ekleriz

        kalori = kalori_hesapla(
            profil["cinsiyet"],
            son_kilo,
            profil["boy"],
            profil["yas"],
            profil["aktivite"],
            hedef
        )

        kahvalti, ogle, aksam, ara = ogun_onerisi(
            profil["beslenme_tipi"],
            profil["gelir"]
        )

        plan = haftalik_plan(kahvalti, ogle, aksam, ara, kalori)

        bugun_gun = list(plan.keys())[0]
        bugun_plan = plan[bugun_gun]

        st.markdown(f"""
        <div class="day-card">
            <b>Kahvaltı:</b> {bugun_plan['kahvalti']['ad']} ({bugun_plan['kahvalti']['kalori']} kcal)<br>
            <b>Öğle:</b> {bugun_plan['ogle']['ad']} ({bugun_plan['ogle']['kalori']} kcal)<br>
            <b>Akşam:</b> {bugun_plan['aksam']['ad']} ({bugun_plan['aksam']['kalori']} kcal)<br>
            <b>Ara:</b> {bugun_plan['ara']['ad']} ({bugun_plan['ara']['kalori']} kcal)<br><br>
            <b>Toplam:</b> {bugun_plan['toplam']} kcal
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- GÜNLÜK DURUM ANALİZİ ---
    if son_gunluk:
        st.markdown('<div class="section-title">Günlük Analiz</div>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="info-card">
            Su: {son_gunluk['su']} L<br>
            Uyku: {son_gunluk['uyku']} saat<br>
            Adım: {son_gunluk['adim']}<br>
        </div>
        """, unsafe_allow_html=True)

        # akıllı yorumlar
        st.write(su_uyarisi(son_gunluk["su"]))
        st.write(uyku_uyarisi(son_gunluk["uyku"]))

        # basit motivasyon
        if son_gunluk["gunluk_puan"] == "çok iyi":
            st.success("Harika gidiyorsun, böyle devam!")
        elif son_gunluk["gunluk_puan"] == "iyi":
            st.info("İyi gidiyorsun, biraz daha dikkat edebilirsin.")
        elif son_gunluk["gunluk_puan"] == "orta":
            st.warning("Bugün biraz dengesiz, yarın daha iyi olabilir.")
        else:
            st.error("Bugün hedeflerden uzak kaldın, tekrar dene.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- HIZLI KİLO GİRİŞİ ---
    st.markdown('<div class="section-title">Hızlı Kilo Güncelle</div>', unsafe_allow_html=True)

    if "kilo_input" not in st.session_state:
     st.session_state.kilo_input = float(son_kilo) if son_kilo else 70.0

    yeni_kilo = st.number_input(
    "Bugünkü kilo",
    min_value=30.0,
    max_value=200.0,
    value=st.session_state.kilo_input,
    step=0.1,
    key="kilo_input"
)

    if st.button("Kiloyu Kaydet"):
        add_weight(st.session_state.user_id, yeni_kilo, bugun)
        st.success("Kilo kaydedildi.")
        st.rerun()
    # =========================
    # DASHBOARD AI CHATBOX
    # =========================

    st.markdown("---")
    st.markdown("## 🤖 AI Diyet Asistanı")

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    bugun_yemekler_ai = get_today_meals(st.session_state.user_id, bugun)
    alinan_kalori_ai = sum([x[2] for x in bugun_yemekler_ai]) if bugun_yemekler_ai else 0

    hedef_kalori_ai = 0
    if profil and son_kilo:
        hedef_kalori_ai = kalori_hesapla(
            profil["cinsiyet"],
            son_kilo,
            profil["boy"],
            profil["yas"],
            profil["aktivite"],
            "Kilo Vermek"
        )

    if "ai_messages" not in st.session_state:
        st.session_state.ai_messages = [
            {
                "role": "assistant",
                "content": "Merhaba! Ben AI diyet asistanıyım. Bugün ne yediğini veya ne yemen gerektiğini sorabilirsin."
            }
        ]

    for msg in st.session_state.ai_messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="info-card" style="border-left: 5px solid #8b5cf6; margin-bottom: 12px;">
                <b>Sen:</b><br>{msg["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="info-card" style="border-left: 5px solid #f59e0b; margin-bottom: 12px;">
                <b>AI Asistan:</b><br>{msg["content"]}
            </div>
            """, unsafe_allow_html=True)

    user_question = st.text_input(
        "AI Asistana Sor",
        placeholder="Örn: Bugün tantuni yedim, akşam ne yemeliyim?",
        key="ai_user_question"
    )

    if st.button("AI'ye Sor", key="ai_send_button"):

        if not user_question.strip():
            st.warning("Önce bir soru yaz.")
        else:
            st.session_state.ai_messages.append({
                "role": "user",
                "content": user_question
            })

            system_prompt = f"""
Sen profesyonel bir AI diyet ve yaşam tarzı asistanısın.

Kurallar:
- Türkçe konuş.
- Kısa, net ve pratik cevap ver.
- Kullanıcı yurtta kalan öğrenci olabilir.
- Bütçe dostu ve uygulanabilir öneriler sun.
- Tıbbi teşhis koyma.
- Riskli sağlık durumlarında doktora/diyetisyene yönlendir.

Kullanıcı bilgileri:
Profil: {profil}
Güncel kilo: {son_kilo}
Bugünkü yemekler: {bugun_yemekler_ai}
Alınan kalori: {alinan_kalori_ai}
Hedef kalori: {hedef_kalori_ai}
"""

            try:
                with st.spinner("AI cevap hazırlıyor..."):
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            *st.session_state.ai_messages
                        ],
                        temperature=0.7
                    )

                    ai_answer = response.choices[0].message.content

            except Exception as e:
                ai_answer = f"AI bağlantısında hata oluştu: {e}"

            st.session_state.ai_messages.append({
                "role": "assistant",
                "content": ai_answer
            })

            st.rerun()
# profil
# profil
elif sayfa == "Profil":
    st.markdown('<div class="section-title">Profil Bilgileri</div>', unsafe_allow_html=True)

    default = profil if profil else {
        "ad_soyad": "",
        "yas": 22,
        "cinsiyet": "Kadın",
        "boy": 169,
        "gelir": "Orta",
        "beslenme_tipi": "Normal",
        "alerjiler": "",
        "sevilmeyenler": "",
        "spor_gecmisi": "Başlangıç",
        "egzersiz_tercihi": "Yürüyüş",
        "egzersiz_hedefi": "Yağ Kaybı",
        "aktivite": "Düşük"
    }

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="input-label">👤 Ad Soyad</div>', unsafe_allow_html=True)
        ad_soyad = st.text_input("", value=default["ad_soyad"], key="profil_ad")

        st.markdown('<div class="input-label">🎂 Yaş</div>', unsafe_allow_html=True)
        yas = st.number_input("", min_value=10, max_value=100, value=int(default["yas"]), key="profil_yas")

        st.markdown('<div class="input-label">⚧️ Cinsiyet</div>', unsafe_allow_html=True)
        cinsiyet = st.selectbox(
            "",
            ["Kadın", "Erkek"],
            index=["Kadın", "Erkek"].index(default["cinsiyet"]),
            key="profil_cinsiyet"
        )

    with c2:
        st.markdown('<div class="input-label">📏 Boy (cm)</div>', unsafe_allow_html=True)
        boy = st.number_input("", min_value=100, max_value=250, value=int(default["boy"]), key="profil_boy")

        st.markdown('<div class="input-label">💸 Gelir</div>', unsafe_allow_html=True)
        gelir = st.selectbox(
            "",
            ["Düşük", "Orta", "Yüksek"],
            index=["Düşük", "Orta", "Yüksek"].index(default["gelir"]),
            key="profil_gelir"
        )

        st.markdown('<div class="input-label">🏃 Aktivite</div>', unsafe_allow_html=True)
        aktivite = st.selectbox(
            "",
            ["Çok Düşük", "Düşük", "Orta", "Yüksek"],
            index=["Çok Düşük", "Düşük", "Orta", "Yüksek"].index(default["aktivite"]),
            key="profil_aktivite"
        )

    with c3:
        st.markdown('<div class="input-label">🥗 Beslenme Tipi</div>', unsafe_allow_html=True)
        beslenme_tipi = st.selectbox(
            "",
            ["Normal", "Vejetaryen", "Vegan"],
            index=["Normal", "Vejetaryen", "Vegan"].index(default["beslenme_tipi"]),
            key="profil_beslenme"
        )

        st.markdown('<div class="input-label">🏋️ Spor Geçmişi</div>', unsafe_allow_html=True)
        spor_gecmisi = st.selectbox(
            "",
            ["Hiç Yok", "Başlangıç", "Orta", "İleri"],
            index=["Hiç Yok", "Başlangıç", "Orta", "İleri"].index(default["spor_gecmisi"]),
            key="profil_spor"
        )

        st.markdown('<div class="input-label">🎯 Egzersiz Tercihi</div>', unsafe_allow_html=True)
        egzersiz_tercihi = st.selectbox(
            "",
            ["Yürüyüş", "Ev Egzersizi", "Fitness", "Koşu", "Pilates", "Yüzme", "Tenis"],
            index=["Yürüyüş", "Ev Egzersizi", "Fitness", "Koşu", "Pilates", "Yüzme", "Tenis"].index(default["egzersiz_tercihi"]),
            key="profil_tercih"
        )

    st.markdown('<div class="input-label">🚫 Alerjiler</div>', unsafe_allow_html=True)
    alerjiler = st.text_area("", value=default["alerjiler"], key="profil_alerji")

    st.markdown('<div class="input-label">😵 Sevmediklerim</div>', unsafe_allow_html=True)
    sevilmeyenler = st.text_area("", value=default["sevilmeyenler"], key="profil_sevmedik")

    st.markdown('<div class="input-label">🔥 Egzersiz Hedefi</div>', unsafe_allow_html=True)
    egzersiz_hedefi = st.selectbox(
        "",
        ["Yağ Kaybı", "Sıkılaşma", "Kondisyon", "Kas Kazanımı"],
        index=["Yağ Kaybı", "Sıkılaşma", "Kondisyon", "Kas Kazanımı"].index(default["egzersiz_hedefi"]),
        key="profil_hedef"
    )

    if st.button("Profili Kaydet"):
        save_user_profile(
            st.session_state.user_id,
            ad_soyad,
            yas,
            cinsiyet,
            boy,
            gelir,
            beslenme_tipi,
            alerjiler,
            sevilmeyenler,
            spor_gecmisi,
            egzersiz_tercihi,
            egzersiz_hedefi,
            aktivite
        )
        st.success("Profil kaydedildi.")
        st.rerun()

    st.markdown('<div class="input-label">⚖️ Güncel Kilo</div>', unsafe_allow_html=True)
    ilk_kilo = st.number_input(
        "",
        min_value=30.0,
        max_value=200.0,
        value=float(son_kilo) if son_kilo else 70.0,
        step=0.1,
        key="profil_kilo"
    )

    if st.button("Kiloyu Kaydet (Profil)"):
        add_weight(st.session_state.user_id, ilk_kilo, bugun)
        st.success("Kilo kaydedildi.")
        st.rerun()


# diyet planı
elif sayfa == "Diyet Planı":
    if not profil or not son_kilo:
        st.warning("Önce Profil sayfasında bilgilerini ve güncel kilonu kaydet.")
    else:
        hedef = st.selectbox("Hedef", ["Kilo Vermek", "Kiloyu Korumak", "Kilo Almak"])

        bmi = bmi_hesapla(son_kilo, profil["boy"])
        durum = bmi_durumu(bmi)
        kalori = kalori_hesapla(
            profil["cinsiyet"],
            son_kilo,
            profil["boy"],
            profil["yas"],
            profil["aktivite"],
            hedef
        )
        makro = makro_stratejisi(hedef)

        al_list = profil["alerjiler"].split(",") if profil["alerjiler"] else []
        sev_list = profil["sevilmeyenler"].split(",") if profil["sevilmeyenler"] else []

        kahvalti, ogle, aksam, ara = ogun_onerisi(profil["beslenme_tipi"], profil["gelir"])
        kahvalti = filtrele_ogunler(kahvalti, al_list, sev_list)
        ogle = filtrele_ogunler(ogle, al_list, sev_list)
        aksam = filtrele_ogunler(aksam, al_list, sev_list)
        ara = filtrele_ogunler(ara, al_list, sev_list)

        if not kahvalti or not ogle or not aksam or not ara:
            st.error("Filtreleme sonrası yeterli öğün kalmadı.")
        else:
            plan = haftalik_plan(kahvalti, ogle, aksam, ara, kalori)

            a1, a2, a3 = st.columns(3)
            with a1:
                st.markdown(
                    f'<div class="metric-card"><div class="metric-title">BMI</div><div class="metric-value">{bmi}</div></div>',
                    unsafe_allow_html=True
                )
            with a2:
                st.markdown(
                    f'<div class="metric-card"><div class="metric-title">Durum</div><div class="metric-value">{durum}</div></div>',
                    unsafe_allow_html=True
                )
            with a3:
                st.markdown(
                    f'<div class="metric-card"><div class="metric-title">Kalori</div><div class="metric-value">{kalori} kcal</div></div>',
                    unsafe_allow_html=True
                )

            st.markdown('<div class="section-title">Makro Dağılımı</div>', unsafe_allow_html=True)

            m1, m2, m3, m4 = st.columns(4)

            with m1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">Plan Türü</div>
                    <div class="metric-value">{makro['tip']}</div>
                </div>
                """, unsafe_allow_html=True)

            with m2:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">Protein</div>
                    <div class="metric-value">{makro['protein']}</div>
                </div>
                """, unsafe_allow_html=True)

            with m3:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">Karbonhidrat</div>
                    <div class="metric-value">{makro['karbonhidrat']}</div>
                </div>
                """, unsafe_allow_html=True)

            with m4:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">Yağ</div>
                    <div class="metric-value">{makro['yag']}</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown('<div class="section-title">Alternatifler</div>', unsafe_allow_html=True)

            with st.expander("Kahvaltı"):
                for item in kahvalti:
                    st.markdown(
                        f'<div class="meal-card"><b>{item["ad"]}</b><br>{item["kalori"]} kcal</div>',
                        unsafe_allow_html=True
                    )

            with st.expander("Öğle"):
                for item in ogle:
                    st.markdown(
                        f'<div class="meal-card"><b>{item["ad"]}</b><br>{item["kalori"]} kcal</div>',
                        unsafe_allow_html=True
                    )

            with st.expander("Akşam"):
                for item in aksam:
                    st.markdown(
                        f'<div class="meal-card"><b>{item["ad"]}</b><br>{item["kalori"]} kcal</div>',
                        unsafe_allow_html=True
                    )

            with st.expander("Ara Öğün"):
                for item in ara:
                    st.markdown(
                        f'<div class="meal-card"><b>{item["ad"]}</b><br>{item["kalori"]} kcal</div>',
                        unsafe_allow_html=True
                    )

            st.markdown('<div class="section-title">Haftalık Plan</div>', unsafe_allow_html=True)

            for gun, v in plan.items():
                st.markdown(f"""
                <div class="day-card">
                    <b>{gun}</b><br><br>
                    Kahvaltı: {v['kahvalti']['ad']} ({v['kahvalti']['kalori']} kcal)<br>
                    Öğle: {v['ogle']['ad']} ({v['ogle']['kalori']} kcal)<br>
                    Akşam: {v['aksam']['ad']} ({v['aksam']['kalori']} kcal)<br>
                    Ara: {v['ara']['ad']} ({v['ara']['kalori']} kcal)<br><br>
                    <b>Toplam:</b> {v['toplam']} kcal | <b>Hedef:</b> {v['hedef']} kcal
                </div>
                """, unsafe_allow_html=True)


# egzersiz planı
elif sayfa == "Egzersiz Planı":
    if not profil:
        st.warning("Önce Profil sayfasını doldur.")
    else:
        sonuc = egzersiz_onerisi(
            profil["gelir"],
            profil["spor_gecmisi"],
            profil["egzersiz_tercihi"],
            profil["egzersiz_hedefi"]
        )

        st.markdown('<div class="section-title">Egzersiz Önerileri</div>', unsafe_allow_html=True)
        st.write("Ortam:", sonuc["ortam"])
        st.write("Süre:", sonuc["sure"])
        st.write("Not:", sonuc["seviye_notu"])

        st.markdown('<div class="section-title">Önerilen Sporlar</div>', unsafe_allow_html=True)
        for x in sonuc["oneriler"]:
            st.markdown(f"- {x}")

        st.markdown('<div class="section-title">Öğün Sonrası Hareket</div>', unsafe_allow_html=True)
        for k, v in sonuc["ogun_sonrasi"].items():
            st.markdown(f"**{k}:** {v}")


# günlük takip
# günlük takip
elif sayfa == "Günlük Takip":
    if not profil:
        st.warning("Önce Profil sayfasını doldur.")
    else:
        st.markdown('<div class="section-title">Bugün Ne Yedin?</div>', unsafe_allow_html=True)

        kahvalti, ogle, aksam, ara = ogun_onerisi(profil["beslenme_tipi"], profil["gelir"])

        tum_yemekler = []
        for grup in [kahvalti, ogle, aksam, ara]:
            tum_yemekler.extend([x["ad"] for x in grup])

        st.markdown('<div class="input-label">🍽️ Öğün Tipi</div>', unsafe_allow_html=True)
        ogun_tipi = st.selectbox(
            "",
            ["Kahvaltı", "Öğle", "Akşam", "Ara Öğün"],
            key="gunluk_ogun"
        )

        st.markdown('<div class="input-label">🥘 Yemek Seç</div>', unsafe_allow_html=True)
        secilen_yemek = st.selectbox(
            "",
            tum_yemekler,
            key="gunluk_yemek"
        )

        kalori_map = {}
        for grup in [kahvalti, ogle, aksam, ara]:
            for item in grup:
                kalori_map[item["ad"]] = item["kalori"]

        if st.button("Yemeği Kaydet"):
            save_meal_log(
                st.session_state.user_id,
                bugun,
                ogun_tipi,
                secilen_yemek,
                kalori_map[secilen_yemek]
            )
            st.success("Yemek kaydedildi.")
            st.rerun()

        st.markdown('<div class="section-title">Günlük Yaşam Takibi</div>', unsafe_allow_html=True)

        st.markdown('<div class="input-label">💧 Su (litre)</div>', unsafe_allow_html=True)
        su = st.number_input(
            "",
            min_value=0.0,
            max_value=10.0,
            step=0.1,
            key="gunluk_su"
        )

        st.markdown('<div class="input-label">😴 Uyku (saat)</div>', unsafe_allow_html=True)
        uyku = st.number_input(
            "",
            min_value=0.0,
            max_value=24.0,
            step=0.5,
            key="gunluk_uyku"
        )

        st.markdown('<div class="input-label">👣 Adım</div>', unsafe_allow_html=True)
        adim = st.number_input(
            "",
            min_value=0,
            max_value=100000,
            step=500,
            key="gunluk_adim"
        )

        st.markdown('<div class="input-label">🔥 Egzersizle Yaktığın Kalori</div>', unsafe_allow_html=True)
        egzersiz_kalori = st.number_input(
            "",
            min_value=0.0,
            max_value=5000.0,
            step=10.0,
            key="gunluk_egzersiz"
        )

        bugun_yemekler = get_today_meals(st.session_state.user_id, bugun)
        alinan_kalori = sum([x[2] for x in bugun_yemekler]) if bugun_yemekler else 0

        hedef_kalori = 0
        if profil and son_kilo:
            hedef_kalori = kalori_hesapla(
                profil["cinsiyet"],
                son_kilo,
                profil["boy"],
                profil["yas"],
                profil["aktivite"],
                "Kilo Vermek"
            )

        adim_yakim = adim_kalorisi(adim)
        net_kalan = hedef_kalori + adim_yakim + egzersiz_kalori - alinan_kalori if hedef_kalori else 0
        puan = gunluk_puanla(hedef_kalori, alinan_kalori, su, uyku) if hedef_kalori else "-"

        if st.button("Günlük Takibi Kaydet"):
            save_daily_log(
                st.session_state.user_id,
                bugun,
                su,
                uyku,
                adim,
                egzersiz_kalori,
                alinan_kalori,
                puan
            )
            st.success("Günlük takip kaydedildi.")
            st.rerun()

        st.markdown('<div class="section-title">Bugünkü Özet</div>', unsafe_allow_html=True)

        o1, o2, o3, o4 = st.columns(4)

        with o1:
            st.markdown(f"""
            <div class="metric-card" style="border-left: 5px solid #ec4899;">
                <div class="metric-title">Alınan Kalori</div>
                <div class="metric-value">{alinan_kalori} kcal</div>
            </div>
            """, unsafe_allow_html=True)

        with o2:
            st.markdown(f"""
            <div class="metric-card" style="border-left: 5px solid #22c55e;">
                <div class="metric-title">Adım Yakımı</div>
                <div class="metric-value">{adim_yakim} kcal</div>
            </div>
            """, unsafe_allow_html=True)

        with o3:
            st.markdown(f"""
            <div class="metric-card" style="border-left: 5px solid #f59e0b;">
                <div class="metric-title">Egzersiz Yakımı</div>
                <div class="metric-value">{egzersiz_kalori} kcal</div>
            </div>
            """, unsafe_allow_html=True)

        with o4:
            st.markdown(f"""
            <div class="metric-card" style="border-left: 5px solid #8b5cf6;">
                <div class="metric-title">Net Kalan</div>
                <div class="metric-value">{net_kalan} kcal</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="info-card">
            <b>Günlük Değerlendirme:</b> {puan}<br>
            <b>Su Yorumu:</b> {su_uyarisi(su)}<br>
            <b>Uyku Yorumu:</b> {uyku_uyarisi(uyku)}
        </div>
        """, unsafe_allow_html=True)

        if bugun_yemekler:
            st.markdown('<div class="section-title">Bugün Kaydedilen Yemekler</div>', unsafe_allow_html=True)

            for row in bugun_yemekler:
                st.markdown(f"""
                <div class="meal-card">
                    <b>{row[0]}</b><br>
                    {row[1]} - {row[2]} kcal
                </div>
                """, unsafe_allow_html=True)
                        # --- KİLO DEĞİŞİM GRAFİĞİ ---
        st.markdown('<div class="section-title">Kilo Değişim Grafiği</div>', unsafe_allow_html=True)

        kilo_gecmisi = get_weight_history(st.session_state.user_id)

        if kilo_gecmisi:
            import pandas as pd

            kilo_df = pd.DataFrame(kilo_gecmisi, columns=["Tarih", "Kilo"])
            kilo_df["Tarih"] = pd.to_datetime(kilo_df["Tarih"])

            st.line_chart(
                kilo_df,
                x="Tarih",
                y="Kilo"
            )
        else:
            st.info("Kilo grafiği için önce birkaç kilo kaydı eklemelisin.")

