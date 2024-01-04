import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

class LLAMA2:
    def __init__(self):
        self.url = os.environ.get('MODEL_URL')
        self.headers = {
            "Authorization": f"Bearer {os.environ.get('HUGGINGFACEHUB_API_TOKEN')}",
            "Content-Type": "application/json"
        }
        self.payload = {
            "inputs": "",
            "parameters": {
                "return_full_text": True,
                "use_cache": True,
                "max_new_tokens": 25
            }

        }

    def query(self, input: str) -> list:
        try:
            self.payload["inputs"] = input
            data = json.dumps(self.payload)
            response = requests.post(self.url, headers=self.headers, data=data)
            
            # Check if the response status code is OK (200)
            response.raise_for_status()
            
            # Attempt to parse the response as JSON
            data = json.loads(response.content.decode("utf-8"))
            text = data[0]['generated_text']

            print(text)
 
        
        except requests.exceptions.RequestException as e:
            print(f"Error during request: {e}")
            
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    LLAMA2().query("Are dogs smarter than cats??")
