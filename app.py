import streamlit as st
from main import generate_insights
import re

st.set_page_config(page_title="GenAI Insight Generator")

st.markdown(
    """
    <style>
    /* Wrap long links */
    .stMarkdown a {
        word-wrap: break-word;
        white-space: pre-wrap;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("GenAI Insight Generator")

def clean_insights(insights):
    # Remove any ** or * characters around links
    cleaned_insights = re.sub(r'\*{1,2}([^\*]+)\*{1,2}', r'\1', insights)
    return cleaned_insights

industry = st.text_input("Enter an Industry (e.g., Healthcare, Retail, Finance)")

if st.button("Generate Insights"):
    if industry:
        st.write("Generating insights... Please wait.")
        insights = generate_insights(industry)
        if insights:
            # Clean up the insights before displaying them
            cleaned_insights = clean_insights(insights)
            st.write("### Generated Use Cases and Dataset Links")
            st.markdown(cleaned_insights)
            st.success("Insights generated successfully!")
        else:
            st.error("Failed to generate insights.")
    else:
        st.warning("Please enter an industry.")
