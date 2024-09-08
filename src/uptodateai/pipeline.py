import os
from urllib.parse import urlparse
from newspaper import Article
from bs4 import BeautifulSoup
import html2text
from slugify import slugify

class MarkdownPipeline:
    def create_directory_from_url_with_slug(self, url):
        parsed_url = urlparse(url)
        path_segments = parsed_url.path.strip('/').split('/')
        directory_path = './docs/' + self.collection
        for segment in path_segments[:-1]:
            directory_path = os.path.join(directory_path, segment)
            os.makedirs(directory_path, exist_ok=True)
        filename = slugify(path_segments[-1])
        return os.path.join(directory_path, filename)

    def open_spider(self, spider):
        self.collection = spider.domain.title().replace('.', '')
        os.makedirs(f'./docs/{self.collection}', exist_ok=True)

    def process_item(self, item, spider):
        url = item.get('url')
        article = Article(url)
        article.download()
        article.parse()

        soup = BeautifulSoup(article.html, 'html.parser')
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')

        if main_content:
            h = html2text.HTML2Text()
            h.ignore_links = False
            h.ignore_images = False
            md_content = h.handle(str(main_content))
        else:
            md_content = article.text

        full_content = f"# {article.title}\n\nSource: {url}\n\n{md_content}"

        directory = self.create_directory_from_url_with_slug(url)

        with open(directory + '.md', 'w', encoding='utf-8') as f:
            f.write(full_content)

        return item