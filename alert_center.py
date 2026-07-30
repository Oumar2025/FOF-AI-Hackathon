import streamlit as st
import pandas as pd

from services.alert_service import AlertService


def show_alert_center():

    st.title("🚨 Alert Center")

    alerts = AlertService.get_active_alerts()

    if not alerts:
        st.success("No active alerts.")
        return

    df = pd.DataFrame(
        alerts,
        columns=[
            "Alert ID",
            "Product ID",
            "Product",
            "Category",
            "Quantity",
            "Unit",
            "Expiry Date",
            "Alert Level",
            "Sent At",
            "Acknowledged",
            "Muted",
            "Resolved"
        ]
    )

    st.dataframe(df, use_container_width=True)