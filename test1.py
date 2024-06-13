import time

long_paragraph = """
This is a long paragraph that spans multiple lines.
It contains a lot of text that you want to print cleanly.
By using triple quotes, you can break the paragraph into
multiple lines without worrying about escaping special characters.
This makes the code more readable and maintainable.
"""

for char in long_paragraph:
    print(char, end='', flush=True)
    time.sleep(0.05)  # Adjust the sleep time as per your preference