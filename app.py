import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from analysis import load_data, generate_basic_insights
from ai_helper import ask_ai

st.set_page_config(page_title="AI Data Assistant", layout="wide")

st.title("📊 AI-Powered Intelligent Data Assistant")

file = st.file_uploader("Upload CSV File", type=["csv"])

if file:
    df = load_data(file)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    st.write(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")

    # =========================
    # AUTOMATIC STATISTICAL INSIGHTS
    # =========================
    st.subheader("🤖 Automatic Statistical Insights")

    basic_insights = generate_basic_insights(df)
    st.write(basic_insights)

    # =========================
    # VISUAL SECTION
    # =========================
    st.subheader("📊 Visual Analysis")

    cat_columns = df.select_dtypes(include='object').columns
    numeric_columns = df.select_dtypes(include=['number']).columns

    col1, col2 = st.columns(2)

    with col1:
        if len(cat_columns) > 0:
            st.write("### Category Distribution")
            selected_cat = st.selectbox("Select category column", cat_columns)

            fig1, ax1 = plt.subplots(figsize=(5,3))
            df[selected_cat].value_counts().head(5).plot(kind='bar', ax=ax1)
            ax1.tick_params(axis='x', rotation=45)
            st.pyplot(fig1, use_container_width=True)
        else:
            st.info("No text columns available.")

    with col2:
        if len(numeric_columns) > 0:
            st.write("### Numeric Distribution")
            selected_num = st.selectbox("Select numeric column", numeric_columns)

            fig2, ax2 = plt.subplots(figsize=(5,3))
            df[selected_num].plot(kind='hist', ax=ax2)
            st.pyplot(fig2, use_container_width=True)
        else:
            st.info("No numeric columns available.")

    # =========================
    # AI BUSINESS INSIGHTS
    # =========================
    st.subheader("🧠 AI Business Insight Generator")

    if st.button("Generate AI Insights"):
        with st.spinner("Analyzing deeper patterns..."):
            summary = df.describe(include='all').to_string()

            prompt = f"""
            You are a professional data analyst.

            Dataset summary:
            {summary}

            Basic statistical insights:
            {basic_insights}

            Provide clear business insights, patterns, risks,
            and recommendations based on this dataset.
            """

            ai_insights = ask_ai(prompt)

        st.write("### 🚀 AI Insights")
        st.write(ai_insights)

    # =========================
    # USER QUESTION SECTION
    # =========================
    st.subheader("💬 Ask Custom Questions")

    user_question = st.text_input("Ask something about your dataset")

    if user_question:
        with st.spinner("Thinking..."):
            summary = df.describe(include='all').to_string()

            prompt = f"""
            Dataset summary:
            {summary}

            Question:
            {user_question}

            Answer clearly and professionally.
            """

            answer = ask_ai(prompt)

        st.write("### 🧠 AI Answer")
        st.write(answer)

else:
    st.info("Upload a CSV file to begin analysis.")