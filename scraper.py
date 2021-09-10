from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Place you instagram phone number, username or email here
_INSTAGRAM_LOGIN = ""
# Place you instagram password here
_INSTAGRAM_PASSWORD = ""


def main():
    # Create selenium firefox webdriver (firefox's geckodriver have to be in the same folder)
    driver = webdriver.Firefox(executable_path="./geckodriver")
    try:
        # Navigate to the instagram login page
        driver.get("https://instagram.com")

        # Wait and retrieve the username field
        username_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="username"]'))
        )
        # Insert phone number, username or email into the field
        username_input.send_keys(_INSTAGRAM_LOGIN)

        # Wait and retrieve the password field
        password_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]'))
        )
        # Insert password into the field
        password_input.send_keys(_INSTAGRAM_PASSWORD)

        # Wait for login button to be clickable
        login_submit = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginForm button[type=submit]'))
        )
        # Click the "Log In" button
        login_submit.click()

        # Wait for logged in page to re-render
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'html.logged-in'))
        )

        # Insert javascript code to navigate to the feed page
        driver.execute_script("window.location.replace('/');")

        not_now_button_selector = 'div[role="dialog"] button:last-child'
        # Wait for the notification popup and not now button
        not_now_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, not_now_button_selector))
        )
        # Click the "Not now" button
        not_now_button.click()

        # Wait for the popup to hide
        WebDriverWait(driver, 5).until_not(
            EC.element_to_be_clickable((By.CSS_SELECTOR, not_now_button_selector))
        )

        # Save the newsfeed screenshot
        driver.save_screenshot("screenshot.png")

    finally:
        # Close the driver after the whole process
        driver.close()


# Execute the main function if the module is not imported but called directly
if __name__ == "__main__":
    main()
