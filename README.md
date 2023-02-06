# Automated-SASE-Monitoring-and-Troubleshooting
This project uses Cisco Secure APIs to automate the monitoring and troubleshooting of Secure Access Service Edge (SASE) deployments. It retrieves real-time network performance and security data, and uses this data to provide customers with visibility into their network, create custom dashboards and alerts and troubleshoot issues. It also enables to take actions to resolve issues, such as adjusting firewall rules or VPN configurations, to ensure optimal network performance and security. The goal of this project is to simplify and automate the management of SASE deployments, making it easier for customers to ensure the security and performance of their network, without the need for extensive IT resources.

#### Security Advisory code is written in Python and makes API calls to retrieve security advisories data from the Cisco Secure API.

The code defines several functions:

- retrieve_data: This function makes an API call to the endpoint specified in the endpoint variable, using the headers and params dictionaries to provide the API key and access token, and any additional parameters. The function returns the API response data if the call was successful, or None if there was an error.
- write_to_file: This function writes the data received as a parameter to a file specified by file_path.
- process_data: This function processes the API response data received as a parameter and returns a dictionary containing only the advisories that were published in the last 7 days and their CVSS score and published date.
- The main body of the code calls the retrieve_data function to get the API response data, checks if the call was successful, and if so, processes the data using the process_data function and writes it to a file using the write_to_file function.



