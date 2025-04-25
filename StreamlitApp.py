import streamlit as st

# App Title
st.markdown(" **Delivery Time Prediction App**")

# UI Elements
st.markdown("### Select Product Category")
product_category = st.selectbox("", ["Electronics", "Clothing", "Home & Kitchen", "Books", "Other"])

st.markdown("### Choose Customer Location")
customer_location = st.selectbox("", ["Urban", "Suburban", "Rural"])

st.markdown("### Pick a Shipping Method")
shipping_method = st.selectbox("", ["Standard", "Express", "Same-Day"])

st.markdown("### Define Shipping Priority")
shipping_priority = st.selectbox("", ["Normal", "High", "Urgent"])

st.markdown("### Weather Conditions")
weather = st.selectbox("", ["Sunny", "Rainy", "Snowy", "Stormy"])

st.markdown("### Enter Package Weight (kg)")
weight = st.number_input("Weight", min_value=0.1, max_value=100.0, step=0.1)

st.markdown("### Choose Package Size")
package_size = st.selectbox("", ["Small", "Medium", "Large"])

st.markdown("### Enter Distance to Destination (km)")
distance = st.number_input("Distance (km)", min_value=1, max_value=5000,step=1)

st.markdown("### Nearby Warehouse Availability?")
warehouse_available = st.radio("", ["Yes", "No"])

st.markdown("### Delivery Type")
delivery_type = st.selectbox("", ["Residential", "Business"])

# Delivery Time Prediction Logic
base_time = 0
if st.button(" Predict Delivery Time"):
    if shipping_method == "Standard":
        base_time = 3
    elif shipping_method == "Express":
        base_time = 2
    else:
        base_time = 1
        
    if customer_location == "Rural":
        base_time += 2
    if weather in ["Rainy", "Snowy", "Stormy"]:
        base_time += 1
    if weight > 10:
        base_time += 1
    if distance > 1000:
        base_time += 2
    if package_size == "Large":
        base_time += 1
    if warehouse_available == "Yes":
        base_time -= 1
    if delivery_type == "Business":
        base_time -= 1
    if shipping_priority == "Urgent":
        base_time = min(base_time,2)

base_time = max(1,base_time)
st.success(f" Estimated Delivery Time: **{base_time} days**")