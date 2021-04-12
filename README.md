# Nessus_To_Excel

![Pentaho2](https://user-images.githubusercontent.com/51793648/114426147-0c72bb00-9bba-11eb-8f21-7f20166c9c3b.png)


**Configure script:**
------------------------
Customize the execution of the script based on different parameters. 
This can be done by editing the file **\Nessus_toExcel\variables.properties**
1. General parameters

`execute_pythonScript = Y` -> necessary to transform the json raw data from nessus report.

`loadReport_toDDBB = Y` -> necessary to load raw data from nessus report to DDBB.

`generateReport_Excel = Y` -> necessary to generate Excel report (techincal & executive).

`compareReports = N` -> necessary to compare two different reports and get the vulnerabilities that are reaparing (also need down below to fill the dates between).


2. Data generate report. Nnecessary when have multiple reports in the database and only one report is required. **%Month day%**

`data_start = %Jun 20%
date_end = %Jun 22%`

3. Data to compare two different reports.

`data_init_report1 = %Apr 24%2020
data_end_report1 = %Apr 24%2020
data_init_report2 = %Jun 21%2020
data_end_report2 = %Jun 21%2020`

4. Set severity between which leveles want to dump the data from report. It has to be configured between the technical and executive report  Nessus severity category: Informative = 0, Low = 1, Medium = 2, High = 3, Critical = 4.

`techincal_severity_min = 1
techincal_severity_max = 4
executive_severity_min = 2
executive_severity_max = 4`

5. Set connection with the database (MySQL). Keep the same DDBB name.

`Host_name = 127.0.0.1
DataBase_name_init = world
DataBase_name = nessus
Port_number = 3306
User_name = root
Password = `

**Execute script:**
------------------------
1. **From Pentaho Interface:** Open `Spoon.bat` file and run the script by default.
2. **From CLI:** `Kitchen.bat /file:C:\..\Nessus_to_Excel\Job_Start_GeneralExcel.kjb /level:Basic`
