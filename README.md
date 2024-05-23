# PRAIRview
Review Pull Requests with AI assistance

## Overview
PRAIRview is a tool designed to streamline the code review process by leveraging the capabilities of OpenAI's GPT-4. It automates the review of pull requests by downloading them as patch files and then using the GPT-4 API to analyze the content.

## Quick Start

```shell
pip3 install -r requirements.txt
python3 main.py
```

## Features
- **Download Pull Requests**: Automatically fetches PRs from your repository and converts them into patch files.
- **AI-Powered Review**: Utilizes OpenAI's GPT-4 to provide insights and suggestions on the patch content.
- **Configurable**: All operations can be customized via a `config.json` file.

## Configuration
To use PRAIRview, you need to set up a `config.json` file with the following parameters:
- `repository_url`: URL of the GitHub repository
- `access_token`: Personal access token for GitHub API
- `openai_api_key`: API key for OpenAI GPT-4

Example `config.json`:

```json
{
"repository_url": "https://github.com/yourusername/yourrepo",
"access_token": "your_github_access_token",
"openai_api_key": "your_openai_api_key"
}
```


## Usage
1. **Set up your configuration file** as described above.
2. **Run the tool** to download the PRs and send them to the OpenAI API.

## Installation
Instructions on how to install and set up PRAIRview in your local environment.

## Contributing
Guidelines for contributing to the PRAIRview project.

## License
Specify the license under which the project is released.

