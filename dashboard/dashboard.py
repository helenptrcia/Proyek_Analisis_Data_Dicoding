import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# PAGE CONFIG
st.set_page_config(
    page_title="E-Commerce Analysis Dashboard",
    layout="wide"
)

st.title("📦 E-Commerce Public Dataset Dashboard")
st.caption("Ringkasan hasil Exploratory Data Analysis (EDA) dan Advanced Analysis")

# LOAD MAIN DATA
@st.cache_data
def load_data():
    return pd.read_csv(
        "dashboard/main_data.csv",
        parse_dates=["order_purchase_timestamp"]
    )

df = load_data()

# KPI SECTION
st.markdown("### 📊 Ringkasan Utama")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Order", f"{df['order_id'].nunique():,}")

with col2:
    st.metric(
        "Persentase Keterlambatan",
        f"{df['is_delayed'].mean() * 100:.2f}%"
    )

with col3:
    st.metric(
        "Rata-rata Review Score",
        f"{df['review_score'].mean():.2f}"
    )

st.markdown("---")

# EXPLORATORY DATA ANALYSIS (EDA)
st.header("📘 Exploratory Data Analysis (EDA)")

col1, col2 = st.columns(2)

with col1:
    # 1. Kategori Produk dengan Penjualan Terendah
    st.subheader("📉 Kategori Produk dengan Penjualan Terendah")

    low_sales_categories = (
        df.groupby("product_category_name")
        .size()
        .reset_index(name="total_sales")
        .sort_values("total_sales")
        .head(10)
    )

    min_value = low_sales_categories["total_sales"].min()

    colors = [
        "#D62728" if val == min_value else "#B0B0B0"
        for val in low_sales_categories["total_sales"]
    ]

    fig1, ax1 = plt.subplots(figsize=(10, 8))
    sns.barplot(
        data=low_sales_categories,
        x="total_sales",
        y="product_category_name",
        hue="product_category_name",
        palette=colors,
        legend=False,
        ax=ax1
    )
    ax1.set_xlabel("Total Penjualan")
    ax1.set_ylabel(None)
    sns.despine()
    st.pyplot(fig1, use_container_width=True)

    with st.expander("🔍 Lihat Penjelasan"):
        st.write(
            """Beberapa kategori produk seperti *seguros_e_servicos*, *fashion_roupa_infanto_juvenil*, dan *pc_gamer* memiliki 
            volume penjualan yang jauh lebih rendah dibandingkan kategori lainnya. Hal ini menunjukkan bahwa permintaan pelanggan 
            terhadap kategori-kategori tersebut relatif kecil, sehingga kontribusinya terhadap total transaksi platform juga terbatas."""
        )

with col2:
    # 2. Negara Bagian dengan Aktivitas Seller Tertinggi
    st.subheader("🏬 Negara Bagian dengan Aktivitas Seller Tertinggi")

    seller_activity = (
        df.groupby("seller_state")
        .size()
        .reset_index(name="total_seller_activity")
        .sort_values("total_seller_activity", ascending=False)
        .head(10)
    )

    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.barplot(
        data=seller_activity,
        x="total_seller_activity",
        y="seller_state",
        color='#4C72B0',
        ax=ax2
    )   
    ax2.set_xlabel("Jumlah Aktivitas Seller")
    ax2.set_ylabel("State")
    sns.despine()
    st.pyplot(fig2, use_container_width=True)

    with st.expander("🔍 Lihat Penjelasan"):
        st.write(
            """Aktivitas seller sangat terkonsentrasi pada beberapa negara bagian tertentu. State SP (São Paulo) menunjukkan 
            jumlah aktivitas seller yang paling tinggi dibandingkan state lainnya. Pola ini mengindikasikan adanya sentralisasi 
            penjual dan aktivitas ekonomi pada wilayah tertentu, sementara banyak state lain memiliki tingkat aktivitas seller 
            yang relatif rendah."""
        )

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    # 3. Dampak Keterlambatan terhadap Review
    st.subheader("🚚 Dampak Keterlambatan terhadap Skor Ulasan")

    delay_review_summary = (
        df.groupby("is_delayed")["review_score"]
        .mean()
        .reset_index()
    )

    delay_review_summary["status"] = delay_review_summary["is_delayed"].map(
        {False: "Tepat Waktu", True: "Terlambat"}
    )

    fig3, ax3 = plt.subplots(figsize=(8, 6))
    sns.barplot(
        data=delay_review_summary,
        x="review_score",
        y="status",
        hue="status",
        palette=["#008450", "#B81D13"],
        legend=False,
        ax=ax3
    )
    ax3.set_xlabel("Rata-rata Review Score")
    ax3.set_ylabel(None)
    sns.despine()
    st.pyplot(fig3, use_container_width=True)

    with st.expander("🔍 Lihat Penjelasan"):
        st.write(
            """Terdapat perbedaan yang jelas pada rata-rata skor ulasan antara pesanan yang dikirim tepat waktu dan yang 
            mengalami keterlambatan. Pesanan yang dikirim tepat waktu cenderung memperoleh skor ulasan yang lebih tinggi, 
            sementara keterlambatan pengiriman berkorelasi dengan penurunan tingkat kepuasan pelanggan."""
        )

with col4:
    # 4. State dengan Rasio Keterlambatan Tertinggi
    st.subheader("📍 State dengan Rasio Keterlambatan Tertinggi")

    state_delay = (
        df.groupby("customer_state")
        .agg(
            total_orders=("order_id", "nunique"),
            delayed_orders=("is_delayed", "sum")
        )
        .reset_index()
    )

    state_delay["delay_ratio"] = (
        state_delay["delayed_orders"] / state_delay["total_orders"]
    )

    top_states_delay = (
        state_delay
        .sort_values("total_orders", ascending=False)
        .head(10)
        .sort_values("delay_ratio", ascending=False)
    )

    fig4, ax4 = plt.subplots(figsize=(8, 6))
    sns.barplot(
        data=top_states_delay,
        x="delay_ratio",
        y="customer_state",
        color='#4C72B0',
        ax=ax4
    )
    ax4.set_xlabel("Rasio Keterlambatan")
    ax4.set_ylabel("State")
    sns.despine()
    st.pyplot(fig4, use_container_width=True)

    with st.expander("🔍 Lihat Penjelasan"):
        st.write(
            """Rasio keterlambatan pengiriman bervariasi antar negara bagian. Beberapa state seperti BA (Bahia), RJ (Rio de Janeiro), 
            dan ES (Espírito Santo) menunjukkan rasio keterlambatan yang lebih tinggi dibandingkan state lain dengan volume pesanan 
            besar. Hal ini mengindikasikan adanya perbedaan performa logistik antar wilayah."""
            )

st.markdown("---")

# ADVANCED ANALYSIS
st.header("🚀 Advanced Analysis")
col5, col6 = st.columns(2)

with col5:
    # RFM ANALYSIS
    st.subheader("👥 Segmentasi Pelanggan (RFM Analysis)")

    snapshot_date = df["order_purchase_timestamp"].max() + pd.Timedelta(days=1)

    rfm = (
        df.groupby("customer_unique_id")
        .agg(
            recency=("order_purchase_timestamp", lambda x: (snapshot_date - x.max()).days),
            frequency=("order_id", "nunique"),
            monetary=("price", "sum")
        )
        .reset_index()
    )

    # Scoring
    rfm["R_score"] = pd.qcut(rfm["recency"], 4, labels=[4, 3, 2, 1])
    rfm["M_score"] = pd.qcut(rfm["monetary"], 4, labels=[1, 2, 3, 4])
    rfm["F_score"] = pd.cut(
        rfm["frequency"],
        bins=[0, 1, 2, 5, rfm["frequency"].max()],
        labels=[1, 2, 3, 4]
    )

    # Segment rule
    def rfm_segment(row):
        if row["R_score"] == 4 and row["F_score"] == 4:
            return "Loyal Customer"
        elif row["R_score"] <= 2 and row["F_score"] >= 3:
            return "At Risk Customer"
        else:
            return "Regular Customer"

    rfm["segment"] = rfm.apply(rfm_segment, axis=1)

    fig, ax = plt.subplots(figsize=(8, 6))
    rfm["segment"].value_counts().plot(kind="bar", ax=ax)
    ax.set_yscale("log")
    ax.set_xlabel(None)
    ax.set_ylabel("Jumlah Pelanggan (log scale)")
    sns.despine()
    st.pyplot(fig)

    with st.expander("🔍 Lihat Penjelasan"):
        st.write(
            """Hasil segmentasi RFM menunjukkan bahwa mayoritas pelanggan termasuk dalam kategori Regular Customer, sementara jumlah 
            Loyal Customer sangat kecil dan At Risk Customer hanya sebagian kecil dari total pelanggan. Distribusi ini mencerminkan 
            rendahnya tingkat pembelian ulang dan loyalitas pelanggan, sehingga masih terdapat peluang besar untuk meningkatkan 
            strategi retensi."""
        )

with col6:
    # SPENDING CATEGORY
    st.subheader("💰 Distribusi Kategori Pengeluaran Pelanggan")

    def spending_category(x):
        if x >= 500:
            return "High Value"
        elif x >= 200:
            return "Medium Value"
        else:
            return "Low Value"

    rfm["spending_category"] = rfm["monetary"].apply(spending_category)

    fig5, ax5 = plt.subplots(figsize=(8, 6))
    rfm["spending_category"].value_counts().plot(
        kind="pie", autopct="%1.1f%%", ax=ax5
    )
    ax5.set_ylabel(None)
    st.pyplot(fig5)

    with st.expander("🔍 Lihat Penjelasan"):
        st.write(
            """Berdasarkan pengelompokan manual terhadap total pengeluaran pelanggan, sebagian besar pelanggan termasuk dalam kategori 
            *Low Value*, diikuti oleh *Medium Value*, dan hanya sebagian kecil yang tergolong *High Value*. Hal ini menunjukkan bahwa 
            sebagian besar transaksi memiliki nilai pembelian relatif rendah, sementara kontribusi pendapatan terbesar kemungkinan 
            berasal dari kelompok pelanggan bernilai tinggi yang jumlahnya terbatas."""
        )

# FOOTER
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>"
    "Dashboard dibuat menggunakan Streamlit | EDA & Advanced Analysis"
    "</p>",
    unsafe_allow_html=True
)