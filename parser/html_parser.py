import re
from html.parser import HTMLParser

from config import email_patterns, BASE_DIR


class EmailParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.html_data = []
        self.in_body = False

    def handle_starttag(self, tag, attrs):
        self.html_data.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        self.html_data.append(f"</{tag}>")

    def handle_data(self, data):
        self.html_data.append(data)

    def get_html(self):
        return ''.join(self.html_data)

    def parse_html(self, html):
        self.feed(html)
        return self.get_html()


class EmailReplyParser:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.html_content = file.read()
        self.email_parser = EmailParser()
        self.email_parser.parse_html(self.html_content)
        self.parsed_html = self.email_parser.get_html()
        self.body_content = ""
        self.replies_content = []

    def extract_parts(self):
        extracted_strings = []
        for pattern in email_patterns:
            compiled_pattern = re.compile(pattern, re.MULTILINE | re.DOTALL | re.IGNORECASE)
            matches = compiled_pattern.findall(self.parsed_html)
            extracted_strings.extend(matches)

        return self.format_strings(extracted_strings)

    @staticmethod
    def save_to_file(text):
        with open(f'{BASE_DIR}/example.txt', 'w') as file:
            for idx, quote in enumerate(text):
                file.write(f"{quote}\n\n")

    @staticmethod
    def format_strings(strings):
        formatted_strings = []
        for string in strings:
            clean_string = re.sub(r'<(?!a(?:\s|>))[^>]*>', '', string)
            clean_string = re.sub(r'(\s+)([\w.-]+@[^\s<>\"]+)', r'\1<\2', clean_string)
            clean_string = re.sub(r'\s+', ' ', clean_string)
            clean_string = re.sub(r'<.*?>', ' ', clean_string)
            clean_string = re.sub(r'\s{2,}', '\n\n', clean_string)
            clean_string = re.sub(r'.*\s+{.*:.*\}', '', clean_string)
            clean_string = clean_string.strip()
            formatted_strings.append(clean_string)

        return formatted_strings

    def get_body(self):
        return self.body_content

    def get_replies(self):
        return self.replies_content

