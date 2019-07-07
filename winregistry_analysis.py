#!/usr/bin/python3

import winreg
import argparse
import sys

class RegDemo:
    def __init__(self):
        pass
    @staticmethod
    def get_args():
        parser=argparse.ArgumentParser(description='Query the registry')
        parser.add_argument("-e", "--enum", help="Enumerate all keys")
        parser.add_argument("-q","--query",nargs=2,help="Query registry")
        return parser.parse_args()

    def enum(self,hive,reg_path):
        registry_key=winreg.OpenKey(hive,reg_path,0,winreg.KEY_READ)
        try:
            registry_key=winreg.OpenKey(hive,reg_path,0,winreg.KEY_READ)
            i=0
            while True:
                value=winreg.EnumKey(registry_key,i)
                print(value)
                i+=1
        except:
            print("error loading key")
        finally:
            winreg.CloseKey(registry_key)

    def  query(self,hive,reg_path,value_name):
        registry_key=winreg.OpenKey(hive,reg_path,0,winreg.KEY_READ)
        try:
            registry_key=winreg.OpenKey(hive,reg_path,0,winreg.KEY_READ)
            value=winreg.QueryValueEx(registry_key,value_name)
            print(value)
        except WindowsError as e:
            print("Error Loading Key\n{}".format(e))
        finally:
            winreg.CloseKey(registry_key)

    def main(self):
        args=self.get_args()
        hive=winreg.HKEY_CURRENT_USER
        if args.enum:
            self.enum(hive,args.enum)
        if args.query:
            self.query(hive,args.query[0],args.query[1])

if __name__=='__main__':
    reg_instance=RegDemo()
    reg_instance.main()
