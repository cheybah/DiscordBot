import requests
from bs4 import BeautifulSoup
from shared_data import image_urls, populate_image_urls

# Replace this URL with the Pinterest board or page you want to scrape
pinterest_url = "your_desired_pinterest_board"

response = requests.get(pinterest_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Clear the image_urls list before scraping
image_urls.clear()

# Find image URLs on the page and add them to the list
for img in soup.find_all('img'):
    if 'src' in img.attrs:
        image_urls.append(img['src'])

# Print the scraped image URLs (for debugging)
print(image_urls)


# Pass the image_urls list to the image_downloader.py script
if __name__ == "__main__":
    download_dir = 'downloaded_images'
    from image_downloader import download_known_image
    download_known_image(download_dir)
    # After scraping, call the function to populate image_urls
    scraped_image_urls = image_urls[:] 
    populate_image_urls(scraped_image_urls)
