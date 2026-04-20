import streamlit as st
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

    fig_pie.update_traces(
        textinfo="percent+label"
    )

    fig_pie.update_layout(height=500)

    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")

# ------------------------------
# Theme details
# ------------------------------
st.subheader("Theme Descriptions")

for _, row in data.iterrows():
    st.markdown(
        f"""
        <div class="theme-box">
            <h4>{row['Theme']}</h4>
            <p><strong>Mentions:</strong> {row['Mentions']} respondents ({row['Percentage']}%)</p>
            <p>{row['Description']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------
# Optional downloadable table
# ------------------------------
st.subheader("Download Theme Summary")

csv = data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="thematic_analysis_summary.csv",
    mime="text/csv"
)
