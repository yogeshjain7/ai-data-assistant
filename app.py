import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from analysis import load_data, generate_basic_insights, create_fast_summary
from ai_helper import ask_ai

st.set_page_config(page_title="AI Data Assistant", layout="wide")

st.title("📊 AI-Powered Intelligent Data Assistant")

file = st.file_uploader("Upload CSV File", type=["csv"])

def detect_chart_request(question):
    keywords = ["chart", "plot", "graph", "compare"]
    return any(word in question.lower() for word in keywords)

if file:
    df = load_data(file)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    st.write(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")

    st.subheader("🤖 Automatic Insights")
    st.write(generate_basic_insights(df))

    st.subheader("📊 Visual Analysis")

    numeric_columns = df.select_dtypes(include=['number']).columns

    if len(numeric_columns) > 0:
        selected_col = st.selectbox("Select column", numeric_columns)
        st.line_chart(df[selected_col])

    # =========================
    # AI INSIGHTS
    # =========================
    st.subheader("🧠 AI Business Insights")

    if st.button("Generate AI Insights"):
        with st.spinner("Analyzing..."):

            summary = create_fast_summary(df)

            prompt = f"""
            Dataset summary:
            {summary}

            Give business insights, risks and recommendations.
            """

            result = ask_ai(prompt)

        if result["status"] == "success":
            st.markdown("### 🧠 AI Insights")
            st.markdown(result["data"])   # ✅ FIX (NO ORANGE TEXT)

        elif result["status"] == "retry":
            st.warning(result["message"])

        else:
            st.error(result["message"])

    # =========================
    # QUESTION SECTION
    # =========================
    st.subheader("💬 Ask Questions")

    user_question = st.text_input("Ask something about your data")

    if user_question:
        with st.spinner("Thinking..."):

            summary = create_fast_summary(df)

            if detect_chart_request(user_question) and len(numeric_columns) >= 2:

                col1, col2 = numeric_columns[:2]

                st.subheader("📊 Comparison Chart")
                st.line_chart(df[[col1, col2]])

                prompt = f"""
                Compare {col1} and {col2}.
                Summary: {summary}
                """

            else:
                prompt = f"""
                Dataset summary:
                {summary}

                Question:
                {user_question}
                """

            result = ask_ai(prompt)

        if result["status"] == "success":
            st.markdown("### 🧠 Answer")
            st.markdown(result["data"])   # ✅ FIX HERE ALSO

        elif result["status"] == "retry":
            st.warning(result["message"])

        else:
            st.error(result["message"])

else:
    st.info("Upload a CSV file to start.")