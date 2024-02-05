#!/usr/bin/env python
# coding: utf-8

# In[12]:


import datetime
import streamlit as st


# In[16]:


# type customer name 
import streamlit as st

# Title for your app
st.title("Customer Information")

# Create a text input field for the customer's name
customer_name = st.text_input("Enter the customer's name")

# You can then use this customer name in your app. 
# For example, display it back on the screen or process it further.
if customer_name:
    st.write("Customer's Name:", customer_name)


# In[19]:


# Title for your app
st.title("Laundris Pi Setup")

# Create a radio button for the Laundris Pi question
pi = st.radio(
    "Do you already have the Laundris Pi?",
    ["Yes", "No"]
)

# Respond to the user's choice
if pi == 'Yes':
    st.write('You are good to go then!')
else:
    # Ask for the user's address if they don't have the Laundris Pi
    address = st.text_input("What's your address to ship the Laundris Pi?")

    # You can add additional code here to handle the provided address
    if address:
        st.write("Laundris Pi will be shipped to:", address)


# In[21]:


# Title for your app
st.title("Schedule Laundris Pi Installation")

# Date input for the installation
installation_date = st.date_input("Please, choose the installation date:", datetime.date.today())

# Time input for the installation
installation_time = st.time_input("Please, choose the installation time in Central Time Zone:")

# Display the chosen date and time
if installation_date and installation_time:
    st.write(f"Installation is scheduled for {installation_date} at {installation_time}.")


# In[22]:


if st.button('Submit', 
             disabled=not(customer_name and (pi == 'Yes' or (pi == 'No' and address)) and installation_date and installation_time)):
    # Display the confirmation and process the data
    st.success(f"Thank you, {customer_name}. Your installation is scheduled for {installation_date} at {installation_time}.")
    if pi == 'No':
        st.write(f"Laundris Pi will be shipped to: {address}")


# In[ ]:




