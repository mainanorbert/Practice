#!/usr/bin/python3
import csv
import json
import xml.etree.ElementTree as ET
"""This code is for reading data from various types of files"""

# Function to extract data from CSV file

def extract_csv(file_path):
    """extracts data from csv file"""
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        return data
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def extract_json(file_path):
    """Function to extract data from JSON file"""
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        for item in data:
            if 'debt' in item:
                try:
                    x = float(item['debt'])                 
                    item['debt_amount'] = item['debt']
                except:              
                    item['debt_amount'] = item['debt']['amount']
                    item['debt_period_in_years'] = item['debt']['time_period_years']
                finally:
                    del item['debt']
        return data
    
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

def extract_txt(file_path):
    """ Function to extract data from text file"""
    try:
        with open(file_path, 'r') as txt_file:
            data = [line.strip() for line in txt_file]
        return data
    except Exception as e:
        print(f"Error reading TXT file: {e}")
        return None

def extract_xml(file_path):
    """ Function to extract data from XML file"""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        data = []
        for user_elem in root.findall('.//user'):
            record_data = {}
            for attr_name, attr_value in user_elem.attrib.items():
                record_data[attr_name] = attr_value
            data.append(record_data)
        return data
    except Exception as e:
        print(f"Error reading XML file: {e}")
        return None

