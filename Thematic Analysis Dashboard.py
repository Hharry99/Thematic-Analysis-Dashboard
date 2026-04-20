import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="Thematic Analysis Dashboard",
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

TOTAL_RESPONSES = 56
data["Percentage"] = round((data["Mentions"] / TOTAL_RESPONSES) * 100, 1)

# ---------------------------------------------------
# CUSTOM CSS FOR DARK MODE
# ---------------------------------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #0f172a;
    color: #f8fafc;
}

.main-title {
    font-size: 46px;
    font-weight: 800;
    color: #60a5fa;
    margin-bottom: 0px;
}

.sub-title {
    font-size: 20px;
    color: #cbd5e1;
    margin-top: 0px;
    margin-bottom: 25px;
}

.metric-card {
    background: linear-gradient(135deg, #1e293b, #111827);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #334155;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
}

.metric-title {
    font-size: 16px;
    color: #94a3b8;
    margin-bottom: 10px;
}

.metric-value {
    font-size: 42px;
    font-weight: bold;
    color: #f8fafc;
}

.metric-highlight {
    color: #38bdf8;
}

.section-title {
    font-size: 34px;
    font-weight: 700;
    color: #e2e8f0;
    margin-top: 30px;
    margin-bottom: 15px;
}

.theme-card {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    padding: 20px;
    border-radius: 16px;
    border-left: 6px solid #38bdf8;
    border: 1px solid #334155;
    margin-bottom: 18px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.35);
}

.theme-title {
    color: #f8fafc;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 10px;
}

.theme-meta {
    color: #93c5fd;
    font-size: 16px;
    margin-bottom: 10px;
}

.theme-description {
    color: #cbd5e1;
    font-size: 15px;
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown(
    '<div class="main-title">Thematic Analysis Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Q27 and Q28 Open-Ended Reflections on Pavement Performance Management in Kenya</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="color:#e2e8f0; font-size:18px; margin-bottom:25px;">Based on 56 survey responses</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# METRICS
# ---------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Total Responses</div>
        <div class="metric-value">56</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Total Themes</div>
        <div class="metric-value">{len(data)}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Most Mentioned Theme</div>
        <div class="metric-value metric-highlight">AI & Forecasting</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------
# COLORS
# ---------------------------------------------------
theme_colors = [
    "#38bdf8",  # cyan
    "#6366f1",  # indigo
    "#ec4899",  # pink
    "#f97316",  # orange
    "#22c55e",  # green
    "#eab308"   # yellow
]

# ---------------------------------------------------
# CHARTS
# ---------------------------------------------------
chart1, chart2 = st.columns(2)

with chart1:
    st.markdown('<div class="section-title">Theme Frequency</div>', unsafe_allow_html=True)

    sorted_data = data.sort_values(by="Mentions", ascending=True)

    fig_bar = px.bar(
        sorted_data,
        x="Mentions",
        y="Theme",
        orientation="h",
        text="Mentions",
        color="Theme",
        color_discrete_sequence=theme_colors
    )

    fig_bar.update_layout(
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font=dict(color="#f8fafc", size=14),
        showlegend=False,
        height=520,
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis=dict(
            title="Number of Respondents",
            gridcolor="#334155",
            zerolinecolor="#334155"
        ),
        yaxis=dict(
            title="",
            tickfont=dict(size=14)
        )
    )

    fig_bar.update_traces(
        textposition="outside"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

with chart2:
    st.markdown('<div class="section-title">Theme Percentage Share</div>', unsafe_allow_html=True)

    fig_pie = px.pie(
        data,
        names="Theme",
        values="Mentions",
        hole=0.45,
        color="Theme",
        color_discrete_sequence=theme_colors
    )

    fig_pie.update_traces(
        textinfo="percent+label",
        textfont=dict(size=14, color="white")
    )

    fig_pie.update_layout(
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font=dict(color="#f8fafc"),
        height=520,
        legend=dict(
            font=dict(size=13),
            bgcolor="#0f172a"
        )
    )

    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("<br><hr style='border:1px solid #334155'><br>", unsafe_allow_html=True)

# ---------------------------------------------------
# THEME DESCRIPTIONS
# ---------------------------------------------------
st.markdown('<div class="section-title">Theme Descriptions</div>', unsafe_allow_html=True)

for _, row in data.iterrows():
    st.markdown(
        f"""
        <div class="theme-card">
            <div class="theme-title">{row['Theme']}</div>
            <div class="theme-meta">
                {row['Mentions']} respondents • {row['Percentage']}%
            </div>
            <div class="theme-description">
                {row['Description']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------------------------------
# DATA TABLE
# ---------------------------------------------------
st.markdown('<div class="section-title">Theme Summary Table</div>', unsafe_allow_html=True)

styled_table = data[["Theme", "Mentions", "Percentage"]]

st.dataframe(
    styled_table,
    use_container_width=True
)

# ---------------------------------------------------
# DOWNLOAD BUTTON
# ---------------------------------------------------
csv = data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Theme Summary CSV",
    data=csv,
    file_name="thematic_analysis_summary.csv",
    mime="text/csv"
)
