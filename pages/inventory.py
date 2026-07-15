import streamlit as st
import pandas as pd

from models.product import Product
from services.product_service import ProductService
from services.ai_service import AIService
from datetime import datetime


def show_inventory():

    st.title("📦 Inventory Management")

    st.markdown("---")

    products = ProductService.get_all_products()

    product_options = ["New Product"]

    for p in products:
        product_options.append(f"{p[0]} - {p[1]}")

    selected = st.selectbox(
        "📦 Select Product",
        product_options
    )

    selected_row = None

    if selected != "New Product":

        product_id = int(selected.split(" - ")[0])

        for p in products:

            if p[0] == product_id:

                selected_row = p
                break

    st.subheader("Add New Product")

    with st.form("product_form"):

        product_name = st.text_input(
            "Product Name",
            value="" if selected_row is None else selected_row[1]
        )

        category_list = [
            "Biscuit",
            "Chocolate",
            "Candy",
            "Dates"
        ]

        category = st.selectbox(
            "Category",
            category_list,
            index=0 if selected_row is None else category_list.index(selected_row[2])
        )

        brand = st.text_input(
            "Brand",
            value="" if selected_row is None else selected_row[3]
        )

        supplier_list = [
            "Turkey",
            "Morocco",
            "Tunisia",
            "Brazil"
        ]

        supplier_country = st.selectbox(
            "Supplier Country",
            supplier_list,
            index=0 if selected_row is None else supplier_list.index(selected_row[4])
        )

        destination_list = [
            "Mali",
            "Burkina Faso",
            "Côte d'Ivoire",
            "Angola"
        ]

        destination_country = st.selectbox(
            "Destination Country",
            destination_list,
            index=0 if selected_row is None else destination_list.index(selected_row[5])
        )

        quantity = st.number_input(
            "Quantity",
            min_value=0,
            step=1,
            value=0 if selected_row is None else int(selected_row[6])
        )

        unit_list = [
            "Cartons",
            "Boxes",
            "Pallets"
        ]

        unit = st.selectbox(
            "Unit",
            unit_list,
            index=0 if selected_row is None else unit_list.index(selected_row[7])
        )

        cost_price = st.number_input(
            "Cost Price",
            min_value=0.0,
            value=0.0 if selected_row is None else float(selected_row[8])
        )

        selling_price = st.number_input(
            "Selling Price",
            min_value=0.0,
            value=0.0 if selected_row is None else float(selected_row[9])
        )

        manufacture_date = st.date_input(
            "Manufacture Date",
            value=datetime.today().date() if selected_row is None else datetime.strptime(
                selected_row[10], "%Y-%m-%d"
            ).date()
        )

        expiry_date = st.date_input(
            "Expiry Date",
            value=datetime.today().date() if selected_row is None else datetime.strptime(
                selected_row[11], "%Y-%m-%d"
            ).date()
        )

        warehouse = st.text_input(
            "Warehouse",
            value="" if selected_row is None else selected_row[12]
        )
        status_list = [
            "Available",
            "Low Stock",
            "Out of Stock"
        ]

        status = st.selectbox(
            "Status",
            status_list,
            index=0 if selected_row is None else status_list.index(selected_row[13])
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            add_clicked = st.form_submit_button("➕ Add Product")

        with col2:
            update_clicked = st.form_submit_button("✏️ Update")

        with col3:
            delete_clicked = st.form_submit_button("🗑 Delete")

    product = Product(
        product_name=product_name,
        category=category,
        brand=brand,
        supplier_country=supplier_country,
        destination_country=destination_country,
        quantity=quantity,
        unit=unit,
        cost_price=cost_price,
        selling_price=selling_price,
        manufacture_date=str(manufacture_date),
        expiry_date=str(expiry_date),
        warehouse=warehouse,
        status=status
    )

    # -----------------------------
    # ADD
    # -----------------------------
    if add_clicked:

        ProductService.add_product(product)

        st.success("✅ Product added successfully!")

        st.rerun()


    # -----------------------------
    # UPDATE
    # -----------------------------
    if update_clicked:

        if selected_row is None:

            st.warning("Please select a product first.")

        else:

            ProductService.update_product(
                selected_row[0],
                product
            )

            st.success("✅ Product updated successfully!")

            st.rerun()


    # -----------------------------
    # DELETE
    # -----------------------------
    if delete_clicked:

        if selected_row is None:

            st.warning("Please select a product first.")

        else:

            ProductService.delete_product(
                selected_row[0]
            )

            st.success("🗑 Product deleted successfully!")

            st.rerun()

    st.markdown("---")

    st.subheader("📋 Inventory List")

    search = st.text_input(
        "🔍 Search Product",
        placeholder="Type product name..."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        category_filter = st.selectbox(
            "Category",
            ["All", "Biscuit", "Chocolate", "Candy", "Dates"]
        )

    with col2:
        supplier_filter = st.selectbox(
            "Supplier",
            ["All", "Turkey", "Morocco", "Tunisia", "Brazil"]
        )

    with col3:
        status_filter = st.selectbox(
            "Status",
            ["All", "Available", "Low Stock", "Out of Stock"]
        )

    products = ProductService.get_all_products()

    selected_product = None

    if products:

        product_options = {
            f"{row[0]} - {row[1]}": row[0]
            for row in products
        }

        selected_option = st.selectbox(
            "📦 Select Product",
            list(product_options.keys())
        )

        selected_product = ProductService.get_product_by_id(
            product_options[selected_option]
        )

    if products:

        df = pd.DataFrame(
            products,
            columns=[
                "ID",
                "Product",
                "Category",
                "Brand",
                "Supplier",
                "Destination",
                "Quantity",
                "Unit",
                "Cost Price",
                "Selling Price",
                "Manufacture Date",
                "Expiry Date",
                "Warehouse",
                "Status"
            ]
        )

        if search:
            df = df[
                df["Product"].str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        if category_filter != "All":
            df = df[df["Category"] == category_filter]

        if supplier_filter != "All":
            df = df[df["Supplier"] == supplier_filter]

        if status_filter != "All":
            df = df[df["Status"] == status_filter]

        st.dataframe(
            df,
            width="stretch",
            hide_index=True
        )

    else:

        st.info("No products found.")

    if selected_product:

        st.markdown("---")

        st.subheader("📋 Product Details")

        col1, col2 = st.columns(2)

        with col1:

            st.write(f"**Product:** {selected_product[1]}")
            st.write(f"**Category:** {selected_product[2]}")
            st.write(f"**Brand:** {selected_product[3]}")
            st.write(f"**Supplier:** {selected_product[4]}")
            st.write(f"**Destination:** {selected_product[5]}")
            st.write(f"**Quantity:** {selected_product[6]} {selected_product[7]}")

        with col2:

            st.write(f"**Cost Price:** ${selected_product[8]}")
            st.write(f"**Selling Price:** ${selected_product[9]}")
            st.write(f"**Manufacture Date:** {selected_product[10]}")
            st.write(f"**Expiry Date:** {selected_product[11]}")
            st.write(f"**Warehouse:** {selected_product[12]}")
            st.write(f"**Status:** {selected_product[13]}") 

        st.markdown("---")

        st.subheader("🤖 AI Business Insights")

        analysis = AIService.analyze_product(
            selected_product
        )

        st.success(
            f"Stock Level: {analysis['stock']}"
        )

        st.info(
            f"Expiry Status: {analysis['expiry']}"
        )

        st.warning(
            f"Profit Margin: {analysis['margin']}%"
        )

        st.write(
            f"📅 Days Until Expiry: {analysis['days_left']}"
        )

        st.write(
            "### 💡 AI Recommendation"
        )

        st.write(
            analysis["recommendation"]
        )
        st.markdown("---")

        from services.promotion_service import PromotionService

        if st.button(
            f"🎁 Generate Promotion for {selected_product[1]}"
        ):

            with st.spinner("Gemma is creating a marketing campaign..."):

                promotion = PromotionService.generate_promotion(
                    selected_product
                )

            st.success("✅ Promotion Generated")

            facebook = ""
            whatsapp = ""
            slogan = ""
            cta = ""

            section = None

            for line in promotion.splitlines():

                line = line.strip()

                if line == "FACEBOOK_POST:":
                    section = "facebook"
                    continue

                elif line == "WHATSAPP_POST:":
                    section = "whatsapp"
                    continue

                elif line == "SLOGAN:":
                    section = "slogan"
                    continue

                elif line == "CALL_TO_ACTION:":
                    section = "cta"
                    continue

                if section == "facebook":
                    facebook += line + "\n"

                elif section == "whatsapp":
                    whatsapp += line + "\n"

                elif section == "slogan":
                    slogan += line + "\n"

                elif section == "cta":
                    cta += line + "\n"


            st.subheader("📘 Facebook Advertisement")

            st.text_area(
                "Facebook",
                facebook,
                height=180
            )

            st.subheader("💬 WhatsApp Advertisement")

            st.text_area(
                "WhatsApp",
                whatsapp,
                height=180
            )

            st.subheader("🏷 Marketing Slogan")

            st.text_input(
                "Slogan",
                slogan
            )

            st.subheader("📢 Call To Action")

            st.text_area(
                "Call To Action",
                cta,
                height=100
            )


        st.markdown("---")

        st.subheader("🎯 AI Promotion Advisor")

        promotion = AIService.promotion_advisor(
            selected_product
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Suggested Discount",
                promotion["discount"]
            )

        with col2:

            st.metric(
                "Priority",
                promotion["priority"]
            )

        st.info(
            promotion["action"]
        )

        st.markdown("---")

        st.subheader("📦 AI Import Recommendation")

        recommendation = AIService.import_advisor(
            selected_product
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Recommended Import",
                f"{recommendation['recommended_quantity']} Cartons"
            )
            st.metric(
                "Predicted Demand",
                recommendation["predicted_demand"]
            )

            st.metric(
                "Priority",
                recommendation["priority"]
            )

        with col2:

            st.metric(
                "Supplier Country",
                recommendation["supplier"]
            )

            st.metric(
                "Import Time",
                recommendation["timing"]
            )

        st.success(
            f"""
        **Recommendation**

        Import **{recommendation['recommended_quantity']} cartons**
        of this product from **{recommendation['supplier']}**
        {recommendation['timing'].lower()}.
        """
        )      