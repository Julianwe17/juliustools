# Julius Tools API Wrapper

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This Python API Wrapper provides a simple and intuitive interface for interacting with the Julius Tools API. It offers easy access to various endpoints, allowing you to leverage the power of Julius Tools in your Python projects.

## Features

- Simple and intuitive API
- Supports core Julius Tools API endpoints
- Automatic handling of authentication
- Enhanced error handling with detailed error information
- Comprehensive documentation (Soon)

## Installation

Install the Julius Tools API Client using pip:

```bash
pip install juliustools
```

## Quick Start

Here's a quick example to get you started with the Julius Tools API Wrapper:

```python
from juliustools import JuliusToolsAPI

# Initialize the client with your API key
api = JuliusToolsAPI(api_key="your_api_key_here")

# Get API status
status = api.get_status()
print(f"API Status: {status}")

# Perform a crypto operation
result = api.crypto_operation(text="Hello, World!", operation="encrypt")
print(f"Encrypted text: {result['result']}")
print(f"Encryption key: {result['key']}")

# Get a random quote
quote = api.get_random_quote()
print(f"Random quote: {quote['quote']}")

# Get a random joke
joke = api.get_random_joke()
print(f"Random joke: {joke['joke']}")
```

## Documentation

For detailed documentation on all available methods and their usage, please refer to our [official documentation](https://docs.tools.juliusbot.eu/).

## Available Methods

- `get_status()`: Get the API status
- `crypto_operation(text, operation, key=None)`: Perform encryption or decryption
- `get_random_quote()`: Get a random quote
- `get_random_joke()`: Get a random joke
- `add_content(content, content_type)`: Submit new content for approval

## Error Handling

The client provides informative error messages through a custom `APIError` exception. Here's an example of how to handle errors:

```python
from juliustools import JuliusToolsAPI, APIError

try:
    api = JuliusToolsAPI(api_key="invalid_key")
    api.get_status()
except APIError as e:
    print(f"An error occurred: {e}")
    if e.status_code:
        print(f"Status code: {e.status_code}")
    if e.response:
        print(f"Response content: {e.response.content}")
```

The `APIError` exception includes the following attributes:
- `message`: A descriptive error message
- `status_code`: The HTTP status code (if applicable)
- `response`: The full response object (if available)

This allows you to handle different types of errors (e.g., network errors, API errors, invalid API key) in a unified way while still having access to detailed error information when needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.