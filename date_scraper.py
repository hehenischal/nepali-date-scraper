import requests
from bs4 import BeautifulSoup

'''this is the html snippet of the website
<div class="logo">
                    <div class="date">
              <span class="nep">
                  १३ पुष २०८१, शनिवार              </span>
            <br>
            </div>
                        <div style="margin: 10px 0; color: white; font-size: 1.3rem">
                    पुष कृष्ण त्रयोदशी                </div>
                <div style="line-height: 1.9">
                    पञ्चाङ्ग:
          शूल गर अनुराधा                       </div>
            <div class="time">
                <span> बिहानको १० : ५७</span><br>
                <span class="eng"> Dec 28, 2024 </span>
              <br>
            </div>
        </div>'''

# URL of the webpage to scrape
url = "https://www.hamropatro.com"  # Replace with the actual URL

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract the required data
nepali_date = soup.find(class_= "nep").text.strip()
english_date = soup.find(class_= "eng").text.strip()
time_nepali = soup.find(class_= "time").text.strip()
panchang = soup.find(style="line-height: 1.9").text.strip()

# Print the extracted data

file_handler = open('date.txt', 'w')
file_handler.write(f"Nepali Date: {nepali_date}\n")
file_handler.write(f"English Date: {english_date}\n")
file_handler.write(f"Time: {time_nepali}\n")
file_handler.write(f"Panchang: {panchang}\n")
file_handler.close()

print(f"Nepali Date: {nepali_date}")
print(f"English Date: {english_date}")
print(f"Time: {time_nepali}")
print(f"Panchang: {panchang}")
