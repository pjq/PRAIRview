import json
import requests
import openai

def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

config = load_config()
# Set the OpenAI base URL
openai.api_base = config['openai_base_url']

def download_pull_request(pr_number):
    headers = {'Authorization': f'token {config["access_token"]}'}
    pr_endpoint = f"{config['repository_url']}/pulls/{pr_number}"
    response = requests.get(pr_endpoint, headers=headers)
    
    if response.status_code == 200:
        pr = response.json()
        patch_url = pr['patch_url']
        patch_response = requests.get(patch_url, headers=headers)
        if patch_response.status_code == 200:
            patch_file_path = f"PR_{pr['number']}.patch"
            with open(patch_file_path, 'w') as file:
                file.write(patch_response.text)
            print(f"Downloaded PR {pr['number']} as patch file.")
            review_patch_file(patch_file_path)
        else:
            print(f"Failed to download patch for PR {pr['number']}")
    else:
        print(f"Failed to fetch PR {pr_number}")

def review_patch_file(patch_file_path):
    print(f"review the PR patch: {patch_file_path}")
    with open(patch_file_path, 'r') as file:
        patch_content = file.read()
    
    response = openai.Completion.create(
        engine=config['llm_model'],  # Updated to use the model specified in config
        prompt=f"Review the following patch:\n{patch_content}",
        max_tokens=150,
        api_key=config['openai_api_key']
    )
    review_text = response.choices[0].text
    print(f"Review for {patch_file_path}:\n{review_text}")

if __name__ == "__main__":
    pr_number = input("Enter the PR number to download: ")
    download_pull_request(pr_number)