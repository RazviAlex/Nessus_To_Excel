# Nessus_To_Excel

![Pentaho2](https://user-images.githubusercontent.com/51793648/114426147-0c72bb00-9bba-11eb-8f21-7f20166c9c3b.png)

- **Transform raw data from nessus file into excel for the analysis and management of the vulnerabilities.**
- **Include working with a database to store a history and make comparisons between different reports to detect those vulnerabilities that have not been corrected.**

**Launch**
------------------------
1. **From Pentaho Interface:** Open `Spoon.bat` file and run the script by default.
2. **From Terminal:** `Kitchen.bat /file:C:\..\Nessus_to_Excel\Job_Start_GeneralExcel.kjb /level:Basic`

**Instalation**
------------------------
- **Download Pentaho software and DDBB**

To execute the script it is necessary to download the **pentaho software** and a **database**. Pentaho no need instalation and the database can be installed by default (save configuration of the database installed, and if any default data has changed, update it in the configuration file). The script by default is configured to be used **mysql**, if change to another database you have to change the database data in the configuration file **variable.properties** 

- **Download Connector**

The database connector it is necessary because it will allow communication between pentaho and the database. The connector will depend on the database that is configured and it must be saved in the following pentaho path: **\data-integration\lib**

**Configuration file**
------------------------
Customize the execution of the script based on different parameters. 
All this can be done by editing the file **\Nessus_To_Excel\variables.properties**
- Set general parameters

```bash
execute_pythonScript = Y     necessary to transform the json raw data from nessus report.
loadReport_toDDBB = Y        necessary to load raw data from nessus report to DDBB.
generateReport_Excel = Y     necessary to generate Excel report (techincal & executive).
compareReports = N           necessary to compare two different reports and get the vulnerabilities that are reaparing (also need down below to fill the dates between).
```

- Set data generate report. Nnecessary when have multiple reports in the database and only one report is required. **%month day%year**
```bash
data_start = %Jun 20%2019
date_end = %Jun 22%2019
```

- Set data to compare two different reports.
```bash
data_init_report1 = %Apr 24%2019
data_end_report1 = %Apr 24%2019
data_init_report2 = %Jun 21%2020
data_end_report2 = %Jun 21%2020
```

- Set severity between which leveles want to dump the data from report. It has to be configured for the technical and executive report. Nessus severity category: Informative = 0, Low = 1, Medium = 2, High = 3, Critical = 4.
```bash
techincal_severity_min = 1
techincal_severity_max = 4
executive_severity_min = 2
executive_severity_max = 4
```

- Set connection with the database (MySQL). Keep the same DDBB name.
```bash
Host_name = 127.0.0.1
DataBase_name_init = world
DataBase_name = nessus
Port_number = 3306
User_name = root
Password = 
```

**Requirements:**
------------------------
**Pentaho software**
- [Pentaho last version](<https://events.pentaho.com/CE-Download_Data-Integration-ALL-OS.html>)
- [Pentaho all version](https://sourceforge.net/projects/pentaho/files/)

**DDBB** (in this case used MySQL, can use any other, however for that you must find the right connector between the database and pentaho give the link below, and change the configuration file for the new DDBB)
- [MySQL workbench](https://www.mysql.com/products/workbench/)

**DDBB Connector**
- [All conectors for pentaho ](https://dev.mysql.com/downloads/workbench/)
