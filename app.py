import streamlit as st

def cost_in_time(hourly_wage, hours_per_day, item_price):
    total_hours = item_price / hourly_wage
    days = int(total_hours // hours_per_day)
    remaining_hours = total_hours % hours_per_day
    hours = int(remaining_hours)
    minutes = int((remaining_hours - hours) * 60)
    return f"{days} days {hours} hours {minutes} minutes"

st.title("Work Time Cost Calculator")

wage = st.number_input("Hourly Wage (£)", value=12.75)
hours_per_day = st.number_input("Hours Worked Per Day", value=7.5)
price = st.number_input("Item Price (£)", value=0)

if st.button("Calculate"):
    result = cost_in_time(wage, hours_per_day, price)
    st.success(result)
