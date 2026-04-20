import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Thematic Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Data
# -----------------------------
data = pd.DataFrame({
    "Theme": [
        "AI, Analytics & Forecasting",
        "Improved Data Collection & Record Keeping",
        "Technical Capacity & Training",
        "Centralized & Integrated Data Systems",
        "Budget & Resource Support",
        "Policy, Institutional Reform & Coordination"
    ],
    "Mentions": [31, 23, 22, 21, 16, 14],
    "Description": [
        "Need for AI, machine learning, HDM-4 and predictive models to improve planning and deterioration forecasting.",
        "Need for regular pavement surveys, complete maintenance histories and better continuity of records.",
        "Need for staff training in HDM-4, AI, data analytics and pavement management tools.",
        "Need for a shared national road asset database linking condition, maintenance and planning data.",
        "Need for more budget support for data collection, research and technology.",
        "Need for stronger policy frameworks, institutional coordination and reduced political influence."
    ]
})

data["Percentage"] = round((data["Mentions"] / 56) * 100, 1)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: bold;
    color: #1f2937;
    margin-bottom: 0px;
}
.sub-title {
    font-size: 18px;
    color: #6b7280;
    margin-top: 0px;
}
.theme-card {
    background-color: #f8fafc;
    padding: 18px;
    border-radius: 10px;
    border-left: 6px solid #2563eb;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title Section
# -----------------------------
st.markdown(
    '<p class="main-title">Thematic Analysis Dashboard</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Q27 and Q28 Open-Ended Reflections on Pavement Performance Management in Kenya</p>',
    unsafe_allow_html=True
)

st.write("Based on 56 survey responses")

# -----------------------------
# Metrics
# -----------------------------
metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric("Total Responses", 56)

with metric2:
    st.metric("Total Themes", len(data))

with metric3:
    st.metric("Most Mentioned Theme", "AI & Forecasting")

st.markdown("---")

# -----------------------------
# Charts
# -----------------------------
chart1, chart2 = st.columns(2)

with chart1:
    st.subheader("Theme Frequency")

    sorted_data = data.sort_values(by="Mentions", ascending=True)

    fig_bar = px.bar(
        sorted_data,
        x="Mentions",
        y="Theme",
        orientation="h",
        text="Mentions",
        color="Theme"
    )

    fig_bar.update_layout(
        showlegend=False,
        height=500,
        xaxis_title="Number of Respondents",
        yaxis_title=""
    )

    fig_bar.update_traces(textposition="outside")

    st.plotly_chart(fig_bar, use_container_width=True)

with chart2:
    st.subheader("Theme Percentage Share")

    fig_pie = px.pie(
        data,
        names="Theme",
        values="Mentions",
        hole=0.35
    )

    fig_pie.update_traces(textinfo="percent+label")
    fig_pie.update_layout(height=500)

    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")

# -----------------------------
# Theme Details
# -----------------------------
st.subheader("Theme Descriptions")

for _, row in data.iterrows():
    st.markdown(
        f"""
        <div class="theme-card">
            <h4>{row['Theme']}</h4>
            <p><strong>Mentions:</strong> {row['Mentions']} respondents ({row['Percentage']}%)</p>
            <p>{row['Description']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Download CSV
# -----------------------------
st.subheader("Download Theme Summary")

csv = data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV File",
    data=csv,
    file_name="thematic_analysis_summary.csv",
    mime="text/csv"
)
