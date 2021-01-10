# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
import numpy as np

# Patch to ChromDriver
# which chromedriver

def scrape_all():
    # Set the executable path and initialize the chrome brownse in splinter
    executable_path = {'executable_path': '/Users/osvaldoferraz/Desktop/Development/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = mars_news(browser)

    #Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemi_images": hemisphere_images(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    #Add try/excetp for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:
        return None, None

    return news_title, news_p



### Featured Images

def featured_image(browser):

    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()

    # parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get('src')

    except AttributeError:
        return None
        
    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'    

    return img_url


def mars_facts():
    try:
        # scrape a table from the website
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None

    #Assign columns and set index of dataframe
    df.columns = ['description', 'Mars']
    df.set_index('description', inplace=True)

    #COnvert dataframe into HTML format, add bootstrap
    return df.to_html()

def hemisphere_images(browser):
    # 1. Use browser to visit the URL 
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Cerberus
    # 2. Create a list to hold the images and titles.
    # hemisphere_image_urls = []

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

    
    try:
        # get the full res img and text
        full_res = []
        for a in res_soup.find_all('a', href=True): 
            if a.text: 
                full_res.append(a['href'])

    except AttributeError:
        return None
            
    full_res_1 = full_res[4]
    

    # Schiaparelli

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

    try:
        # get the full res img and text
        full_res = []
        for a in res_soup.find_all('a', href=True): 
            if a.text: 
                full_res.append(a['href'])
    
    except AttributeError:
        return None
            
    full_res_2 = full_res[4]
    

    # Syrtis

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

    try:
        # get the full res img and text
        full_res = []
        for a in res_soup.find_all('a', href=True): 
            if a.text: 
                full_res.append(a['href'])

    except AttributeError:
        return None

    full_res_3 = full_res[4]
    

    # Valles
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

    try:
        # get the full res img and text
        full_res = []
        for a in res_soup.find_all('a', href=True): 
            if a.text: 
                full_res.append(a['href'])

    except AttributeError:
        return None 

    full_res_4 = full_res[4]
    

    # Titles
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
    
    # add to Dictionary
    # 4. Print the list that holds the dictionary of each image url and title.

    hemisphere_images = [full_res_1, full_res_2, full_res_3, full_res_4]

    hemi_images = []

    for i in ls:
        images = {'img_url':hemisphere_images[i], 'title':hemisphere_titles[i]}
        hemi_images.append(dict(images))

    return hemi_images


if __name__ == "__main__":

    #if returning as script, print scraped data
    print(scrape_all())




