# MBW Employee Service

## Description

MBW Employee Service is a Frappe app that allows employees to access and manage their own HR-related information and perform various self-service tasks. This app requires ERPNext and HRMS to be installed and running.

## Installation

1. **Prerequisites**

    Before installing the MBW Employee Service app, make sure you have the following requirements met:
    - Frappe framework is installed and set up on your system.
    - ERPNext v14.45.4 (HEAD)
    - HRMS v14.14.0 (HEAD)
    - FCM Notification 

2. **Install the App**
    Run the following commands to install the MBW Employee Service app:<br/>
    - <b>bench get-app https://github.com/MOBIWORK/MBW_Employee.git</b><br/>
    - <b>bench --site <site_name> install-app mbw_employee</b>

Note: Replace `<site_name>` with the name of your Frappe site.

3. **Run Bench Migrate**

    After the installation, run the following command to migrate the database:
    bench migrate

4. **Run Bench Setup**

    Setup Python and Node dependencies:
    bench setup requirements

### User Guilde
For the web version
https://mbw-frappe.gitbook.io/user-guide-mbw-employee

For the mobile version
https://mbw-frappe.gitbook.io/user-guide-mbw-employee-mobile

### Comming Soon
Our company is still in the process of development and improvement. Here are some features that we will be launching this month:
- Calculate late and early arrival times
- The feature to approve requests from mobile.
- Explanation of timekeeping in cases of forgetting to clock in or unexpected tasks.
- 
### License

MBW Employee Service is distributed under the GNU/General Public License. See the LICENSE file for more information.

### Support and Contact

For any issues, questions, or feedback, please feel free to reach out via email: dev@mbw.vn


