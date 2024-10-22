import os
import time

def take_screenshot(driver, name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_dir = 'screenshots'
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    screenshot_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")