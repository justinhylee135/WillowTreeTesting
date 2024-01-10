import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
import time

# Justin Lee WillowTree Website testing

def test_navigate_from_home_to_about():
    # Initialize and set up
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service) 
    driver.maximize_window()
    driver.get("https://www.willowtreeapps.com/")

    # Wait for About tag
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "About"))
    )  
    aboutLink = driver.find_element(By.LINK_TEXT, "About") 
    aboutLink.click()

    # Exit
    driver.close()
    driver.quit()

def test_home_learnMoreButton():
    # Initialize and set up
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service) 
    driver.maximize_window()
    driver.get("https://www.willowtreeapps.com/")

    # Wait for and handle the cookies banner
    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "truste-consent-button"))
        )
        accept_cookies_button.click()
        # Wait for the page to adjust after accepting cookies
        time.sleep(2)  # Adjust this time as needed
    except Exception as e:
        print("No accept cookies button found or other error:", e)

    # Navigate to learn more
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Learn more"))
    )
    learnMore = driver.find_element(By.LINK_TEXT, "Learn more")

    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView();", learnMore)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    try:
        # Attempt to click the element
        learnMore.click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        # If normal click fails, use JavaScript click
        driver.execute_script("arguments[0].click();", learnMore)

    # Wait for the new tab to open
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # Switch to the new tab
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Compare URLs
    actual_url = driver.current_url
    expected_url_base = "https://www.tobiasdengel.com/"
    assert actual_url.startswith(expected_url_base), "expected URL was not found"

    # Close tab
    driver.close()

    # Switch back to the original tab
    driver.switch_to.window(original_window)

    # Exit
    driver.quit()

def test_ourWork_to_contactUs():
    # Initialize and set up
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service) 
    driver.maximize_window()
    driver.get("https://www.willowtreeapps.com/our-work")

    # Wait for and handle the cookies banner
    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "truste-consent-button"))
        )
        accept_cookies_button.click()
        # Wait for the page to adjust after accepting cookies
        time.sleep(2)  # Adjust this time as needed
    except Exception as e:
        print("No accept cookies button found or other error:", e)

    # Initialize Contact Us Button
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Contact us"))
    )
    contactButton = driver.find_element(By.LINK_TEXT, "Contact us")

    # Scroll to button and click
    driver.execute_script("arguments[0].scrollIntoView();", contactButton)
    contactButton.click()

    # Verify correct URL
    actual_url = driver.current_url
    expected_url = "https://www.willowtreeapps.com/contact"
    assert actual_url == expected_url, "Unexpected URL found"

    # Fill out form
    # First Name
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "First-Name"))
    )
    firstName = driver.find_element(By.ID, "First-Name")
    firstName.send_keys("test_first_name")

    # Last Name
    lastName = driver.find_element(By.ID, "Last-Name")
    lastName.send_keys("test_last_name")

    # Company
    company = driver.find_element(By.ID, "Company")
    company.send_keys("test_company")
    
    # Email
    email = driver.find_element(By.ID, "Email")
    email.send_keys("test_email@gmail.com")

    # Phone Number
    phoneNumber = driver.find_element(By.ID, "Phone-Number")
    phoneNumber.send_keys("123456789")

    # Hear About
    hearAbout = driver.find_element(By.ID, "How-did-you-hear-about-us")
    hearAbout.send_keys("test")

    # Help
    help = driver.find_element(By.ID, "Message")
    help.send_keys("test")
    time.sleep(3)

    # Don't actually submit

def test_insights_searchBar_visitPage():
    # Initialize and set up
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service) 
    driver.maximize_window()
    driver.get("https://www.willowtreeapps.com/insights")

    # Wait for and handle the cookies banner
    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "truste-consent-button"))
        )
        accept_cookies_button.click()
        # Wait for the page to adjust after accepting cookies
        time.sleep(2)  # Adjust this time as needed
    except Exception as e:
        print("No accept cookies button found or other error:", e)

    # Initialize search bar and scroll to it
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.ID, "search-1"))
    )
    searchBar = driver.find_element(By.ID, "search-1")
    driver.execute_script("arguments[0].scrollIntoView();", searchBar)
    searchBar.send_keys("test" + Keys.ENTER)

    # Visit all Pages
    # Collect links array
    visitPageLinks = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.LINK_TEXT, "Visit page"))
    )
    urls = [link.get_attribute('href') for link in visitPageLinks]

    # Visit all collected pages
    for url in urls:
        driver.get(url)


def test_about_playVideo():
    # Initialize and set up
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service) 
    driver.maximize_window()
    driver.get("https://www.willowtreeapps.com/about")

    # Wait for and handle the cookies banner
    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "truste-consent-button"))
        )
        accept_cookies_button.click()
        # Wait for the page to adjust after accepting cookies
        time.sleep(2)  # Adjust this time as needed
    except Exception as e:
        print("No accept cookies button found or other error:", e)

    # Try finding the video player
    videoPlayer = driver.find_element(By.ID, "w-node-_4b2b4366-3e70-698b-a17a-54a194e40f24-d800366a")
    driver.execute_script("arguments[0].scrollIntoView();", videoPlayer)
    videoPlayer.click()
                                               
    time.sleep(10) # Let video play for 10 seconds

    driver.quit()

    