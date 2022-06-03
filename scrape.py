from bs4 import BeautifulSoup
import requests

def get_social_from_website(url):
    """
    find the social media links from a webpage and return them as a dictionary
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    social_links = {}
    for link in soup.find_all('a'):
        if link.get('href') and 'facebook.com' in link.get('href'):
            social_links['facebook'] = link.get('href')
        elif link.get('href') and 'twitter.com' in link.get('href'):
            social_links['twitter'] = link.get('href')
        elif link.get('href') and 'instagram.com' in link.get('href'):
            social_links['instagram'] = link.get('href')
        elif link.get('href') and 'linkedin.com' in link.get('href'):
            social_links['linkedin'] = link.get('href')
        elif link.get('href') and 'youtube.com' in link.get('href'):
            social_links['youtube'] = link.get('href')
        elif link.get('href') and 'pinterest.com' in link.get('href'):
            social_links['pinterest'] = link.get('href')
        elif link.get('href') and 'youtube.com' in link.get('href'):
            social_links['youtube'] = link.get('href')
    return social_links



urls = get_social_from_website('https://convurt.io')
print(urls)