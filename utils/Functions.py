from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from utils.Functions import *
from resources.locators import *
from config import *

linkedin_URL= 'https://www.linkedin.com/'

def LoginToLinkedIN(driver):
  driver.maximize_window()
  driver.get(linkedin_URL)

  # Enter Username
  username= driver.find_element(By.ID, username_field_id)
  username.click()
  username.send_keys(username_key)

  # Enter Password
  password= driver.find_element(By.ID, password_field_id)
  password.click()
  password.send_keys(password_key)

  #Hit Login Button 
  SignInBtn= driver.find_element(By.XPATH, sign_in_button_Xpath)
  SignInBtn.click()


def SearchManagers(driver):

  # Find Search Field
  searchBar=driver.find_element(By.XPATH, search_bar_Xpath)
  searchBar.click()

  # Enter Item for Search
  searchBar.send_keys(f"Manager {company_name}")
  searchBar.send_keys(Keys.RETURN)

  # Click on "See All People"
  FindAllPeople= driver.find_element(By.XPATH, see_all_Button_Xpath)
  FindAllPeople.click()

  # Collect all the Manager Profiles
  ListOfPeeps=driver.find_elements(By.CSS_SELECTOR, people_list_Css_Selector)
  
  # Initialize the emptry list; this will store the Profile links of managers
  profile_links=[]
  
  for person in ListOfPeeps:
    try:
      href_link = person.find_element(By.CSS_SELECTOR, profile_link_Css_Selector).get_attribute("href")

      # Extracting the name
      name = person.find_element(By.CSS_SELECTOR, profile_link_Css_Selector).text

      # Printing or storing the results
      print("Name:", name)
      print("Profile Link:", href_link)
      print("----------")

      profile_links.append(href_link)
      
    except:
      pass

  return profile_links

def SendMessageToManager(driver, people):
 
  actions = ActionChains(driver)
  
  for manager in people:
    
    # Open manager Profile
    driver.get(manager)

    # Click Message Button
    print("Clicking the Message button")
    message_button = driver.find_element(By.XPATH, profile_message_button_Xpath)
    actions.move_to_element(message_button).click().perform()

    # Find the chat box & Type the message
    chat_box= driver.find_element(By.XPATH, chat_box_Xpath)
    actions.move_to_element(chat_box).click().perform()
    chat_box.send_keys(custom_message)

    # Click "Send" Button
    send_btn=driver.find_element(By.XPATH,)
    actions.move_to_element(send_btn).click().perform()
    send_btn.click()