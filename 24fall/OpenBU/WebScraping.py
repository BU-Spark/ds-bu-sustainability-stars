from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

df = pd.read_csv("name.csv")
authors = df["0"].tolist() 
# Initialzie WebDriver
service = Service('./chromedriver')
driver = webdriver.Chrome(service=service)

# Open OpenBU
driver.get('https://open.bu.edu/discover')
time.sleep(2)

# Ensure the page is loaded
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "show-advanced-filters"))
)

# Show Advanced Filters
show_advanced_filters = driver.find_element(By.CLASS_NAME, "show-advanced-filters")
driver.execute_script("arguments[0].scrollIntoView(true);", show_advanced_filters)
time.sleep(1)
driver.execute_script("arguments[0].click();", show_advanced_filters)
time.sleep(1)

# Change "Title" to "Author"
filter_dropdown = driver.find_element(By.ID, "aspect_discovery_SimpleSearch_field_filtertype_1")
for option in filter_dropdown.find_elements(By.TAG_NAME, 'option'):
    if option.get_attribute("value") == "author":
        option.click()
        break


# Empty list
results = []

for author in authors:
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "aspect_discovery_SimpleSearch_field_filter_1"))
    )
    driver.execute_script("arguments[0].value = '';", input_field) #clear
    input_field.send_keys(author)  #input

    # Apply
    apply_button = driver.find_element(By.ID, "aspect_discovery_SimpleSearch_field_submit_apply_filter")
    apply_button.click()
    time.sleep(2)

    # Scraping
    while True:
        items = driver.find_elements(By.TAG_NAME, "h4")  # target title
        for item in items:
            try:
                item.click()
                time.sleep(2)

                # title
                title_element = driver.find_element(By.CLASS_NAME, "page-header")
                title = title_element.text if title_element else None

                # abstract
                try:
                    abstract_element = driver.find_element(By.XPATH, "//h5[text()='Abstract']/following-sibling::div")
                    abstract = abstract_element.text if abstract_element else None
                except:
                    abstract = None  # if no abstract, set as none

                # Ignore poster
                if title or abstract:
                    results.append({"Author": author, "Title": title, "Abstract": abstract})
                
                # back to search page
                driver.back()
                time.sleep(2)

            except:
                continue 

        # Check if there is a Next
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "glyphicon-arrow-right"))
            )
            next_button.click()
            time.sleep(2)
        except:
            break  # If no, break the loop

    # After scrapping one author's all papers, jumpy to the next
    show_advanced_filters = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "show-advanced-filters"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", show_advanced_filters)
    driver.execute_script("arguments[0].click();", show_advanced_filters)
    time.sleep(1)

# Quit chrome
driver.quit()

# Save as csv
df = pd.DataFrame(results)
df.to_csv("./author_search_results6.csv", index=False)
print(" Result in author_search_results4.csv'")
