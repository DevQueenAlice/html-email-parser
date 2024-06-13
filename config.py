from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

email_patterns = [
    # r'On\s+\d{1,2}\s+\w+\s+\d{4},\s+at\s+\d{1,2}:\d{2}.*?wrote:',
    # r'On\s+[A-Za-z]{1,3}\s+\d{1,2}\s+[A-Za-z]{1,3}\s+\d{4},\s+\d{1,2}:\d{1,2}.*?wrote:',
    # r'On\s+\d{1,2}/\d{1,2}/\d{4}\s+\d{1,2}:\d{2}.*?wrote:',
    r'<[a-z]+>.*</[a-z]+>',
]
