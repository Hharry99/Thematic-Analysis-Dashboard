import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------
# Page configuration
# ------------------------------
st.set_page_config(
    page_title="Thematic Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# ------------------------------
# Data
# ------------------------------
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

# ------------------------------
# Custom styling
# ------------------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        color: #1f2937;
        margin-bottom: 0;
    }
    .sub-title {
        font-size: 18px;
        color: #6b7280;
        margin-top: 0;
    }
    .metric-card {
        background-color: #f3f4f6;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #e5e7eb;
    }
    .theme-box {
        background-color: #f9fafb;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2563eb;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# Title
# ------------------------------
st.markdown('<p class="main-title">Thematic Analysis Dashboard</p>', unsafe_allow_html=True)
st.markdown(
)
