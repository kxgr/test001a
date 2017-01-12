import requests
import json

def trade_spider(max_pages, url):
    """3.this method takes two arguments, first says to loop how many time to run, the second is the url.
    It opens the given url, then saves the text in one variable and after calls next function with given
    argument the text as list"""
    page = 1
    while page <= max_pages:
        source_code = requests.get(url)
        plain_text = source_code.text
        list_to_dictio(plain_text)
        page += 1

def write_file_append(string):
    """7. this method takes one argument, this is the string who will be writen in txt file.
    It opens the file, write the given string adds a new line and it closes the file."""
    fo = open('products.txt', 'a')
    fo.write(string)
    fo.write("\n")
    fo.close()

def set_vendor_on_text(vendor):
    """5. this method takes one argument, and its the vendor name. Opens the txt file, write the Vendor
    name, it adds a new line, and then closes."""
    fo = open('products.txt', 'a')
    vendor_txt = "Vendor Name: "+vendor
    fo.write(vendor_txt)
    fo.write("\n")
    fo.close()

def fix_url_adr(old_url):
    """2.this method takes one argument, the old url, first reads a txt file,and after adds to end of the old url
     each line of our text file and calls next function with given argument the new url"""
    fr=open('test03.txt', 'r')
    text=fr.readlines()
    for line in text:
        new_url = old_url+str(line)
        trade_spider(1,new_url)

def list_to_dictio(list):
    """4.this method takes one argument, the given list. It takes that list then save this in a dictionary.
     each dictionary has two keys. We save the values from this keys in two lists. Then calls the function
     who sets the name, and after calls next with given argument the value list"""
    dict = json.loads(list)
    new_dict=dict['product']
    vendor_name = dict['vendor']
    set_vendor_on_text(vendor_name)
    dict_to_list(new_dict)

def dict_to_list(dict):
    """6. this method takes one argument, and its the given list from last method. Then for each value in given list
    calls next function to write the data to a file."""
    for value in dict:
        write_file_append(value)

def main():
    """1.this is the main method, will run as first,
    will take the url and call next method with argument the url"""
    old_url = 'http://cve.circl.lu/api/browse/'
    fix_url_adr(old_url)

if __name__ == '__main__':
    main()