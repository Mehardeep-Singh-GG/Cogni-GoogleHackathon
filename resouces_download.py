api_key_giphy = "sApq0geYUF7MOC9m04sxc8t9MJJ4IlCw"

def gif_download(searchquery, api_key, sentence_number):
    import requests

    # Define your GIPHY API key


    # Define the base URL for GIPHY's translation API
    base_url = "https://api.giphy.com/v1/gifs/translate"

    # Define the search term
    search_term = searchquery

    # Define any additional parameters like rating
    params = {
        "api_key": api_key,
        "s": search_term,
        "rating": "g"  # optional, adjust as needed
    }

    # Make the API call
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the GIF URL from the response
        gif_url = data['data']['images']['original']['url']

        # Download the GIF
        gif_response = requests.get(gif_url)

        # Check if the download was successful
        if gif_response.status_code == 200:
            # Save the GIF to a file
            with open(f"downloaded_resources/gifs/{sentence_number}.gif", "wb") as f:
                f.write(gif_response.content)

            print("GIF downloaded successfully.")
        else:
            print("Failed to download GIF:", gif_response.status_code)
    else:
        print("Failed to fetch GIF:", response.status_code)

def image_make(explanation, sentence_number):

gif_download("people dancing", api_key_giphy, 5)