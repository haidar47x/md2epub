import os
import re

src = "src"

def starts_with_lowercase(line):
    return line and line[0].islower()

if __name__ == "__main__":
  for filename in os.listdir(src):
    if filename.endswith('.md'):
      file_path = os.path.join(src, filename)
      with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
          stripped_line = line.strip()
          if starts_with_lowercase(stripped_line):
              print(filename)
              print(stripped_line)

