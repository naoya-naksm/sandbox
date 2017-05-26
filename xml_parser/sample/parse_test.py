# encoding: utf-8
from xml.etree import ElementTree

def parse_xml():
    page = {}
    f = open("page.xml", "r")
    try: 
        tree = ElementTree.parse(f)
        page["version"] = tree.getroot().get("version")
        page["base"] = {
                "title": tree.find("base").find("title").text,
                "description": tree.find("base").findtext("description"),
        }
        page["items"] = []
        for item in tree.find("items").getiterator("item"):
            page["items"].append({
                    "name": item.findtext("name"),
                    "price": item.findtext("price"),
                    "type": item.get("type"),
            })
        print("PAGE: " + str(page))
    finally:
        f.close()
if __name__ == "__main__":
    parse_xml()
