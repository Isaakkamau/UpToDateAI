# UpToDateAI

UpToDateAI is a Python package for crawling websites and converting their content into Markdown format. It uses Scrapy for web crawling and various libraries for content extraction and conversion.

## Installation

You can install UpToDateAI using pip:

```bash
pip install uptodateai
```

## Usage

URL of the website you want to crawl:

```python
from uptodateai import process_docs

process_docs("https://docs.fastht.ml/")
```

This will crawl the specified website and save the content as Markdown files in a `docs` directory.

## Features

- Web crawling using Scrapy
- Content extraction using newspaper3k
- HTML to Markdown conversion
- Automatic directory structure creation based on URL paths
- Customizable crawling settings

## Development

To set up the development environment:

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python -m unittest discover tests`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
