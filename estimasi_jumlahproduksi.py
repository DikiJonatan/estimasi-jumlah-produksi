import pickle
import streamlit as st

model = pickle.load(open('estimasi_jumlahproduksi.sav', 'rb'))

st.title('Estimasi')
st.subheader('Jumlah Produksi')



Luas_Lahan = st.number_input('Input Luas_Lahan')
Jumlah_Pohon = st.number_input('Input Jumlah_Pohon')
Pupuk_Kandang = st.number_input('Input Pupuk_Kandang')
Pupuk_Phonska = st.number_input('Input Pupuk_Phonska')
Pestisida = st.number_input('Input Pestisida')
Tenaga_Kerja = st.number_input('Input Tenaga_Kerja')

predict = ''

if st.button('Jumlah Produksi'):
    predict = model.predict(
        [[Luas_Lahan,Jumlah_Pohon,Pupuk_Kandang,Pupuk_Phonska,Pestisida,Tenaga_Kerja]]
    )
    st.write ('Estimasi jumlah produksi yang dihasilkan adalah : ', predict)