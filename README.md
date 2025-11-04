# Glassdoor Job Search Automation

This n8n workflow automates Glassdoor job scraping using **Bright Data** and stores the results in **Google Sheets**.

## Features
- Scrapes job listings by keyword, location, and country  
- Saves results (title, company, location, rating, link) to Google Sheets  
- Includes error handling and retry logic  

## Requirements
- [n8n](https://n8n.io/) instance  
- Bright Data account + dataset ID  
- Google Sheets API credentials  

## Setup
1. Import the workflow JSON into n8n  
2. Add your Bright Data and Google Sheets credentials  
3. Update sheet ID and dataset details  
4. Run or trigger the workflow to start collecting job data  

## Source
- Original n8n workflow: [Automate Glassdoor Job Search with Bright Data & Google Sheets Storage](https://n8n.io/workflows/4843-automate-glassdoor-job-search-with-bright-data-scraping-and-google-sheets-storage/) :contentReference[oaicite:0]{index=0}

## Use Case
Perfect for recruiters, job seekers, or analysts tracking hiring trends.
