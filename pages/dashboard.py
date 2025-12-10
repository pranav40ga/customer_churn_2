# # import streamlit as st
# # import pandas as pd
# # import matplotlib.pyplot as plt

# # st.title("📊 Customer Churn Dashboard")

# # # Load CSV
# # df = pd.read_csv("Customer_churn.csv")

# # # -----------------------------
# # # Convert Yes/No → 1/0
# # # -----------------------------
# # yes_no_columns = []

# # for col in df.columns:
# #     if df[col].dtype == "object":
# #         unique_vals = set(df[col].dropna().unique())
        
# #         if unique_vals <= {"Yes", "No"}:
# #             df[col] = df[col].map({"Yes": 1, "No": 0})
# #             yes_no_columns.append(col)

# # # Convert Churn to numeric if it's still Yes/No
# # if df["Churn"].dtype == "object":
# #     df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
# #     yes_no_columns.append("Churn")

# # st.write(f"Converted Yes/No columns ➝ 1/0: **{yes_no_columns}**")

# # # -----------------------------
# # # Dataset Preview
# # # -----------------------------
# # st.subheader("📌 Dataset Overview")
# # st.dataframe(df.head())

# # # -----------------------------
# # # Churn Count Plot
# # # -----------------------------
# # st.subheader("Churn Distribution")

# # fig1, ax1 = plt.subplots()
# # df["Churn"].value_counts().plot(kind="bar", ax=ax1)
# # ax1.set_title("Churn vs Non-Churn Customers")
# # ax1.set_xlabel("Churn (1 = Yes, 0 = No)")
# # ax1.set_ylabel("Count")
# # st.pyplot(fig1)

# # # -----------------------------
# # # Monthly Charges vs Churn
# # # -----------------------------
# # st.subheader("Monthly Charges by Churn")

# # if "MonthlyCharges" in df.columns:
# #     fig2, ax2 = plt.subplots()
# #     df.groupby("Churn")["MonthlyCharges"].mean().plot(kind="bar", ax=ax2)
# #     ax2.set_title("Average Monthly Charges by Churn")
# #     ax2.set_xlabel("Churn")
# #     ax2.set_ylabel("Monthly Charges")
# #     st.pyplot(fig2)
# # else:
# #     st.warning("Column 'MonthlyCharges' not found.")

# # # -----------------------------
# # # Tenure vs Churn
# # # -----------------------------
# # st.subheader("Average Tenure by Churn")

# # tenure_col = "tenure" if "tenure" in df.columns else ("Tenure" if "Tenure" in df.columns else None)

# # if tenure_col:
# #     fig3, ax3 = plt.subplots()
# #     df.groupby("Churn")[tenure_col].mean().plot(kind="bar", ax=ax3)
# #     ax3.set_title("Average Tenure by Churn")
# #     ax3.set_xlabel("Churn")
# #     ax3.set_ylabel("Tenure")
# #     st.pyplot(fig3)
# # else:
# #     st.warning("No 'tenure' or 'Tenure' column found.")

# # # -----------------------------
# # # Summary Section
# # # -----------------------------
# # st.subheader("📌 Summary Statistics")

# # churn_rate = df["Churn"].mean() * 100
# # st.write(f"### 🔍 Overall Churn Rate: **{churn_rate:.2f}%**")

# # st.write("### 📊 Numerical Feature Summary:")
# # st.dataframe(df.describe())

# # st.write("### 📈 Churn Group Summary:")

# # # Fix: only numeric cols allowed for mean()
# # numeric_df = df.select_dtypes(include=["int64", "float64"])

# # grouped_mean = numeric_df.groupby(df["Churn"]).mean()

# # st.dataframe(grouped_mean)
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import matplotlib.pyplot as plt

# st.title("📊 Customer Churn Interactive Dashboard")

# # Load CSV
# df = pd.read_csv("Customer_churn2.csv")

# # -----------------------------
# # Convert Yes/No → 1/0
# # -----------------------------
# yes_no_columns = []

# for col in df.columns:
#     if df[col].dtype == "object":
#         unique_vals = set(df[col].dropna().unique())
        
#         if unique_vals <= {"Yes", "No"}:
#             df[col] = df[col].map({"Yes": 1, "No": 0})
#             yes_no_columns.append(col)

# # Convert Churn to numeric if it's still Yes/No
# if df["churn"].dtype == "object":
#     df["churn"] = df["Churn"].map({"Yes": 1, "No": 0})
#     yes_no_columns.append("Churn")

# st.write(f"Converted Yes/No columns ➝ 1/0: **{yes_no_columns}**")

# # -----------------------------
# # Dataset Preview
# # -----------------------------
# st.subheader("📌 Dataset Overview")
# st.dataframe(df.head())

# # -----------------------------
# # Pie Chart - Churn Distribution
# # -----------------------------
# st.subheader("🟠 Churn Distribution (Pie Chart)")

# pie_fig = px.pie(
#     df,
#     names="Churn",
#     title="Churn vs Non-Churn Customers",
#     color="Churn",
#     color_discrete_map={0: "green", 1: "red"}
# )
# st.plotly_chart(pie_fig)

# # -----------------------------
# # Monthly Charges vs Churn (Interactive Bar)
# # -----------------------------
# st.subheader("💰 Average Monthly Charges by Churn")

# if "MonthlyCharges" in df.columns:
#     bar_fig = px.bar(
#         df.groupby("Churn")["MonthlyCharges"].mean().reset_index(),
#         x="Churn",
#         y="MonthlyCharges",
#         color="Churn",
#         title="Avg Monthly Charges by Churn"
#     )
#     st.plotly_chart(bar_fig)
# else:
#     st.warning("Column 'MonthlyCharges' not found.")

# # -----------------------------
# # Tenure vs Churn (Box Plot)
# # -----------------------------
# st.subheader("📦 Tenure Distribution by Churn")

# tenure_col = "tenure" if "tenure" in df.columns else ("Tenure" if "Tenure" in df.columns else None)

# if tenure_col:
#     box_fig = px.box(
#         df,
#         x="Churn",
#         y=tenure_col,
#         color="Churn",
#         title="Tenure Distribution by Churn"
#     )
#     st.plotly_chart(box_fig)
# else:
#     st.warning("No 'tenure' or 'Tenure' column found.")

# # -----------------------------
# # Histogram – Monthly Charges
# # -----------------------------
# st.subheader("📊 Monthly Charges Distribution")

# hist_fig = px.histogram(
#     df,
#     x="MonthlyCharges",
#     nbins=30,
#     color="Churn",
#     title="Monthly Charges Distribution (Churn vs Non-Churn)"
# )
# st.plotly_chart(hist_fig)

# # -----------------------------
# # Summary Section
# # -----------------------------
# st.subheader("📌 Summary Statistics")

# churn_rate = df["Churn"].mean() * 100
# st.write(f"### 🔍 Overall Churn Rate: **{churn_rate:.2f}%**")

# st.write("### 📊 Numerical Feature Summary:")
# st.dataframe(df.describe())

# # Fix: only numeric cols allowed for mean()
# numeric_df = df.select_dtypes(include=["int64", "float64"])

# grouped_mean = numeric_df.groupby(df["Churn"]).mean()

# st.write("### 📈 Churn Group Summary:")
# st.dataframe(grouped_mean)
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.title("📊 Customer Churn Interactive Dashboard")

# Load CSV (already numeric & scaled)
df = pd.read_csv("Customer_churn2.csv")

# --------------------------------------------------
# CLEAN CSV — NO ENCODING NEEDED
# --------------------------------------------------
# Ensure churn column name is consistent
df.columns = df.columns.str.strip().str.lower()

if "churn" not in df.columns:
    st.error("❌ No 'churn' column found in CSV. Please check the file.")
    st.stop()

# --------------------------------------------------
# Dataset Preview
# --------------------------------------------------
st.subheader("📌 Dataset Overview")
st.dataframe(df.head())

# --------------------------------------------------
# Pie Chart - Churn Distribution
# --------------------------------------------------
st.subheader("🟠 Churn Distribution (Pie Chart)")

pie_fig = px.pie(
    df,
    names="churn",
    title="Churn vs Non-Churn Customers",
    color="churn",
    color_discrete_map={0: "green", 1: "red"}
)
st.plotly_chart(pie_fig)

# --------------------------------------------------
# Monthly Charges vs Churn
# --------------------------------------------------
st.subheader("💰 Average Monthly Charges by Churn")

if "monthlycharges" in df.columns:
    bar_fig = px.bar(
        df.groupby("churn")["monthlycharges"].mean().reset_index(),
        x="churn",
        y="monthlycharges",
        color="churn",
        title="Avg Monthly Charges by Churn"
    )
    st.plotly_chart(bar_fig)
else:
    st.warning("Column 'MonthlyCharges' not found in CSV.")

# --------------------------------------------------
# Tenure vs Churn (Box Plot)
# --------------------------------------------------
st.subheader("📦 Tenure Distribution by Churn")

tenure_col = "tenure" if "tenure" in df.columns else None

if tenure_col:
    box_fig = px.box(
        df,
        x="churn",
        y=tenure_col,
        color="churn",
        title="Tenure Distribution by Churn"
    )
    st.plotly_chart(box_fig)
else:
    st.warning("No 'tenure' column found.")

# --------------------------------------------------
# Histogram – Monthly Charges
# --------------------------------------------------
st.subheader("📊 Monthly Charges Distribution")

if "monthlycharges" in df.columns:
    hist_fig = px.histogram(
        df,
        x="monthlycharges",
        nbins=30,
        color="churn",
        title="Monthly Charges Distribution"
    )
    st.plotly_chart(hist_fig)
else:
    st.warning("Column 'monthlycharges' missing.")

# --------------------------------------------------
# Summary Section
# --------------------------------------------------
st.subheader("📌 Summary Statistics")

churn_rate = df["churn"].mean() * 100
st.write(f"### 🔍 Overall Churn Rate: **{churn_rate:.2f}%**")

st.write("### 📊 Numerical Feature Summary:")
st.dataframe(df.describe())

# Only numeric columns
numeric_df = df.select_dtypes(include=["int64", "float64"])

grouped_mean = numeric_df.groupby(df["churn"]).mean()

st.write("### 📈 Churn Group Summary:")
st.dataframe(grouped_mean)
