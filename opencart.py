import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

URL = 'https://www.opencart.com/' #I assigned the link of the site I want to test to the URL variable.
PATH = r'C:\\Users\\Ferid\\Desktop\\chromedriver.exe' #I assigned the Chrome driver path to the PATH variable.

web = webdriver.Chrome(PATH) #I writed the web variable and showed the chrome driver and assigned it
action = ActionChains(web) #Since I will be using the Action class, I have exposed the chrome driver to ActionChains.
web.get(URL) #To go to the site where I will test

web.maximize_window()#makes the window full size

communityLink = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[3]/section/ul/li[1]/a') #I found the "Community Forum" Link text by taking the xpath of the "Community Forum" Link. How did I get the xpath address? "Community Forum" Link right click->inspect->shows required location->right click on that region->copy->copy xpath
action.double_click(communityLink).perform() #I double clicked the "Community Forum" Link.

time.sleep(2) #after 2 seconds
web.back()#go back page

contact_us_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[2]/section/ul/li[1]/a') #Same process as CommunityLink. I explained there.
action.double_click(contact_us_link).perform()

option = web.find_element_by_xpath('//*[@id="input-reason"]') #I find the Combobox part by taking its path.
optionDD =Select(option) #i choose combobox
optionDD.select_by_visible_text("I would like to report an account issue") #I chose "I would like to report an account issue" from the sentences in the Combobox.

search = web.find_element_by_name('name') #I did the same codes explanations in previous tests 
search.send_keys('feridferid')  
search.send_keys(Keys.RETURN)

search = web.find_element_by_name('email')  
search.send_keys('teste3t@gmail.com')
search.send_keys(Keys.RETURN)

search = web.find_element_by_name('enquiry')
search.send_keys('THİS IS TEST')
search.send_keys(Keys.RETURN)

time.sleep(5)
web.back()

features_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[1]/section/ul/li[1]/a') #Same process as CommunityLink. I explained there.
action.double_click(features_link).perform()

time.sleep(2)
web.back()
 
showcase_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[1]/section/ul/li[2]/a')#Same process as CommunityLink. I explained there.
action.double_click(showcase_link).perform()

time.sleep(2)
web.back()

demo_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[1]/section/ul/li[3]/a') #Same process as CommunityLink. I explained there.
action.double_click(demo_link).perform()

time.sleep(2)
web.back()

downloand_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[1]/section/ul/li[4]/a') #Same process as CommunityLink. I explained there.
action.double_click(downloand_link).perform()

time.sleep(2)
web.back()

marketplace_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[1]/section/ul/li[5]/a') #Same process as CommunityLink. I explained there.
action.double_click(marketplace_link).perform()

time.sleep(2)
web.back()

login_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[1]/section/ul/li[6]/a') #Same process as CommunityLink. I explained there.
action.double_click(login_link).perform()

time.sleep(2)
web.back()

ExtensionAdvertising_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[2]/section/ul/li[2]/a') #Same process as CommunityLink. I explained there.
action.double_click(ExtensionAdvertising_link).perform()

time.sleep(2)
web.back()

MarketplaceAdvertising_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[2]/section/ul/li[3]/a') #Same process as CommunityLink. I explained there.
action.double_click(MarketplaceAdvertising_link).perform()

time.sleep(2)
web.back()

AboutUs_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[2]/section/ul/li[4]/a') #Same process as CommunityLink. I explained there.
action.double_click(AboutUs_link).perform()

time.sleep(2)
web.back()

ExtensionDeveloper_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[2]/section/ul/li[5]/a') #Same process as CommunityLink. I explained there.
action.double_click(ExtensionDeveloper_link).perform()

time.sleep(2)
web.back()

DedicatedSupport_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[3]/section/ul/li[2]/a') #Same process as CommunityLink. I explained there.
action.double_click(DedicatedSupport_link).perform()

time.sleep(2)
web.back()

OpenCartPartners_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[3]/section/ul/li[3]/a') #Same process as CommunityLink. I explained there.
action.double_click(OpenCartPartners_link).perform()

time.sleep(2)
web.back()

MarketplaceSupport_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[3]/section/ul/li[4]/a') #Same process as CommunityLink. I explained there.
action.double_click(MarketplaceSupport_link).perform()

time.sleep(2)
web.back()

MigratetoOpenCart_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[3]/section/ul/li[5]/a') #Same process as CommunityLink. I explained there.
action.double_click(MigratetoOpenCart_link).perform()

time.sleep(2)
web.back()

OpenCartBlog_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[4]/section/ul/li[1]/a') #Same process as CommunityLink. I explained there.
action.double_click(OpenCartBlog_link).perform()

time.sleep(2)
web.back()

OpenCartDocumentation_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[4]/section/ul/li[2]/a') #Same process as CommunityLink. I explained there.
action.double_click(OpenCartDocumentation_link).perform()

time.sleep(2)
web.back()

OpenCartBooks_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[4]/section/ul/li[3]/a') #Same process as CommunityLink. I explained there.
action.double_click(OpenCartBooks_link).perform()

time.sleep(2)
web.back()

GithubBugTracker_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[4]/section/ul/li[4]/a') #Same process as CommunityLink. I explained there.
action.double_click(GithubBugTracker_link).perform()

time.sleep(2)
web.back()

Developer_link = web.find_element_by_xpath('/html/body/footer/div/div[1]/div[4]/section/ul/li[5]/a') #Same process as CommunityLink. I explained there.
action.double_click(Developer_link).perform()

time.sleep(2)
web.back()

element = web.find_element_by_xpath('//*[@id="hero"]/div[1]/div[1]/div/p[2]/a[1]') #I found the "Free Download" element by taking the xpath of the "Free Download" element. How did I get the xpath address? "Free Download" button right click->inspect->shows required location->right click on that region->copy->copy xpath
action.double_click(element).perform() #Finally, I double clicked the "Free Download" button.

time.sleep(2)
web.back()

element = web.find_element_by_xpath('//*[@id="hero"]/div[1]/div[1]/div/p[2]/a[2]') #I found the "VIEW DEMO" element by taking the xpath of the "VIEW DEMO" element. How did I get the xpath address? "VIEW DEMO" button right click->inspect->shows required location->right click on that region->copy->copy xpath
action.double_click(element).perform() #Finally, I double clicked the "VIEW DEMO" button.
 






print("-------Test Finished--------")
