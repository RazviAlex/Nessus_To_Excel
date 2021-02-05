#! usr/bin/env python

# Import Statements
import sys
from lxml import etree
import datetime

# Invoke script by passing nmap .xml file and Nessus .nessus file.  Ex., 'python dbsec_parser.py scan.xml scan.nessus'
def main (nessus_filepath):
	#nmap_tree = etree.parse(nmap_filepath)
	nessus_tree = etree.parse(nessus_filepath)
	scan_data_tag = etree.Element("NessusClientData_v2") # root xml tag

	# The following code parses the nessus file and creates the hosts xml for the hosts table
	hosts_tag = etree.SubElement(scan_data_tag, "hosts")
	host_ip_value = ''
	host_name_value = ''
	host_os_value = ''
	host_mac_value = ''

	for Report in nessus_tree.xpath("Report"):
	
		for ReportHost in Report.xpath("ReportHost"):
		
			for HostProperties in ReportHost.xpath("HostProperties"):
			
				for tag in HostProperties.xpath("tag"):
					if tag.attrib.get("name") == "host-ip":
						host_ip_value = tag.text
					if tag.attrib.get("name") == "host-fqdn":
						host_name_value = tag.text
					if tag.attrib.get("name") == "operating-system":
						host_os_value = tag.text
					if tag.attrib.get("name") == "mac-address":
						host_mac_value = tag.text
			
				host_tag = etree.SubElement(hosts_tag, "host")				
				host_ip_tag = etree.SubElement(host_tag, "host_ip")
				host_ip_tag.text = host_ip_value
				host_name_tag = etree.SubElement(host_tag, "host_name")
				host_name_tag.text = host_name_value
				host_os_tag = etree.SubElement(host_tag, "host_os")
				host_os_tag.text = host_os_value
				host_mac_tag = etree.SubElement(host_tag, "mac_address")
				host_mac_tag.text = host_mac_value

				host_ip_value = ''
				host_name_value = ''
				host_os_value = ''
				host_mac_value = ''

	# The following code parses the nessus file and creates the vulnerabilities xml for the vulnerabilities table
	vulns_tag = etree.SubElement(scan_data_tag, "vulnerabilities")
	vuln_id = 0

	for Report in nessus_tree.xpath("Report"):

		report_name_value = ''
		report_name_value = Report.attrib.get("name")

		for ReportHost in Report.xpath("ReportHost"):

			severity_tag_value = ''
			plugin_tag_value = ''
			solution_tag_value = ''
			cvss_base_tag_value = ''
			cvss_temp_tag_value = ''
			port_tag_value = ''
			plugin_output_tag_value = ''
			cvss3_vector_tag_value = ''
			lista = []
			
			for HostProperties in ReportHost.xpath("HostProperties"):
				
				for tag in HostProperties.xpath("tag"):
					if tag.attrib.get("name") == "host-ip":
						vuln_host_ip_tag_value = tag.text
					if tag.attrib.get("name") == "HOST_START":
						Host_Start_tag_value = tag.text



				for ReportItem in ReportHost.xpath("ReportItem"):
					severity_tag_value = ReportItem.attrib.get("severity")
					port_tag_value = ReportItem.attrib.get("port")
					plugin_tag_value = ReportItem.attrib.get("pluginID")
					vuln_name_tag_value = ReportItem.attrib.get("pluginName")

					"""for cve in ReportItem.xpath("cve"):
						lista.append(cve)""" 

					for solution in ReportItem.xpath("solution"):
						solution_tag_value = solution.text


					for plugin_output in ReportItem.xpath("plugin_output"):
						plugin_output_tag_value = plugin_output.text

					for cvss_base in ReportItem.xpath("cvss3_base_score"):
						cvss_base_tag_value = cvss_base.text

					for cvss_temp in ReportItem.xpath("cvss3_temporal_score"):
						cvss_temp_tag_value = cvss_temp.text

					for cvss3_vector in ReportItem.xpath("cvss3_vector"):
						cvss3_vector_tag_value = cvss3_vector.text
						

					vuln_tag = etree.SubElement(vulns_tag, "vulnerability")				
					vuln_id_tag = etree.SubElement(vuln_tag, "vuln_id")
					vuln_id_tag.text = str(vuln_id)
					vuln_id += 1

					"""for i in range(len(lista)):
						lista_tag = etree.SubElement(vuln_tag, "cve")
						lista_tag.text = lista[i] """


					vuln_host_ip_tag = etree.SubElement(vuln_tag, "host_ip")
					vuln_host_ip_tag.text = vuln_host_ip_tag_value

					Host_Start_tag = etree.SubElement(vuln_tag, "nessus_datetime")
					Host_Start_tag.text = Host_Start_tag_value

					report_name_tag = etree.SubElement(vuln_tag, "report_name")
					report_name_tag.text = report_name_value

					severity_tag = etree.SubElement(vuln_tag, "severity")
					severity_tag.text = severity_tag_value

					port_tag = etree.SubElement(vuln_tag, "port")
					port_tag.text = port_tag_value

					vuln_name_tag = etree.SubElement(vuln_tag, "vuln_name")
					vuln_name_tag.text = vuln_name_tag_value

					sol_tag = etree.SubElement(vuln_tag, "sol")
					sol_tag.text = solution_tag_value

					plugin_output_tag = etree.SubElement(vuln_tag, "plugin_output")
					plugin_output_tag.text = plugin_output_tag_value

					plugin_tag = etree.SubElement(vuln_tag, "plugin")
					plugin_tag.text = plugin_tag_value

					cvss_base_tag = etree.SubElement(vuln_tag, "cvss_base3")
					cvss_base_tag.text = cvss_base_tag_value

					cvss_temp_tag = etree.SubElement(vuln_tag, "cvss_temp3")
					cvss_temp_tag.text = cvss_temp_tag_value

					cvss3_vector_tag = etree.SubElement(vuln_tag, "cvss3_vector")
					cvss3_vector_tag.text = cvss3_vector_tag_value
					

	# The following code parses the nessus file and creates the cve xml for the cve table
	cves_tag = etree.SubElement(scan_data_tag, "CVEs")
	cve_id = 0

	for Report in nessus_tree.xpath("Report"):
	
		for ReportHost in Report.xpath("ReportHost"):

			for ReportItem in ReportHost.xpath("ReportItem"):
				cve_plugin_tag_value = ReportItem.attrib.get("pluginID")
				for cve in ReportItem.xpath("cve"):
					cve_tag = etree.SubElement(cves_tag, "cve")
					cve_id_tag = etree.SubElement(cve_tag, "cve_id")
					cve_id_tag.text = str(cve_id)						
					cve_id += 1
					cve_plugin_tag = etree.SubElement(cve_tag, "plugin")
					cve_plugin_tag.text = cve_plugin_tag_value
					cve_tag = etree.SubElement(cve_tag, "cve_num")
					cve_tag.text = cve.text

	print(etree.tostring(scan_data_tag, pretty_print=True))	#print to console						

if __name__ == "__main__":
    main(sys.argv[1])
	
