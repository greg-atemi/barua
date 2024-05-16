import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Read the Excel file
data = pd.read_excel('kuccps.xlsx')

# Initialize the WebDriver (example uses Chrome)
driver = webdriver.Firefox()

# Open the target website (replace with your Django application's URL)
driver.get('http://127.0.0.1:8000/admission/signup')  # Change to your signup URL

# Iterate through each row in the Excel file
for index, row in data.iterrows():
    username = row['Index Number/Year']
    email = row['Email']
    full_name = row['Student Name']
    index_number = row['Index Number/Year']
    serial_number = row['S.No']
    box_no = row['P.O. Box']
    box_code = row['Postal Code']
    town = row['Town']
    email_address = row['Email']
    course = row['COURSE']
    phone_number = row['Phone Number']
    phone_number2 = row['Phone Number 2']
    gender = row['Gender']
    mode = row['MODE']
    password = row['Index Number/Year']
    password2 = row['Index Number/Year']
    type = row['TYPE']

    # Find the input fields and submit button
    username_field = driver.find_element(By.NAME, 'username')  # Change NAME based on your form
    email_field = driver.find_element(By.NAME, 'email')  # Change NAME based on your form
    full_name_field = driver.find_element(By.NAME, 'full_name')  # Change NAME based on your form
    index_number_field = driver.find_element(By.NAME, 'index_number')  # Change NAME based on your form
    serial_number_field = driver.find_element(By.NAME, 'serial_number')  # Change NAME based on your form
    box_no_field = driver.find_element(By.NAME, 'box_no')  # Change NAME based on your form
    box_code_field = driver.find_element(By.NAME, 'box_code')  # Change NAME based on your form
    town_field = driver.find_element(By.NAME, 'town')  # Change NAME based on your form
    email_address_field = driver.find_element(By.NAME, 'email_address')  # Change NAME based on your form
    course_field = driver.find_element(By.NAME, 'course')  # Change NAME based on your form
    phone_number_field = driver.find_element(By.NAME, 'phone_number')  # Change NAME based on your form
    phone_number2_field = driver.find_element(By.NAME, 'phone_number2')  # Change NAME based on your form
    gender_field = driver.find_element(By.NAME, 'gender')  # Change NAME based on your form
    mode_field = driver.find_element(By.NAME, 'mode')  # Change NAME based on your form
    password_field = driver.find_element(By.NAME, 'password1')  # Change NAME based on your form
    confirm_password_field = driver.find_element(By.NAME, 'password2')  # Change NAME based on your form
    signup_button = driver.find_element(By.NAME, 'submit')  # Change NAME based on your form
    
    # Input the data
    username_field.clear()
    username_field.send_keys(username)
    
    email_field.clear()
    email_field.send_keys(email)
    
    full_name_field.clear()
    full_name_field.send_keys(full_name)
    
    index_number_field.clear()
    index_number_field.send_keys(index_number)

    serial_number_field.clear()
    serial_number_field.send_keys(serial_number)
    
    box_no_field.clear()
    box_no_field.send_keys(box_no)

    box_code_field.clear()
    box_code_field.send_keys(box_code)

    town_field.clear()
    town_field.send_keys(town)

    email_address_field.clear()
    email_address_field.send_keys(email_address)

    course_field.clear()
    course_field.send_keys(course)

    phone_number_field.clear()
    phone_number_field.send_keys(phone_number)

    phone_number2_field.clear()
    phone_number2_field.send_keys(phone_number2)

    gender_field.clear()
    gender_field.send_keys(gender)

    mode_field.clear()
    mode_field.send_keys(mode)

    password_field.clear()
    password_field.send_keys(password)
    
    confirm_password_field.clear()
    confirm_password_field.send_keys(password2)
    
    # Click the signup button
    signup_button.click()
    
    # Add a delay to see the process (optional for debugging)
    # time.sleep(3)
    
    # Navigate back to the signup page for the next iteration
    driver.get('http://127.0.0.1:8000/admission/signup')  # Change to your signup URL

# Close the browser
driver.quit()
