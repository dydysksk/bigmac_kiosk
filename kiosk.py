import streamlit as st

st.title("Order")

st.image("menu.png", width=300)

choice = st.radio(
    "What would you like?", ["Sandwich Only", "Set (Sandwich + Fries + Coke)"]
)

price = 0.0

if choice == "Sandwich Only":
    price = 5.92
elif choice == "Set (Sandwich + Fries + Coke)":
    price = 8.32


sec_a_col1, sec_a_col2 = st.columns(2)

with sec_a_col1:
    quantity = st.slider("How many?", min_value=0, max_value=10, value=1)

with sec_a_col2:
    ketchup = st.number_input("How many ketchup(s)?", min_value=0, max_value=3, value=0)


sec_b_col1, sec_b_col2, sec_b_col3 = st.columns(3)

with sec_b_col1:

    st.subheader("Item Price")
    st.markdown(f"`${price}`")


with sec_b_col2:
    st.subheader("Tax")
    sales_tax_rate = 0.08875
    st.markdown(f"Sale Tax Rate: `{sales_tax_rate * 100.0}%`")
    tax = price * quantity * sales_tax_rate
    st.markdown(f"Tax Amount: `${tax:.2f}`")


with sec_b_col3:
    st.subheader("Total")
    total = price * quantity + tax
    st.markdown(f"You Owe: `${total:.2f}`")

st.button("Place Order")

st.markdown(
    "*Copyright 2022 Jaeyoung Chun | School of Applied Artificial Intelligence | Handong Global University*"
)
