<!-- ABOUT THE PROJECT -->

# About The Project

![Scraper tag][product-screenshot]

This is a console program that collects all courses in [classcentral.com](https://www.classcentral.com) or by subject.

## Built With

- [Python](https://www.python.org)
- [Scrapy](https://scrapy.org)

## Prerequisites

This application requires the following software components:

- Python (I recommend install as a virtual environment).

  To install Python follow instructions at https://www.python.org. After Python installation on your system run these commands in the project folder :

  ```sh
  pip install virtualenv
  virtualenv venv
  ./venv/Scripts/activate
  ```

  Install these Python librarys on your system or virtual environment:

- Scrapy

  ```sh
  pip install scrapy

  ```

## Installation

- See the prerequisites above and clone the repo inside a folder.

```sh
git clone https://github.com/vol-automation/webscraping-classcentral_courses_scraper.git
```

## Usage

### Run program whitin your terminal:

The subjects titles can be found at [https://www.classcentral.com/subjects](https://www.classcentral.com/subjects)

| Scrape by category:

```sh
scrapy crawl subjects -a subject="Mathematics" -o math.csv
```

| Scrape all main subjects:

```sh
scrapy crawl subjects -o all.csv
```

| Script arguments:

1. **-o _filename.csv_**
   - outputs scraped courses to a CSV file
2. **-a subject=_"subject"_**
   - scrape only courses in a specific subject. e.g. **-o category="business"**
3. **-a filter=_"free|paid"_** without this argument scrapes both free and paid courses
   - filter "free" scrapes only free courses e.g. **-a filter="free"**
   - filter "paid" scrapes only paid courses e.g. **-a filter="paid"**

| **Practical examples:**

- scrapes only art and design courses that are paid

  ```sh
  scrapy crawl subjects -a subject="art and design" -a filter="paid" -o art-paid.csv
  ```

- scrapes all courses that are free

  ```sh
  scrapy crawl subjects -a filter="free" -o all-free.csv
  ```

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: images/tag.png
