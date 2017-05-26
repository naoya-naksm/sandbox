# encoding: utf-8
import sys
from xml.etree import ElementTree

def parse_xml():
    args = sys.argv
    config = {}
    f = open(args[1], "r")
    try:
        tree = ElementTree.parse(f)
        config["sysID"] = tree.find("sysId").text
        config["configuration"] = tree.find("configuration").get("comment")
        config["token"] = tree.find("configuration").find("token").get("api")
        config["settings"] = []
        for setting in tree.find("configuration").getiterator("supportedSetting"):
            config["settings"].append({
                    "id": setting.findtext("id"),
                    "name": setting.findtext("name"),
                    "setupItemID": setting.findtext("setupItemID"),
                    "value": setting.findtext("value"),
            })
#       print("Config: " + str(config))
        print("sysID: " + config["sysID"])
        print("config comment: " + config["configuration"])
        print("token: " + config["token"])
        item_count = 0
        for item in config["settings"]:
            print("Setting# " + str(item_count))
            print("  id: " + item["id"])
            print("  name: " + item["name"])
            print("  setupItemID: " + item["setupItemID"])
            print("  value: " + item["value"])
            item_count = item_count + 1
    finally:
        f.close()

if __name__ == "__main__":
    parse_xml()
