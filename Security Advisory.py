import requests
import json
import datetime

# API endpoint, API key, and access token
endpoint = "https://api.cisco.com/security/advisories/api/v1/advisories"
api_key = "your_api_key_here"
access_token = "your_access_token_here"

# API request headers
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + access_token
}

def retrieve_data(endpoint, headers, api_key, advisory_id=None):
    # API request parameters
    params = {
        "apiKey": api_key
    }
    
    # If an advisory ID is specified, include it in the API request parameters
    if advisory_id is not None:
        params["advisoryId"] = advisory_id
    
    # Make API call
    response = requests.get(endpoint, headers=headers, params=params)

    # Check API response status code
    if response.status_code == 200:
        print("Success: Data retrieved successfully")
        # Parse the API response data
        data = response.json()
        return data
    else:
        print("Error: Failed to retrieve data. HTTP status code: " + str(response.status_code))
        return None

def write_to_file(data, file_path):
    with open(file_path, "w") as file:
        file.write(json.dumps(data, indent=4))
        print("Data written to file successfully")

def process_data(data):
    # Create an empty dictionary to store the processed data
    processed_data = {}
    
    # Iterate through each advisory in the API response data
    for advisory in data["advisories"]:
        # Get the advisory ID, CVSS score, and published date
        advisory_id = advisory["advisoryId"]
        cvss_score = advisory["cvssScore"]
        published_date = advisory["publishedDate"]
        
        # Convert the published date to a datetime object
        published_datetime = datetime.datetime.strptime(published_date, "%Y-%m-%dT%H:%M:%S.%fZ")
        
        # Get the current date and time
        current_datetime = datetime.datetime.now()
        
        # Calculate the difference between the current date and time and the published date and time
        time_difference = current_datetime - published_datetime
        
        # If the difference is less than 7 days, add the advisory to the processed data dictionary
        if time_difference.days < 7:
            processed_data[advisory_id] = {
                "cvssScore": cvss_score,
                "publishedDate": published_date
            }
    
    return processed_data

# Call the retrieve_data function to get the API response data
data = retrieve_data(endpoint, headers, api_key)

# If the API call was successful, process the data and write it to a file if data is not None:
processed_data = process_data(data)
file_path = "processed_data.json"
write_to_file(processed_data, file_path)

# Send an email to notify the user when the processing is complete
import smtplib

sender_email = "sender@email.com"
receiver_email = "receiver@email.com"
password = "sender_email_password"

message = "Subject: Processing Complete\n\nThe data has been processed and written to file successfully."

try:
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
print("Email sent successfully")
except Exception as e:
print("Error sending email: " + str(e))

Plot the data using a visualization library such as Matplotlib or Seaborn
import matplotlib.pyplot as plt

cvss_scores = [advisory["cvssScore"] for advisory in processed_data.values()]

plt.hist(cvss_scores, bins=10)
plt.xlabel("CVSS Score")
plt.ylabel("Frequency")
plt.title("Distribution of CVSS Scores for Advisories Published in the Last 7 Days")
plt.show()




