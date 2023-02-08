![Razeswag77_Automated_SASE_Monitoring_and_Troubleshooting_using__8d66d38f-c8bc-4491-a125-262ba64029fc](https://user-images.githubusercontent.com/68110223/216912512-68a1c002-47f7-4492-b7e3-15c1901fce56.png)

# Automated-SASE-Monitoring-and-Troubleshooting
This project uses Cisco Secure APIs to automate the monitoring and troubleshooting of Secure Access Service Edge (SASE) deployments. It retrieves real-time network performance and security data, and uses this data to provide customers with visibility into their network, create custom dashboards and alerts and troubleshoot issues. It also enables to take actions to resolve issues, such as adjusting firewall rules or VPN configurations, to ensure optimal network performance and security. The goal of this project is to simplify and automate the management of SASE deployments, making it easier for customers to ensure the security and performance of their network, without the need for extensive IT resources.

#### Security Advisory code is written in Python and makes API calls to retrieve security advisories data from the Cisco Secure API.

The code defines several functions:

- retrieve_data: This function makes an API call to the endpoint specified in the endpoint variable, using the headers and params dictionaries to provide the API key and access token, and any additional parameters. The function returns the API response data if the call was successful, or None if there was an error.
- write_to_file: This function writes the data received as a parameter to a file specified by file_path.
- process_data: This function processes the API response data received as a parameter and returns a dictionary containing only the advisories that were published in the last 7 days and their CVSS score and published date.
- The main body of the code calls the retrieve_data function to get the API response data, checks if the call was successful, and if so, processes the data using the process_data function and writes it to a file using the write_to_file function.

#### Performance SASE code is a simple script that retrieves network performance data from a Cisco API endpoint and analyzes the data for potential issues. 

The script makes an HTTP GET request to the API endpoint using the requests library, passing along an api-key and access-token in the request headers. If the response status code is not 200 (i.e. success), the script raises an exception with an error message.

The response data, in JSON format, is loaded into a Python dictionary using the json.loads method. The script then checks the value of the network_latency key in the dictionary against a threshold value of 100 milliseconds. If the network_latency is greater than the threshold, the script outputs a message indicating a network latency issue and takes an action to resolve the issue (which is currently a placeholder in the form of a TODO comment).

#### How to use:

- 1.) Git clone this repository
- 2.) Add your api_key and access_toke inside the code of Performance SASE.py and Security Advisory.py
- 3.) Run the application with Python: python3 SASE.py or python3 Security Advisory.py
- 4.) Enjoy using the application! 



