import requests

def fetch_word_data(word):
    # API endpoint
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    try:
        # Send GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract relevant information
            word_data = {
                'word': data[0].get('word'),
                'phonetics': data[0].get('phonetics', []),
                'meanings': data[0].get('meanings', [])
            }
            
            return word_data
        else:
            print(f"Error: Unable to fetch data for word '{word}'. Status Code: {response.status_code}")
            return None
    
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return None