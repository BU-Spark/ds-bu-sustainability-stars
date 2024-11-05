from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

# Initalize WebDriver
service = Service('./chromedriver')
driver = webdriver.Chrome(service=service)

# Open OpenBU
driver.get('https://open.bu.edu/discover')  

time.sleep(2)

# Step 1: Press "Show Advanced Filters" link
show_advanced_filters = driver.find_element(By.CLASS_NAME, "show-advanced-filters")
show_advanced_filters.click()
time.sleep(1)  

# Author name list
authors = ["MAYANK VARIA"]  

results = []

for author in authors:
    # Step 2: select "Author" as filter
    filter_dropdown = driver.find_element(By.ID, "aspect_discovery_SimpleSearch_field_filtertype_1")
    for option in filter_dropdown.find_elements(By.TAG_NAME, 'option'):
        if option.get_attribute("value") == "author":
            option.click()
            break

    # Step 3: Fill in authors' name
    input_field = driver.find_element(By.ID, "aspect_discovery_SimpleSearch_field_filter_1")
    input_field.clear()  
    input_field.send_keys(author)
    
    # Step 4: Apply to search
    apply_button = driver.find_element(By.ID, "aspect_discovery_SimpleSearch_field_submit_apply_filter")
    apply_button.click()
    
    time.sleep(2) 

    # Step 5: Scrape result of current page
    while True:
        items = driver.find_elements(By.CLASS_NAME, "ds-artifact-title")  
        for item in items:
            title = item.text
            results.append({"Author": author, "Title": title})

        # Step 6: Check is there is "Next"
        try:
            next_button = driver.find_element(By.LINK_TEXT, "Next")  
            next_button.click()
            time.sleep(2)  
        except:
            break  

    # Step 7: Reset
    reset_button = driver.find_element(By.XPATH, "//button[text()='Reset']")
    reset_button.click()
    time.sleep(1)

driver.quit()

# Save as csv
df = pd.DataFrame(results)
df.to_csv("./author_search_results.csv", index=False)
print("Data in 'author_search_results.csv'")
