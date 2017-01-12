import requests
import json

def trade_spider(max_pages, url):
    page = 1
    while page <= max_pages:
        source_code = requests.get(url)
        plain_text = source_code.text
        list_to_dictio(plain_text)
        page += 1


def write_file_append(text):
    fo = open('products.txt', 'a')
    fo.write(text)
    fo.write("\n")
    fo.close()

def set_vendor_on_text(vendor):
    fo = open('products.txt', 'a')
    vendor_txt = "Vendor Name: "+vendor
    fo.write(vendor_txt)
    fo.write("\n")
    fo.close()

def fix_url_adr(old_url):
    fr=open('test03.txt', 'r')
    text=fr.readlines()
    for line in text:
        new_url = old_url+str(line)
        trade_spider(1,new_url)

def list_to_dictio(list):
    dict = json.loads(list)
    new_dict=dict['product']
    vendor_name = dict['vendor']
    set_vendor_on_text(vendor_name)
    dict_to_list(new_dict)
    '''for each in list:
        write_file_append(each)
        # print(text1['product'])
'''
def dict_to_list(dict):
    print(dict)
    for each in dict:
        write_file_append(each)

def main():
    old_url = 'http://cve.circl.lu/api/browse/'
    fix_url_adr(old_url)


if __name__ == '__main__':
    main()