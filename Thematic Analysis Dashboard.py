import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Thematic Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# DATA
# --------------------------------------------------
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

# --------------------------------------------------
# SOFT, ADAPTIVE COLORS FOR BOTH LIGHT & DARK MODE
# --------------------------------------------------
primary = "#2563eb"
secondary = "#475569"
accent = "#0ea5e9"

theme_colors = [
    "#3b82f6",
    "#8b5cf6",
    "#ec4899",
    "#f97316",
    "#22c55e",
    "#eab308"
]

# --------------------------------------------------
# GLOBAL CSS
# --------------------------------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    font-size: 3.2rem;
    font-weight: 800;
    color: #2563eb;
    margin-bottom: 0.25rem;
    line-height: 1.1;
}

.sub-title {
    font-size: 1.35rem;
    color: #475569;
    margin-bottom: 0.6rem;
    font-weight: 500;
}

.caption {
    color: #64748b;
    font-size: 1rem;
    margin-bottom: 2rem;
}

.metric-card {
    background: linear-gradient(135deg, rgba(37,99,235,0.10), rgba(14,165,233,0.06));
    border: 1px solid rgba(37,99,235,0.18);
    border-radius: 18px;
    padding: 1.5rem 1rem;
    text-align: center;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    height: 100%;
}

.metric-title {
    color: #64748b;
    font-size: 1rem;
    margin-bottom: 0.7rem;
    font-weight: 600;
}

.metric-value {
    color: #111827;
    font-size: 2.8rem;
    font-weight: 800;
}

.metric-highlight {
    color: #0ea5e9;
}

.section-title {
    color: #1e293b;
    font-size: 2rem;
    font-weight: 800;
    margin-top: 1.5rem;
    margin-bottom: 1rem;
}

.chart-card {
    background: rgba(255,255,255,0.65);
    border: 1px solid rgba(148,163,184,0.20);
    border-radius: 18px;
    padding: 1rem;
    box-shadow: 0 4px 14px rgba(0,0,0,0.05);
    backdrop-filter: blur(6px);
}

.theme-card {
    background: rgba(255,255,255,0.70);
    border: 1px solid rgba(148,163,184,0.18);
    border-left: 6px solid #2563eb;
    border-radius: 16px;
    padding: 1.25rem;
    margin-bottom: 1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.theme-title {
    color: #111827;
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 0.35rem;
}

.theme-meta {
    color: #2563eb;
    font-size: 0.95rem;
    font-weight: 600;
    margin-bottom: 0.6rem;
}

.theme-description {
    color: #475569;
    font-size: 0.98rem;
    line-height: 1.6;
}

hr {
    border: none;
    border-top: 1px solid rgba(148,163,184,0.25);
    margin-top: 2rem;
    margin-bottom: 2rem;
}

/* Better visibility in dark mode */
@media (prefers-color-scheme: dark) {
    .sub-title {
        color: #cbd5e1 !important;
    }

    .caption {
        color: #94a3b8 !important;
    }

    .metric-card {
        background: linear-gradient(135deg, rgba(15,23,42,0.92), rgba(30,41,59,0.92));
        border: 1px solid rgba(96,165,250,0.20);
    }

    .metric-title {
        color: #cbd5e1 !important;
    }

    .metric-value {
        color: #f8fafc !important;
    }

    .section-title {
        color: #f8fafc !important;
    }

    .chart-card {
        background: rgba(15,23,42,0.82);
        border: 1px solid rgba(148,163,184,0.15);
    }

    .theme-card {
        background: rgba(15,23,42,0.88);
        border: 1px solid rgba(148,163,184,0.15);
    }

    .theme-title {
        color: #f8fafc !important;
    }

    .theme-description {
        color: #cbd5e1 !important;
    }
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    '<div class="main-title">Thematic Analysis Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Q27 and Q28 Open-Ended Reflections on Pavement Performance Management in Kenya</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="caption">Based on 56 survey responses</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# METRICS
# --------------------------------------------------
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

st.markdown("<hr>", unsafe_allow_html=True)

# --------------------------------------------------
# CHARTS
# --------------------------------------------------
c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="section-title">Theme Frequency</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    sorted_data = data.sort_values("Mentions")

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
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        height=480,
        font=dict(size=13),
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(
            title="Respondents",
            gridcolor="rgba(148,163,184,0.2)"
        ),
        yaxis=dict(title="")
    )

    fig_bar.update_traces(textposition="outside")

    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown('<div class="section-title">Theme Percentage Share</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    fig_pie = px.pie(
        data,
        names="Theme",
        values="Mentions",
        hole=0.45,
        color="Theme",
        color_discrete_sequence=theme_colors
    )

    fig_pie.update_traces(
        textinfo="percent",
        textfont_size=14
    )

    fig_pie.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=480,
        legend=dict(
            orientation="h",
            y=-0.15,
            x=0
        ),
        margin=dict(l=10, r=10, t=10, b=40)
    )

    st.plotly_chart(fig_pie, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --------------------------------------------------
# THEME DESCRIPTIONS
# --------------------------------------------------
st.markdown('<div class="section-title">Theme Descriptions</div>', unsafe_allow_html=True)

for _, row in data.iterrows():
    st.markdown(
        f"""
        <div class="theme-card">
            <div class="theme-title">{row['Theme']}</div>
            <div class="theme-meta">{row['Mentions']} respondents • {row['Percentage']}%</div>
            <div class="theme-description">{row['Description']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<hr>", unsafe_allow_html=True)

# --------------------------------------------------
# TABLE + DOWNLOAD
# --------------------------------------------------
st.markdown('<div class="section-title">Theme Summary Table</div>', unsafe_allow_html=True)

st.dataframe(
    data[["Theme", "Mentions", "Percentage"]],
    use_container_width=True,
    hide_index=True
)

csv = data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Theme Summary CSV",
    data=csv,
    file_name="thematic_analysis_summary.csv",
    mime="text/csv"
)
