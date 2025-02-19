# Example usage with UTF-8 handling
from markitdown import MarkItDown
import sys
import io

# Ensure UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

md = MarkItDown()
result = md.convert("medicaldevice.pptx")  # Chinese filename will work too
print(result.text_content)  # Chinese characters will print correctly

# If saving to a file
with open('output.md', 'w', encoding='utf-8') as f:
    f.write(result.text_content)
