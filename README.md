# Job Finder - Python Web Scraping Automation

**Technologies Used:**  
- Python  
- Selenium  
- Web Scraping  
- Email Automation  
- .env for Configuration Management  

This project automates the process of finding available job openings on any career website using **Python**, **Selenium** to send email notifications whenever new positions are posted.

---

## 🚀 Project Overview

This Python script performs automated job search on **career portal** by continuously monitoring job listings for new opportunities. The main tasks are:

- **Web Scraping**: Using **Selenium** to interact with the job search page.
- **Job Monitoring**: Checking if jobs are available based on specific search criteria.
- **Email Notifications**: Sending automatic email alerts when a job listing is found.
- **Headless Browser**: Running the script in the background with **headless Chrome** (without a visible browser interface).

This project is perfect for showcasing automation skills, web scraping techniques, and integration with APIs like **Mailtrap**.

---

## 🔧 Key Features

- **Automated Web Scraping**: Interacts with job listing page to check availability.
- **Headless Browsing**: The script runs silently in the background without opening a browser window.
- **Real-time Job Monitoring**: Continuously checks for job openings matching specific criteria.
- **Email Alerts**: Notifies you when a new job is found through automated email notifications.
- **Environment Configuration**: Utilizes **dotenv** to manage environment variables like email credentials and browser paths securely.
- **Robust Error Handling**: Handles **NoSuchElementException** gracefully for a reliable, continuous execution.

---

## 🛠️ Technologies & Skills Highlighted

### **Python**
- **Python Programming**: Implemented core logic for web scraping and automation using Python.
- **Error Handling**: Used `try-except` blocks to manage exceptions, ensuring smooth execution and providing meaningful feedback in case of failures.
- **Sleep Intervals**: Integrated `sleep` for timed delays between requests to avoid overloading the server and mimic human browsing behavior.

### **Selenium WebDriver**
- **Web Scraping**: Leveraged **Selenium** to interact with the DOM of the job search page. Extracted data dynamically from elements like job status and applied XPath selectors.
- **Headless Mode**: Configured **headless Chrome** for running the script in the background without opening a browser window.
- **XPath Selectors**: Used XPath to precisely identify and extract job status elements from the webpage.

### **Email Automation**
- **Mailtrap API**: Integrated with **Mailtrap** for sending notification emails.
- **SMTP Configuration**: Used environment variables to store and securely manage sensitive information such as email addresses and API tokens.

### **Environment Variables**
- **dotenv**: Managed environment variables securely with **dotenv**, allowing for easy configuration of sensitive data (like email credentials and Chrome driver paths).

---

## 📈 How It Works

1. **Setup Environment**:  
   The script relies on the `.env` file to configure email credentials, browser driver path.

2. **Headless Browsing**:  
   The **Selenium WebDriver** opens job search page in **headless mode** (invisible browser).

3. **Job Search Automation**:  
   It continuously monitors job availability by checking for the “Sorry, no jobs available” message. When a job is found, an email is sent.

4. **Email Notification**:  
   When a job is found, the script sends an email notification, which can be configured for various email services.

5. **Error Handling**:  
   The script handles potential errors such as missing elements and page load issues.

---

## 💻 Installation

To run this project locally:

### Prerequisites:
- Python 3.x
- **Selenium** (for web scraping)
- **dotenv** (for managing environment variables)
- **Mailtrap**

### 1. Clone the Repository:
`git clone https://github.com/yourusername/job-finder.git`  
`cd job-finder`

### 2. Install Dependencies:
`pip install -r requirements.txt`

### 3. Set Up the `.env` File:
Create a `.env` file in the root directory and add your **Chrome driver path**, **sender/receiver email**, and **Mailtrap API token**:

```
chrome_path=path_to_chrome_driver
sender_mail=your_email@example.com
receiver_mail=recipient_email@example.com
token=your_mailtrap_token
```

### 4. Run the Script:  
```
python job_finder.py

```

The script will continuously check for job openings and send notifications when new positions are available.

---

## 📨 Usage

This project automates the process of checking job availability, making it ideal for job seekers who want to keep track of new openings without manual effort.

Once the script is running, it will monitor the page and send an email notification whenever a job becomes available. You can stop the script at any time by interrupting the process in the terminal.

---

## 📬 Contact

For questions or feedback, feel free to reach out:

- **Dinesh Kumar Gopinathan** — [LinkedIn](https://www.linkedin.com/in/dinesh-kumar-5273a8195/)  

---

Thank you for checking out the **Job Finder**! I hope it helps streamline your job search process, and feel free to contribute to this open-source project!
