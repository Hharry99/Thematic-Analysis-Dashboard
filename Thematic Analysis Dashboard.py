import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Pavement Performance Management Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# DATA
# ---------------------------------------------------
data = pd.DataFrame({
    "Theme": [
        "AI, Analytics & Forecasting",
        "Improved Data Collection & Record Keeping",
        "Technical Capacity & Training",
        "Centralized & Integrated Data Systems",
        "Budget & Resource Support",
        "Policy, Institutional Reform & Coordination"
    ],
    "Mentions": [31, 23, 22, 21, 16, 14]
})

data["Percentage"] = round((data["Mentions"] / 56) * 100, 1)

# ---------------------------------------------------
# STYLING
# ---------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.block-container {
    padding-top: 0rem;
    padding-left: 3rem;
    padding-right: 3rem;
    padding-bottom: 3rem;
}

/* Top Bar */
.top-bar {
    background: #071633;
    height: 72px;
    margin: -1rem -3rem 3rem -3rem;
    border-bottom: 4px solid #d97706;
    display: flex;
    align-items: center;
    padding-left: 3rem;
    color: white;
    font-size: 28px;
    font-weight: 800;
    letter-spacing: 1px;
}

/* Research badge */
.badge {
    display: inline-block;
    background: #fff7ed;
    color: #b45309;
    border: 1px solid #fbbf24;
    border-radius: 999px;
    padding: 10px 22px;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 2rem;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 68px;
    font-weight: 900;
    line-height: 1.05;
    color: #020617;
    margin-bottom: 1rem;
}

.subtitle {
    text-align: center;
    font-size: 28px;
    font-weight: 700;
    color: #c2410c;
    margin-bottom: 0.3rem;
}

.subtitle-line {
    width: 340px;
    height: 3px;
    background: #fdba74;
    margin: 0 auto 3rem auto;
    border-radius: 20px;
}

.info-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 26px;
    padding: 2rem;
    box-shadow: 0 10px 30px rgba(15,23,42,0.06);
    margin-bottom: 2rem;
}

.section-header {
    font-size: 34px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 0.3rem;
}

.section-sub {
    font-size: 18px;
    color: #64748b;
    margin-bottom: 2rem;
}

.metric-card {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    border-radius: 22px;
    padding: 2rem;
    text-align: center;
    color: white;
    box-shadow: 0 12px 30px rgba(15,23,42,0.18);
    margin-bottom: 1rem;
}

.metric-title {
    color: #cbd5e1;
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 1rem;
}

.metric-value {
    font-size: 56px;
    font-weight: 800;
}

.metric-highlight {
    color: #38bdf8;
}

.chart-box {
    background: white;
    border-radius: 26px;
    padding: 1.5rem;
    box-shadow: 0 10px 30px rgba(15,23,42,0.08);
    border: 1px solid #e2e8f0;
}

.chart-title {
    font-size: 32px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 0.4rem;
}

.chart-subtitle {
    color: #64748b;
    font-size: 16px;
    margin-bottom: 1.2rem;
}

.theme-card {
    background: white;
    border-radius: 22px;
    padding: 1.5rem 1.8rem;
    border-left: 8px solid #ea580c;
    box-shadow: 0 10px 24px rgba(15,23,42,0.06);
    border: 1px solid #e2e8f0;
    margin-bottom: 1rem;
}

.theme-title {
    color: #0f172a;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 0.4rem;
}

.theme-meta {
    color: #c2410c;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 0.6rem;
}

.theme-text {
    color: #475569;
    font-size: 16px;
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown('<div class="top-bar">SURVEY</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align:center;">
        <div class="badge">📋 DOCTORAL RESEARCH</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="main-title">
        Pavement Performance<br>
        Management under Data<br>
        Constraints
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Perspectives of Practitioners in Kenya</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="subtitle-line"></div>', unsafe_allow_html=True)

# ---------------------------------------------------
# INTRO CARD
# ---------------------------------------------------
st.markdown(
    """
    <div class="info-card">
        <div class="section-header">Thematic Analysis of Open-Ended Responses</div>
        <div class="section-sub">
            Q27 and Q28 responses from 56 practitioners were coded and grouped into six major thematic areas relating to pavement performance management under data constraints.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# METRICS
# ---------------------------------------------------
m1, m2, m3 = st.columns(3)

with m1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Total Responses</div>
        <div class="metric-value">56</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Total Themes</div>
        <div class="metric-value">{len(data)}</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Most Mentioned Theme</div>
        <div class="metric-value metric-highlight">AI & Forecasting</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------
# CHARTS
# ---------------------------------------------------
colors = ["#2563eb", "#7c3aed", "#ec4899", "#ea580c", "#16a34a", "#d97706"]

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="chart-box">
        <div class="chart-title">Theme Frequency</div>
        <div class="chart-subtitle">Number of respondents mentioning each theme</div>
    """, unsafe_allow_html=True)

    fig_bar = px.bar(
        data.sort_values("Mentions"),
        x="Mentions",
        y="Theme",
        orientation="h",
        text="Mentions",
        color="Theme",
        color_discrete_sequence=colors
    )

    fig_bar.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        height=500,
        margin=dict(l=10, r=10, t=10, b=10),
        font=dict(size=14, color="#0f172a"),
        xaxis=dict(
            title="Respondents",
            gridcolor="#e2e8f0"
        ),
        yaxis=dict(title="")
    )

    fig_bar.update_traces(textposition="outside")

    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="chart-box">
        <div class="chart-title">Theme Percentage Share</div>
        <div class="chart-subtitle">Relative contribution of each theme</div>
    """, unsafe_allow_html=True)

    fig_pie = px.pie(
        data,
        names="Theme",
        values="Mentions",
        hole=0.45,
        color="Theme",
        color_discrete_sequence=colors
    )

    fig_pie.update_traces(
        textinfo="percent",
        textfont_size=16
    )

    fig_pie.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        height=500,
        margin=dict(l=10, r=10, t=10, b=10),
        font=dict(color="#0f172a"),
        legend=dict(
            orientation="h",
            y=-0.15
        )
    )

    st.plotly_chart(fig_pie, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------------------------------------
# THEME DETAILS
# ---------------------------------------------------
st.markdown(
    """
    <div class="section-header" style="margin-bottom:0.5rem;">
        Theme Descriptions
    </div>
    <div class="section-sub">
        Summary of the six thematic areas identified from the open-ended responses.
    </div>
    """,
    unsafe_allow_html=True
)

descriptions = {
    "AI, Analytics & Forecasting":
        "Respondents emphasized the need for AI, machine learning, HDM-4 and predictive models to improve maintenance planning and deterioration forecasting.",

    "Improved Data Collection & Record Keeping":
        "Respondents highlighted the need for regular pavement surveys, complete maintenance histories and better continuity of road condition records.",

    "Technical Capacity & Training":
        "Many respondents called for more training in HDM-4, AI, data analytics and pavement management tools for technical staff.",

    "Centralized & Integrated Data Systems":
        "Respondents recommended a shared national road asset database linking condition, maintenance and planning information.",

    "Budget & Resource Support":
        "Several comments stressed the importance of increased funding for data collection, research and technological improvements.",

    "Policy, Institutional Reform & Coordination":
        "Responses suggested stronger policy frameworks, improved coordination across agencies and reduced political influence in maintenance prioritization."
}

for _, row in data.iterrows():
    st.markdown(
        f"""
        <div class="theme-card">
            <div class="theme-title">{row['Theme']}</div>
            <div class="theme-meta">{row['Mentions']} respondents • {row['Percentage']}%</div>
            <div class="theme-text">{descriptions[row['Theme']]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
