# Digital-Forensic
The script enumerate and query Windows Registry of a given hive, registry path and registry key

# Getting Started

The script excepts two types of arguments which are grouped as -e which is to enumerate to be executed at the target remote device, -q to query the registry key value

# Example
>python registry_test.py -q SOFTWARE\Microsoft\Windows\CurrentVersion\Run OneDrive\
>python registry_test.py -e SOFTWARE\Microsoft\Windows\CurrentVersion
