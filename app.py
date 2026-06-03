import streamlit as st

# 1. Konfigurasi halaman web browser
st.set_page_config(page_title="Pajak Bantul - Layanan Pajak Daerah", layout="centered")

# Menggunakan CSS kustom agar tampilannya mirip seperti desain tkinter sebelumnya
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        background-color: #008060;
        color: white;
        width: 100%;
        padding: 12px;
        border-radius: 5px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #006a4e; color: white; }
    .box-hijau {
        background-color: #006a4e;
        padding: 40px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Membuat layout 2 kolom (Kiri Hijau, Kanan Form Login)
kolom_kiri, kolom_kanan = st.columns([1, 1])

with kolom_kiri:
    st.markdown("""
        <div class="box-hijau">
            <h1 style='color: white; margin-top: 40px; font-family: Arial;'>Pajak Bantul</h1>
            <p style='color: #e0e0e0; font-style: italic; font-size: 14px;'>Layanan Pajak Kabupaten Bantul</p>
        </div>
    """, unsafe_allow_html=True)

with kolom_kanan:
    st.subheader("Selamat Datang!")
    st.caption("Aplikasi pelayanan pajak daerah Kabupaten Bantul")
    
    # Input Form ala Web
    email = st.text_input("Masuk (Email)", placeholder="admin@bantul.go.id")
    password = st.text_input("Masukkan kata sandi", type="password", placeholder="••••••••")
    
    # Tombol Masuk dan Logika Verifikasi
    if st.button("Masuk"):
        if not email or not password:
            st.warning("Email dan Kata Sandi harus diisi!")
        else:
            if email == "admin@bantul.go.id" and password == "rahasia123":
                st.success("Selamat Datang di Aplikasi Pajak Bantul!")
            else:
                st.error("Email atau Kata Sandi salah.")
