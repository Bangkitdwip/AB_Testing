"""Projek_DA_Bangkit.ipynb

#Study case / Goals
- melakukan A/B testing kepada pelanggan dengan memberikan diskon apakah akan menaikkan / meningkatkan jumlah pembelian secara signifikan
- Membandingkan total penjualan antara kelompok dengan diskon dan tanpa diskon untuk mengetahui apakah diskon benar-benar meningkatkan pendapatan atau justru mengurangi pendapatan.

#Data Understanding

## Data Description

- **Date**: Purchase date  
- **Customer_ID**: Unique customer identifier  
- **Category**: Product category (Coffee Beans)  
- **Product**: Coffee type (Brazilian, Ethiopian, Colombian, Costa Rica, Guatemala)  
- **Unit Price**: Price per unit for each product  
- **Quantity**: Number of units purchased  
- **Sales Amount**: Total sales (Quantity × Unit Price)  
- **Used_Discount**: Whether a discount was applied (True/False)  
- **Discount_Amount**: Discount value applied (20%)  
- **Final Sales**: Sales After Discount
"""

import pandas as pd
import os
import numpy as np
from scipy import stats
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px


pd.set_option('display.max_rows', None)  # Menampilkan semua baris
pd.set_option('display.max_columns', None)  # Jika ada banyak kolom

def projek():
    st.markdown("<h1 style='text-align: center;'>Analisis A/B Testing Penjualan Biji Kopi</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: left;'>Background</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>Dalam industri ritel, strategi diskon kerap digunakan untuk meningkatkan volume penjualan dan menarik pelanggan baru. Namun, tidak semua program diskon memberikan hasil yang diharapkan. Terkadang, pemberian potongan harga justru menurunkan total pendapatan atau menyebabkan pelanggan hanya membeli ketika ada promosi.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>Dalam konteks ini, dilakukan sebuah eksperimen A/B testing dengan membagi pelanggan ke dalam dua kelompok:</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>- Kelompok A (Variant): Mendapatkan diskon 20%</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>- Kelompok B (Control): Tidak mendapatkan diskon</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>Eksperimen ini dilakukan selama periode 2 tahun dengan tujuan untuk mengevaluasi efektivitas strategi diskon terhadap peningkatan jumlah pembelian dan total pendapatan.</div>", unsafe_allow_html=True)

    st.subheader('')
    with st.expander("Eksplorasi Data"):
        st.write('## Data Description')
        st.write('Date: Purchase date')
        st.write('Customer_ID: Unique customer identifier')
        st.write('Category : Product category (Coffee Beans)')
        st.write('Product: Coffee type (Brazilian, Ethiopian, Colombian, Costa Rica, Guatemala)')
        st.write('Unit Price: Price per unit for each product')
        st.write('Quantity: Number of units purchased')
        st.write('Sales Amount : Total sales (Quantity × Unit Price)')
        st.write('A/B Test: Whether a discount was applied (A/B)')
        st.write('Discount_Amount: Discount value applied (20%)')
        st.write('Final Sales : Sales After Discount')
        df = pd.read_csv('kopisale.csv')
        st.markdown("<h2 style='text-align: justify;'>Datasets</h2>", unsafe_allow_html=True)
        st.dataframe(df)
        if 'Unnamed: 0' in df.columns:
            df.drop(columns='Unnamed: 0', inplace=True)
        info_df = pd.DataFrame({
            "Kolom": df.columns,
            "Non-Null Count": df.notnull().sum().values,
            "Tipe Data": df.dtypes.values
            })
        st.subheader("📋 Informasi Struktur Datasets")
        st.dataframe(info_df)
        

    with st.expander("hipotesis dan uji statistik"):
        st.write('## Hipotesis')
        st.write('H0 : tidak ada peningkatan jumlah penjualan untuk kelompok A')
        st.write('H1 : ada peningkatan jumlah penjualan untuk kelompok A')
        st.write('## Normality test')
        
        group_a = st.checkbox("Tampilkan Grup A")
        group_b = st.checkbox("Tampilkan Grup B")
        def ad_normal_test(x, group_name, container):
            result = stats.anderson(x, dist='norm')
            st.write(f'#### Normality test for {group_name}')
            for cv, sig in zip(result.critical_values, result.significance_level):
                if result.statistic < cv:
                    st.write(f"data is normally distributed at {sig}% significance level")
                else:
                    st.write(f"Reject normality at {sig}% significance level")
        st.write('-' * 50)

        col1, col2 = st.columns(2)
        if group_a:
            with col1:
                st.subheader("🅰️  Grup A")
                for product in df['Product'].unique():
                    subset = df[(df['A/B Test'] == 'A') & (df['Product'] == product)]['Quantity']
                    ad_normal_test(subset, f"A - {product}", st)

        if group_b:
            with col2:
                st.subheader("🅱️ Grup B")
                for product in df['Product'].unique():
                    subset = df[(df['A/B Test'] == 'B') & (df['Product'] == product)]['Quantity']
                    ad_normal_test(subset, f"B - {product}", st)

        if "histplot" not in st.session_state:
            st.session_state.histplot = False
        if st.button('Tampilkan Histplot'):
            st.session_state.histplot = not st.session_state.histplot
        if st.session_state.histplot:
            st.subheader('Histogram Plot')
            g = sns.FacetGrid(df, col="Product", hue="A/B Test", col_wrap=3)
            g.map(sns.histplot, "Quantity", kde=True)
            g.add_legend()
            st.pyplot(g.figure)

        if "show_result" not in st.session_state:
            st.session_state.show_result = False
        if st.button("Tampilkan Hasil Uji"):
            st.session_state.show_result = not st.session_state.show_result
        if st.session_state.show_result:
            st.markdown("###  Hasil Uji Statistik")
            for product in df['Product'].unique():
                group_A = df[(df['A/B Test'] == 'A') & (df['Product'] == product)]['Quantity']
                group_B = df[(df['A/B Test'] == 'B') & (df['Product'] == product)]['Quantity']
                stat, p_value = stats.mannwhitneyu(group_A, group_B)
                st.write(f" 📦 {product}: stat = {stat:.4f}, p-value = {p_value:.4f}")
                if p_value < 0.05:
                    st.success("✅ *Tolak H₀*: Ada perbedaan signifikan antara grup A dan B untuk produk ini.")
                else:
                    st.info("ℹ️ *Gagal tolak H₀*: Tidak ada perbedaan signifikan antara grup A dan B untuk produk ini.")
            
                st.markdown("---")

    st.write("## Visualisasi Penjualan Biji Kopi")
    if st.checkbox("Jumlah Penjualan per Produk (A/B Test)"):
        st.subheader("Jumlah Penjualan per Produk")
        fig1 = px.bar(
            df.groupby(['Product', 'A/B Test'])['Quantity'].sum().reset_index(),
            x='Quantity', y='Product', color='A/B Test', barmode='group', orientation='h'
        )
        st.plotly_chart(fig1)

    if st.checkbox("Persebaran Pelanggan"):
        st.subheader("Persebaran Pelanggan per Kota")
        customer_counts = df.groupby("City")["Customer_ID"].nunique().reset_index()
        customer_counts.rename(columns={"Customer_ID": "Jumlah_Customer"}, inplace=True)
        customer_counts["Label"] = customer_counts["City"] + "<br>Jumlah: " + customer_counts["Jumlah_Customer"].astype(str)

        fig2 = px.treemap(
            customer_counts,
            path=["Label"],
            values="Jumlah_Customer",
            color="Jumlah_Customer",
            color_continuous_scale="Blues"
        )
        st.plotly_chart(fig2)

    if st.checkbox("Total Quantity (A/B Test)"):
        st.subheader("Total Quantity per Grup A/B Test")
        quantity = df.groupby("A/B Test")["Quantity"].sum().reset_index()
        fig3 = px.bar(quantity, x="A/B Test", y="Quantity", color="A/B Test", text_auto=True)
        st.plotly_chart(fig3)

    if st.checkbox("Total Revenue (A/B Test)"):
        st.subheader("Total Revenue per Grup A/B Test")
        revenue = df.groupby("A/B Test")["Final Sales"].sum().reset_index()
        fig4 = px.bar(revenue, x="A/B Test", y="Final Sales", color="A/B Test", text_auto=".2s")
        st.plotly_chart(fig4)

    if st.checkbox("Tren Penjualan Bulanan"):
        st.subheader("Tren Penjualan Bulanan")
        df["Date"] = pd.to_datetime(df["Date"])
        df["Month"] = df["Date"].dt.to_period("M").astype(str)
        trend = df.groupby(["Month", "A/B Test"])["Final Sales"].sum().reset_index()
        fig5 = px.line(trend, x="Month", y="Final Sales", color="A/B Test", markers=True)
        fig5.update_traces(
            texttemplate='%{text:.0f}',  
            textposition='top center')
        st.plotly_chart(fig5)

    st.subheader('Kesimpulan & Rekomendasi Bisnis')
    st.write('### Kesimpulan')
    st.write("1. Pemberian diskon menyebabkan penurunan revenue yang cukup signifikan")
    st.write('2. Ada sedikit kenaikan quantity pembelian hanya saja menurunkan revenue')
    st.write('3. Rata-rata penjualan setiap bulannya untuk kelompok A lebih rendah dibandingkan kelompok B')
    st.write('### Rekomendasi')
    st.write('1. Mensiasati strategi diskon dengan minimal pembelian sehingga menaikkan quantity dan revenue')
    st.write('2. Memberikan diskon kepada produk yang laris sehingga tidak menurunkan revenue tetapi menaikkan quantity pembelian')
    st.write('3. Meningkatkan promosi di kota-kota yang memiliki rata-rata pembelian tertinggi')
