
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
from scipy.stats import shapiro

df = pd.read_csv('data/data.csv', parse_dates=['date'])
df['date'] = df['date'].astype(str)

st.title("End-to-End EDA & Storytelling Dashboard")

buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()

st.sidebar.header("Filters")
cat = st.sidebar.selectbox("Category", df['category'].unique())

page = st.sidebar.selectbox(
    "Select Page",
    ["Overview", "Univariate", "Relationships", "Time Trends", "Statistical Tests"]
)

filtered = df[df['category'] == cat]

if page == "Overview":
    st.subheader("Data Quality Report")
    st.text(s)
    st.write("Summary Statistics:")
    st.write(df.describe())
    st.write("Missing Values:")
    st.write(df.isnull().sum())

    st.subheader("Data Preview")
    st.dataframe(filtered)

    st.subheader("KPIs")
    st.write(filtered.describe())

elif page == "Univariate":
    st.subheader("Univariate Analysis")

    for col in filtered.select_dtypes(include='number').columns:
        st.write(f"Histogram for {col}")
        fig, ax = plt.subplots()
        sns.histplot(filtered[col], kde=True, ax=ax)
        st.pyplot(fig)

        st.write("Skewness:", filtered[col].skew())
        st.write("Kurtosis:", filtered[col].kurt())

    st.subheader("Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered['value'], kde=True, ax=ax)
    st.pyplot(fig)

    st.write("Insight: Distribution shows how values are spread for selected category.")

elif page == "Relationships":
    st.subheader("Correlation Heatmap")
    fig2, ax2 = plt.subplots()
    sns.heatmap(filtered.corr(numeric_only=True), annot=True, ax=ax2)
    st.pyplot(fig2)

elif page == "Time Trends":
    st.subheader("Time Trend")
    st.line_chart(filtered.set_index('date')['value'])

elif page == "Statistical Tests":
    st.subheader("Statistical Test")

    col = st.selectbox("Select column", df.select_dtypes(include='number').columns)

    clean_data = df[col].dropna()

    if len(clean_data) < 3:
        st.write("Not enough data for Shapiro test")
    elif clean_data.nunique() <= 1:
        st.write("Data has no variation (all values same)")
    else:
        stat, p = shapiro(clean_data)
        st.write("Shapiro Test Statistic:", stat)
        st.write("p-value:", p)

        if p > 0.05:
            st.success("Data is normally distributed")
        else:
            st.error("Data is not normally distributed")

    st.download_button("Export Filtered Data", filtered.to_csv(index=False), "filtered.csv")