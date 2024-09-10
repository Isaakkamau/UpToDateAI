# UpToDateAI

UpToDateAI is a Python package designed to fetch and provide the latest documentation about recently released programming frameworks to AI models. This package helps bridge the gap between AI model training cut-off dates and the latest developments in the programming world.

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

## How to use it (recommended for cursor.com IDE):

Inside your project, pass the URL of the documentation you want to crawl:

```bash
from uptodateai import process_docs
```

```python
process_docs("https://microsoft.github.io/graphrag/")
```

3. Run the code. A new folder called `/docs` (very well organized in Markdown format)will be generated within your project. This directory we will then use it as our knowledge base for AI models to enhance their understanding of the latest frameworks.

4. We pass the knowledge base to AI using Cursor Composer:

### To use Cursor Composer:

- Enable it in Cursor Settings under the "Beta" section
- Use the shortcut Cmd+I (MacOS) or Ctrl+I (Windows) to open the Composer interface
- Provide instructions (eg build a web app using Fasthtml and mention relevant files for our case we will mention `@/docs`)

5. The cursor composer will generate new files and code in accordance to the library documentation

6. Review and refine the generated code as needed

7. Please give it a star on GitHub if you find it helpful:

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
