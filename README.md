# Web Scraping Practice

A Python project that demonstrates web scraping techniques by collecting and cleaning NHL team statistics data.

## Overview

This project scrapes historical NHL team statistics from a practice website and processes the data for analysis. It includes pagination handling, data extraction, and cleaning pipelines.

## Files

- `WebScrapping_practice.py` - Scrapes NHL team data from https://www.scrapethissite.com/pages/forms/
- `clean_data.py` - Cleans and processes the scraped data
- `nhl_teams_data.csv` - Output CSV file containing team statistics
- `requirements.txt` - Python dependencies

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Scrape the data:
   ```bash
   python WebScrapping_practice.py
   ```

2. Clean the data:
   ```bash
   python clean_data.py
   ```

## Dependencies

- requests - HTTP library for making web requests
- beautifulsoup4 - HTML parsing and scraping
- pandas - Data manipulation and analysis
- numpy - Numerical computing
- matplotlib - Data visualization

## Notes

This is a practice project for learning web scraping techniques. The data is scraped from a dedicated practice website designed for learning purposes.
