import os
import random
import requests
from shared_data import image_urls

def download_known_image(download_dir):
    if not image_urls:
        return None

    # Choose a random image URL from the list
    random_image_url = random.choice(image_urls)

    try:
        # Create a unique filename
        unique_filename = f"image_{random.randint(1, 10000)}.jpg"

        # Construct the local file path to save the image
        local_image_path = os.path.join(download_dir, unique_filename)

        # Download the known image
        response = requests.get(random_image_url)

        if response.status_code == 200:
            with open(local_image_path, 'wb') as file:
                file.write(response.content)
            return local_image_path
        else:
            print(f"Failed to download image from {random_image_url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error while downloading image: {str(e)}")
        return None

if __name__ == "__main__":
    download_dir = 'downloaded_images'
    downloaded_image = download_known_image(download_dir)
    
    if downloaded_image:
        print(f"Image downloaded: {downloaded_image}")
    else:
        print("No images found in the 'image_urls' list.")
        
    print(f"download_dir: {download_dir}")
    print(f"downloaded_image: {downloaded_image}")
