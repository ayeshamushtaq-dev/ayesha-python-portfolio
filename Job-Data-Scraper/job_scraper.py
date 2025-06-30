import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://realpython.github.io/fake-jobs/'  # Demo job site
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

jobs = soup.find_all('div', class_='card-content')

job_list = []

for job in jobs:
    title = job.find('h2', class_='title').text.strip()
    company = job.find('h3', class_='company').text.strip()
    location = job.find('p', class_='location').text.strip()
    
    job_list.append({
        'Title': title,
        'Company': company,
        'Location': location
    })

# Save to CSV
df = pd.DataFrame(job_list)
df.to_csv('jobs.csv', index=False)
print("✅ Job data saved to jobs.csv")
