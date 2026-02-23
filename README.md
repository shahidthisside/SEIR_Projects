# SEIR Web Scraper and Simhash

This is a simple Python project that does two things:

1. Scrapes a web page and shows its content
2. Compares two web pages using Simhash to check similarity

The project is built for learning web scraping and document similarity concepts.

---

## Features

### 1. Web Scraper

The scraper:

- Takes a URL from the command line
- Downloads the page
- Prints:
  - Page title
  - Full page text
  - All links found on the page

File: scraping.py

---

### 2. Simhash Document Similarity

This script:

- Takes two URLs
- Downloads both pages
- Cleans the text
- Removes common stop words
- Creates a 64-bit Simhash
- Compares both hashes
- Prints number of common bits

More common bits means more similar content.

File: simhash_commonBits.py

---

## How Simhash Works in This Project

1. Convert text to lowercase
2. Split into words
3. Remove stop words
4. Count word frequency
5. Generate hash for each word
6. Build 64-bit fingerprint
7. Compare using XOR
8. Count matching bits

---

## Installation

Make sure Python 3 is installed.

Install required libraries:

pip install -r requirements.txt

---

## How To Run

### Run Web Scraper

python3 scraping.py https://example.com

---

### Run Simhash Comparison

python3 simhash_commonBits.py https://site1.com https://site2.com

Example:

python3 simhash_commonBits.py https://www.google.com https://www.youtube.com

---

## Requirements

- Python 3
- requests
- beautifulsoup4

---

## Purpose

This project is created for learning:

- Web scraping
- Text cleaning
- Hashing techniques
- Document similarity
- Basic information retrieval
