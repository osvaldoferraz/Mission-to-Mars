# Import Splinter adn BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import numpy as np


# In[2]:


# Set the executable path and initialize the chrome brownse in splinter
executable_path = {'executable_path': '/Users/osvaldoferraz/Desktop/Development/chromedriver'}
browser = Browser('chrome', **executable_path, headless = False)


# ## Visit the Nasa Website

# In[3]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delar for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ## Featured Images

# In[8]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[10]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[11]:


# parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get('src')
img_url_rel


# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# ## Mars Facts

# In[14]:


# scrape a table from the website
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns = ['description', 'value']
df.set_index('description', inplace=True)


# In[15]:


df


# In[16]:


df.to_html()


# ## Mars Weather

# In[17]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[18]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[19]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# In[20]:


get_ipython().system('git add .')
get_ipython().system('git status')
get_ipython().system('git commit -m "Starting Challenge"')
get_ipython().system('git push')


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[21]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# ### Cerberus

# In[22]:


# 1. Use browser to visit the URL 
# url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
# browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# parse html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# find the full res image
full_res_1_link = browser.links.find_by_partial_text('Cerberus')
full_res_1_link.click()

# parse the new page
html = browser.html
res_soup = soup(html, 'html.parser')

# get the full res img and text
full_res = []
for a in res_soup.find_all('a', href=True): 
    if a.text: 
        full_res.append(a['href'])
        
full_res_1 = full_res[4]
full_res_1






#retrieve thumbails url, retrieve text and add to a list (dict)

# ls = list(range(0,4))
# for i in ls:
#     pic_url = img_soup.find_all('img', 'thumb')[i].get('src')
#     full_pic_url = f'
#     text_pic = img_soup.find_all('h3')[i].get_text()
#     hemisphere_image_urls.append({text_pic:full_pic_url})

# hemisphere_image_urls
    

    






# ### Schiaparelli

# In[23]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# parse html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# find the full res image
full_res_2_link = browser.links.find_by_partial_text('Schiaparelli')
full_res_2_link.click()

# parse the new page
html = browser.html
res_soup = soup(html, 'html.parser')

# get the full res img and text
full_res = []
for a in res_soup.find_all('a', href=True): 
    if a.text: 
        full_res.append(a['href'])
        
full_res_2 = full_res[4]
full_res_2


# ### Syrtis

# In[24]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# parse html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# find the full res image
full_res_3_link = browser.links.find_by_partial_text('Syrtis')
full_res_3_link.click()

# parse the new page
html = browser.html
res_soup = soup(html, 'html.parser')

# get the full res img and text
full_res = []
for a in res_soup.find_all('a', href=True): 
    if a.text: 
        full_res.append(a['href'])
        
full_res_3 = full_res[4]
full_res_3


# ### Valles

# In[25]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# parse html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# find the full res image
full_res_3_link = browser.links.find_by_partial_text('Valles')
full_res_3_link.click()

# parse the new page
html = browser.html
res_soup = soup(html, 'html.parser')

# get the full res img and text
full_res = []
for a in res_soup.find_all('a', href=True): 
    if a.text: 
        full_res.append(a['href'])
        
full_res_4 = full_res[4]
full_res_4


# ### Titles

# In[26]:



# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# parse html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

#retrieve text and add to a list (dict)
hemisphere_titles = []

ls = list(range(0,4))
for i in ls:
    text_pic = img_soup.find_all('h3')[i].get_text()
    hemisphere_titles.append(text_pic)

hemisphere_titles


# ### Dictionary

# In[27]:


# 4. Print the list that holds the dictionary of each image url and title.

hemisphere_images = [full_res_1, full_res_2, full_res_3, full_res_4]

hemi_images = []

for i in ls:
    images = {'img_url':hemisphere_images[i], 'title':hemisphere_titles[i]}
    hemi_images.append(images)

hemi_images

    


# In[28]:


# 5. Quit the browser
browser.quit()


# In[29]:


get_ipython().system('git add .')
get_ipython().system('git status')
get_ipython().system('git commit -m "Deliverable 1 Challenge"')
get_ipython().system('git push')

