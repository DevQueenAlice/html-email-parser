import re

from email_reply_parser import EmailReplyParser
from parser.html_parser import EmailReplyParser as HtmlEmailReplyParser, EmailParser


def test_email_reply_parser(filename):
    with open(filename, 'r') as f:
        email = f.read()
        email = EmailReplyParser.read(email)
        print(email.reply)


def main():
    html_parser = HtmlEmailReplyParser('messages/test.html')
    html_parser.save_to_file(html_parser.extract_parts())
    html_parser.format_strings(html_parser.extract_parts())
    test_email_reply_parser('example.txt')


if __name__ == '__main__':
    main()
