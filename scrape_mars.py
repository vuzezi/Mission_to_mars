# Import dependencies
import os
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver

import pandas as pd
import time

def init_browser():
    executable_path = {"executable_path":"C:/Users/Papilo_Data/chromedriver"}
    return Browser("chrome", **executable_path, headless = False)




def scrape():

        facts_data={}
        page_scrape= init_browser()
        #visiting the page
        url = "https://mars.nasa.gov/news/"
        page_scrape.visit(url)
        time.sleep(3)


        #using bs to write it into html
        html = page_scrape.html
        soup = bs(html,"html.parser")


        #Scraping latest news

        news_title = soup.find("div",class_="content_title").text
        news_paragraph = soup.find("div", class_="article_teaser_body").text
        facts_data['news_title'] = news_title
        facts_data['news_paragraph'] = news_paragraph


        # # JPL Mars Space Images - Featured Image


        url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit"
        page_scrape.visit(url_image)
        time.sleep(3)



        #Getting the base url
        from urllib.parse import urlsplit
        base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_image))
        xpath = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"



        #Use splinter to click on the mars featured image
        #to bring the full resolution image
        results = page_scrape.find_by_xpath(xpath)
        img = results[0]
        img.click()
        time.sleep(3)



        #get image url using BeautifulSoup
        html_image = page_scrape.html
        soup = bs(html_image, "html.parser")
        img_url = soup.find("img", class_="fancybox-image")["src"]
        full_img_url = base_url + img_url
        facts_data["featured_image"] = full_img_url


        # # Mars Weather

        #get mars weather's latest tweet from the website
        url_weather = "https://twitter.com/marswxreport?lang=en"
        page_scrape.visit(url_weather)
        html_weather = page_scrape.html
        soup = bs(html_weather, "html.parser")
        mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
        facts_data["mars_weather"] = mars_weather



        # # Mars Facts

        facts_url = "https://space-facts.com/mars/"
        time.sleep(3)
        table = pd.read_html(facts_url)
        df_table = table[0]
        df_table.columns = ["Parameter", "Values"]
        df_table.set_index(["Parameter"])

        table_to_html = df_table.to_html()
        table_to_html = table_to_html.replace("\n", "")
        facts_data["table_to_html"]= table_to_html


        # # Mars Hemispheres


        hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        page_scrape.visit(hemisphere_url)

        #Getting the base url
        hemisphere_base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(hemisphere_url))
        hemisphere_img_urls = []
        hemisphere_img_urls


        # Scraping images


        results = page_scrape.find_by_xpath( "//*[@id='product-section']/div[2]/div[1]/a/img").click()
        time.sleep(2)
        cerberus_open_click = page_scrape.find_by_xpath( "//*[@id='wide-image-toggle']").first.click()
        time.sleep(1)
        cerberus_image = page_scrape.html
        soup = bs(cerberus_image, "html.parser")
        cerberus_url = soup.find("img", class_="wide-image")["src"]
        cerberus_img_url = hemisphere_base_url + cerberus_url
        print(cerberus_img_url)
        cerberus_title = soup.find("h2",class_="title").text
        print(cerberus_title)
        back_button = page_scrape.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
        cerberus = {"image title":cerberus_title, "image url": cerberus_img_url}
        hemisphere_img_urls.append(cerberus)





        results = page_scrape.find_by_xpath( "//*[@id='product-section']/div[2]/div[2]/a/img").click()
        time.sleep(2)
        schiaparelli_open_click = page_scrape.find_by_xpath( "//*[@id='wide-image-toggle']").click()
        time.sleep(1)
        schiaparelli_image = page_scrape.html
        soup = bs(schiaparelli_image, "html.parser")
        schiaparelli_url = soup.find("img", class_="wide-image")["src"]
        schiaparelli_img_url = hemisphere_base_url + schiaparelli_url
        print(schiaparelli_img_url)
        schiaparelli_title = soup.find("h2",class_="title").text
        print(schiaparelli_title)
        back_button = page_scrape.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
        schiaparelli = {"image title":schiaparelli_title, "image url": schiaparelli_img_url}
        hemisphere_img_urls.append(schiaparelli)





        results = page_scrape.find_by_xpath( "//*[@id='product-section']/div[2]/div[3]/a/img").click()
        time.sleep(2)
        syrtis_major_open_click = page_scrape.find_by_xpath( "//*[@id='wide-image-toggle']").click()
        time.sleep(1)
        syrtis_major_image = page_scrape.html
        soup = bs(syrtis_major_image, "html.parser")
        syrtis_major_url = soup.find("img", class_="wide-image")["src"]
        syrtis_major_img_url = hemisphere_base_url + syrtis_major_url
        print(syrtis_major_img_url)
        syrtis_major_title = soup.find("h2",class_="title").text
        print(syrtis_major_title)
        back_button = page_scrape.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
        syrtis_major = {"image title":syrtis_major_title, "image url": syrtis_major_img_url}
        hemisphere_img_urls.append(syrtis_major)





        results = page_scrape.find_by_xpath( "//*[@id='product-section']/div[2]/div[4]/a/img").click()
        time.sleep(2)
        valles_marineris_open_click = page_scrape.find_by_xpath( "//*[@id='wide-image-toggle']").click()
        time.sleep(1)
        valles_marineris_image = page_scrape.html
        soup = bs(valles_marineris_image, "html.parser")
        valles_marineris_url = soup.find("img", class_="wide-image")["src"]
        valles_marineris_img_url = hemisphere_base_url + syrtis_major_url
        print(valles_marineris_img_url)
        valles_marineris_title = soup.find("h2",class_="title").text
        print(valles_marineris_title)
        back_button = page_scrape.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
        valles_marineris = {"image title":valles_marineris_title, "image url": valles_marineris_img_url}
        hemisphere_img_urls.append(valles_marineris)





        facts_data["hemisphere_img_url"] = hemisphere_img_urls

        return facts_data

