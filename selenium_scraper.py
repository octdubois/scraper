from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome(ChromeDriverManager().install())

# Go to desired website
browser.get("https://github.com/TheDancerCodes")

# Wait 20 seconds for page to load
timeout = 20

# Get all of the titles for the pinned repositories
# We are not just getting pure titles but we are getting a selenium object
# with selenium elements of the titles.

# find_elements_by_xpath - Returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath("//a[@class='text-bold']")

# List Comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]

# print response in terminal
print('TITLES:')
print(titles, '\n')


# Get all of the pinned repo languages
language_element = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
languages = [x.text for x in language_element] # same concept as for-loop/ list-comprehension above.

# print response in terminal
print("LANGUAGES:")
print(languages, '\n')

# Pair each title with its corresponding language using zip function and print each pair
for title, language in zip(titles, languages):
    print("RepoName : Language")
    print(title + ": " + language, '\n')
