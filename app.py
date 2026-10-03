
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer RFM Segmentation",
    page_icon="📊",
    layout="centered"
)

rfm = pd.read_csv("customer_rfm_segments.csv")

campaign_details = {
    "VIP Loyalty Campaign": {
        "objective": "Retain high-value customers.",
        "action": "Offer exclusive rewards, early access, personalized bundles and loyalty benefits."
    },
    "Loyalty Upgrade": {
        "objective": "Increase customer value and retention.",
        "action": "Reward repeat purchases and encourage higher-value purchases through personalized bundles."
    },
    "Win-Back Campaign": {
        "objective": "Reactivate valuable customers who have become inactive.",
        "action": "Send a personalized reminder with a limited-time reactivation incentive."
    },
    "Come-Back Campaign": {
        "objective": "Re-engage inactive customers.",
        "action": "Send relevant product recommendations with a moderate comeback incentive."
    },
    "Engagement Campaign": {
        "objective": "Increase purchase frequency.",
        "action": "Use personalized recommendations and a small purchase incentive."
    },
    "Second-Purchase Campaign": {
        "objective": "Convert recent customers into repeat buyers.",
        "action": "Recommend complementary products or bundles and encourage a second purchase."
    },
    "Welcome-to-Loyalty Campaign": {
        "objective": "Encourage a first repeat purchase.",
        "action": "Provide a welcome reward and an incentive for the next purchase."
    },
    "Last-Chance Win-Back": {
        "objective": "Attempt to recover highly inactive customers.",
        "action": "Send one targeted recovery offer and reduce further marketing if there is no response."
    }
}

st.title("📊 Customer RFM Segmentation Tool")

st.write(
    "Enter a customer ID to view their RFM profile, "
    "customer segment and recommended campaign."
)

customer_id = st.text_input(
    "Enter a customer ID",
    placeholder="Example: CUST0387"
).strip().upper()

if st.button("🔍 Look Up Customer"):

    if customer_id == "":
        st.warning("Please enter a customer ID.")

    else:
        customer = rfm[rfm["customer_id"] == customer_id]

        if customer.empty:
            st.error(
                "Customer ID not found. Please check the ID and try again."
            )

        else:
            customer = customer.iloc[0]

            st.success(
                f"Customer found: {customer['customer_id']}"
            )

            st.subheader("Customer Segment")
            st.info(f"### {customer['Segment']}")

            st.subheader("RFM Profile")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Recency",
                    f"{int(customer['Recency'])} days"
                )

            with col2:
                st.metric(
                    "Frequency",
                    f"{int(customer['Frequency'])} orders"
                )

            with col3:
                st.metric(
                    "Monetary",
                    f"₹{customer['Monetary']:,.2f}"
                )

            st.subheader("RFM Scores")

            st.write(
                f"**R Score:** {customer['R_Score']}  |  "
                f"**F Score:** {customer['F_Score']}  |  "
                f"**M Score:** {customer['M_Score']}"
            )

            st.write(
                f"**Combined RFM Score:** {customer['RFM_Score']}"
            )

            campaign = customer["Recommended_Campaign"]

            st.subheader("Recommended Campaign")
            st.success(campaign)

            st.write(
                f"**Objective:** "
                f"{campaign_details[campaign]['objective']}"
            )

            st.write(
                f"**Recommended Action:** "
                f"{campaign_details[campaign]['action']}"
            )

st.divider()

st.caption(
    "RFM = Recency, Frequency and Monetary Value. "
    "Segments are generated using quintile-based RFM scoring "
    "and rule-based customer segmentation."
)
