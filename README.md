# IPCAMERA CHECKER

This is a simple web tool to check the domain information and its associated IP address, including the user's public IP and the domain's IP address. It uses JavaScript to fetch data from DNS servers and displays it in a table.

## Features

- Input a domain name to check.
- Fetch and display the user's public IP (UserLocationIP).
- Retrieve the IP address of the provided domain name using DNS queries.
- Display results in a clean, easy-to-read table.

## How to Use

1. Go to the website: [IPCAMERA CHECKER](https://teay.github.io/ipcamera-checkerWith-html-css-js/) (Replace with your actual URL).
2. Enter the domain name you want to check in the input field.
3. Click the "ตรวจสอบโดเมน" (Check Domain) button.
4. View the results in the table below, including:
   - Domain Name
   - Public IP (User Location IP)
   - IP Address of the Domain Name

## How It Works

- The tool uses the following sources to resolve the domain's IP address:
  - [Google DNS](https://dns.google)
  - [Cloudflare DNS](https://1.1.1.1)
  - [OpenDNS](https://resolver1.opendns.com)

The user's public IP is fetched using the [Ipify API](https://api.ipify.org).

## Code

### HTML
The basic structure of the website is built using HTML. It includes:
- A heading
- An input field for the domain name
- A table to display the results
- A button to trigger the domain check

### CSS
The styling of the page is minimal, focusing on readability and a clean interface. The table is used to display the results, and a flexbox layout is applied to the input and button elements for center alignment.

### JavaScript
The JavaScript part performs the following:
- Fetch the user's public IP using the Ipify API.
- Resolve the domain's IP using DNS queries to different DNS services.
- Validate the domain format using a regular expression.
- Display the results in the table dynamically.

## Setup

1. Clone or download the repository.
2. Open the `index.html` file in any modern browser.
3. The website is fully functional without any backend setup. It relies on third-party APIs for IP resolution.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributions

Feel free to open an issue or submit a pull request if you'd like to improve this project. Any contributions are welcome!
