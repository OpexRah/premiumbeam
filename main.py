from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from flask import Flask, render_template, request
import os
import time


app = Flask(__name__,template_folder='Template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/premium', methods= ['GET', 'POST'])
def run_premium():
    if request.method == "POST":
        room_url = request.form.get('room_url')
        finish = seleniumCall(room_url)
        return finish

def seleniumCall(room_url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_experimental_option('detach', True)


    username= "beepoolbehera@gmail.com"
    password= "hyperbeam123#69"

    url = "https://hyperbeam.com/app/login"
    end_msg = "The bot will leave after 10 mins, to make it join, refresh the page and enter URL again"

    driver = webdriver.Chrome(options=options, executable_path=os.environ.get("CHROMEDRIVER_PATH"))
    
    #driver = webdriver.Chrome(executable_path="chromedriver")

    driver.get(url)

    driver.find_element(By.CSS_SELECTOR, ("input[type='email']")).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, ("input[type='password']")).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ("button[type='submit']")).click()
    time.sleep(5)

    driver.get(room_url)
    time.sleep(5)
    try:
        driver.find_element(By.CLASS_NAME, "joinBtn_1TAU6").click()
        #driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(600)
    except:
        time.sleep(600)
    
    return url

if __name__ == "__main__":
    app.run(debug=True)