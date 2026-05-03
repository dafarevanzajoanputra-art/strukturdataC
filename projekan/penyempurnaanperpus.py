import streamlit as st
import pandas as pd

# ===============================================
# INISIALISASI DATABASE (Session State)
# ===============================================
# Streamlit menjalankan ulang skrip dari atas ke bawah setiap ada interaksi.
# session_state digunakan agar data tetap tersimpan selama tab browser dibuka.
if 'daftar_buku' not in st.session_state:
    st.session_state.daftar_buku = [
        # Data contoh awal
        {"code": 101, "judul": "Laskar Pelangi", "pengarang": "Andrea Hirata", "genre": "Fiksi", "stok": 5, "dipinjam": 0},
        {"code": 102, "judul": "Filosofi Teras", "pengarang": "Henry Manampiring", "genre": "Non-Fiksi", "stok": 3, "dipinjam": 0}
    ]

# ===============================================
# FUNGSI HELPER
# ===============================================
def cari_indeks(kode):
    for i, buku in enumerate(st.session_state.daftar_buku):
        if buku['code'] == kode:
            return i
    return None

# ===============================================
# ANTARMUKA UTAMA (UI)
# ===============================================
st.set_page_config(page_title="Perpus Digital Kelompok 4", layout="wide")

st.title("📚 Sistem Manajemen Perpustakaan")
st.sidebar.info("created by:")
st.sidebar.header("Menu Utama")
menu = st.sidebar.selectbox("Pilih Aksi:", 
    ["Katalog Buku", "Tambah Buku", "Pinjam/Kembali", "Update Data", "Hapus Buku"])

# --- 1. KATALOG BUKU (READ) ---
if menu == "Katalog Buku":
    st.header("📖 Katalog Buku")
    if not st.session_state.daftar_buku:
        st.warning("Belum ada data buku.")
    else:
        # Mengubah list of dict menjadi DataFrame agar tampil rapi sebagai tabel
        df = pd.DataFrame(st.session_state.daftar_buku)
        df['Tersedia'] = df['stok'] - df['dipinjam']
        st.table(df)

# --- 2. TAMBAH BUKU (CREATE) ---
elif menu == "Tambah Buku":
    st.header("➕ Tambah Buku Baru")
    with st.form("form_tambah"):
        col1, col2 = st.columns(2)
        with col1:
            kode = st.number_input("Kode Buku", min_value=1, step=1)
            judul = st.text_input("Judul Buku")
            pengarang = st.text_input("Pengarang")
        with col2:
            genre = st.text_input("Genre")
            stok = st.number_input("Jumlah Stok", min_value=1, step=1)
        
        submit = st.form_submit_button("Simpan Buku")
        
        if submit:
            if cari_indeks(kode) is not None:
                st.error("Kode buku sudah ada!")
            else:
                baru = {
                    "code": kode, "judul": judul, "pengarang": pengarang,
                    "genre": genre, "stok": stok, "dipinjam": 0
                }
                st.session_state.daftar_buku.append(baru)
                st.success(f"Buku '{judul}' berhasil ditambahkan!")

# --- 3. PINJAM/KEMBALI (UPDATE STATUS) ---
elif menu == "Pinjam/Kembali":
    st.header("🔄 Sirkulasi Buku")
    kode_cari = st.number_input("Masukkan Kode Buku", min_value=1, step=1)
    idx = cari_indeks(kode_cari)
    
    if idx is not None:
        buku = st.session_state.daftar_buku[idx]
        st.info(f"Buku: **{buku['judul']}** | Tersedia: {buku['stok'] - buku['dipinjam']}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Pinjam Buku"):
                if buku['dipinjam'] < buku['stok']:
                    st.session_state.daftar_buku[idx]['dipinjam'] += 1
                    st.success("Berhasil meminjam!")
                    st.rerun()
                else:
                    st.error("Stok habis!")
        with col2:
            if st.button("Kembalikan Buku"):
                if buku['dipinjam'] > 0:
                    st.session_state.daftar_buku[idx]['dipinjam'] -= 1
                    st.success("Berhasil dikembalikan!")
                    st.rerun()
                else:
                    st.error("Tidak ada buku yang sedang dipinjam.")
    else:
        st.warning("Kode buku tidak ditemukan.")

# --- 4. UPDATE DATA ---
elif menu == "Update Data":
    st.header("✏️ Edit Data Buku")
    kode_cari = st.number_input("Kode Buku yang akan diedit", min_value=1, step=1)
    idx = cari_indeks(kode_cari)
    
    if idx is not None:
        with st.form("form_edit"):
            buku = st.session_state.daftar_buku[idx]
            n_judul = st.text_input("Judul Baru", value=buku['judul'])
            n_pengarang = st.text_input("Pengarang Baru", value=buku['pengarang'])
            n_stok = st.number_input("Total Stok Baru", min_value=buku['dipinjam'], value=buku['stok'])
            
            if st.form_submit_button("Update"):
                st.session_state.daftar_buku[idx].update({
                    "judul": n_judul, "pengarang": n_pengarang, "stok": n_stok
                })
                st.success("Data berhasil diperbarui!")
                st.rerun()
    else:
        st.write("Masukkan kode buku untuk mengedit.")

# --- 5. HAPUS BUKU (DELETE) ---
elif menu == "Hapus Buku":
    st.header("🗑️ Hapus Buku")
    kode_cari = st.number_input("Kode Buku yang akan dihapus", min_value=1, step=1)
    if st.button("Hapus Permanen", type="primary"):
        idx = cari_indeks(kode_cari)
        if idx is not None:
            deleted_book = st.session_state.daftar_buku.pop(idx)
            st.success(f"Buku '{deleted_book['judul']}' dihapus.")
            st.rerun()
        else:
            st.error("Buku tidak ditemukan.")