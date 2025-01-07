# IPCAMERA CHECKER

This is a simple web tool to check the domain information and its associated IP address, including the user's public IP and the domain's IP address. It uses JavaScript to fetch data from DNS servers and displays it in a table.

## Features

- Input a domain name to check.
- Fetch and display the user's public IP (Your Public IP).
- Retrieve the IP address of the provided domain name using DNS queries.
- Display results in a clean, easy-to-read table.

## How to Use

1. Go to the website: [IPCAMERA CHECKER](https://teay.github.io/ipcamera-checker/) (Replace with your actual URL).
2. Enter the domain name you want to check in the input field.
3. Click the "Check Domain" button.
4. View the results in the table below, including:
   - **Domain Name**
   - **Your Public IP**
   - **Domain IP Address**

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

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

### Apache License 2.0

The Apache License 2.0 is a permissive license that allows you to use, modify, and distribute the software both in commercial and non-commercial applications. It also provides an explicit grant of patent rights from contributors to users.

Key points of the Apache License 2.0:

- You may use, modify, and distribute the code under the terms of this license.
- If you distribute modified code, you must include a copy of the license and indicate the changes you made.
- You may not use the names, trademarks, or other identifiers of the project without permission.
- The license includes an explicit grant of patent rights from contributors to users.

For more details, please refer to the [LICENSE](LICENSE) file in this repository.

---

## ใบอนุญาต

โปรเจกต์นี้ได้รับการอนุญาตภายใต้ **Apache License 2.0** - ดูรายละเอียดในไฟล์ [LICENSE](LICENSE)

### Apache License 2.0

**Apache License 2.0** เป็นใบอนุญาตประเภท permissive ที่อนุญาตให้คุณใช้ ปรับแต่ง และแจกจ่ายซอฟต์แวร์นี้ได้ทั้งในแอปพลิเคชันเชิงพาณิชย์และไม่เชิงพาณิชย์ นอกจากนี้ยังให้สิทธิ์ในการใช้สิทธิบัตรจากผู้สนับสนุนแก่ผู้ใช้

จุดสำคัญของ **Apache License 2.0**:

- คุณสามารถใช้ ปรับแต่ง และแจกจ่ายโค้ดภายใต้เงื่อนไขของใบอนุญาตนี้
- หากคุณแจกจ่ายโค้ดที่ปรับแต่งแล้ว คุณต้องรวมสำเนาของใบอนุญาตและระบุการเปลี่ยนแปลงที่คุณได้ทำ
- คุณไม่สามารถใช้ชื่อ เครื่องหมายการค้า หรือสัญลักษณ์อื่นๆ ของโปรเจกต์โดยไม่ได้รับอนุญาต
- ใบอนุญาตนี้รวมถึงการให้สิทธิ์ในการใช้สิทธิบัตรจากผู้สนับสนุนแก่ผู้ใช้

หากต้องการข้อมูลเพิ่มเติม กรุณาดูไฟล์ [LICENSE](LICENSE) ในที่เก็บนี้
