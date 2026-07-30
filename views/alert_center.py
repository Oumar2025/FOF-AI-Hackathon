import streamlit as st
from services.alert_service import AlertService


def show_alert_center():

    st.title("🚨 Alert Center")

    alerts = AlertService.get_active_alerts()

    if not alerts:
        st.success("✅ No active alerts.")
        return

    for alert in alerts:

        (
            alert_id,
            product_id,
            product_name,
            category,
            quantity,
            unit,
            expiry_date,
            alert_level,
            sent_at,
            acknowledged,
            muted,
            resolved
        ) = alert

        with st.container(border=True):

            st.subheader(f"📦 {product_name}")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Category:** {category}")
                st.write(f"**Quantity:** {quantity} {unit}")
                st.write(f"**Expiry Date:** {expiry_date}")

            with col2:
                st.write(f"**Alert Level:** {alert_level} Days")
                st.write(f"**Email Sent:** {sent_at}")

                if acknowledged:
                    st.success("Acknowledged")
                else:
                    st.warning("Not Acknowledged")

            b1, b2, b3, b4 = st.columns(4)

            with b1:

                if st.button(
                    "✅ Acknowledge",
                    key=f"ack_{alert_id}"
                ):

                    AlertService.acknowledge_alert(alert_id)
                    st.rerun()

            with b2:

                if st.button(
                    "🔕 Mute",
                    key=f"mute_{alert_id}"
                ):

                    AlertService.mute_alert(alert_id)
                    st.rerun()

            with b3:

                if st.button(
                    "✔ Resolve",
                    key=f"resolve_{alert_id}"
                ):

                    AlertService.resolve_alert(alert_id)
                    st.rerun()

            with b4:

                if st.button(
                    "ℹ️ View Details",
                    key=f"details_{alert_id}"
                ):

                    st.info(f"""
            Product Name: {product_name}

            Category: {category}

            Quantity: {quantity} {unit}

            Expiry Date: {expiry_date}

            Alert Level: {alert_level} Days

            Email Sent: {sent_at}
            """)        