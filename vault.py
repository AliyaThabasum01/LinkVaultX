import json
import os

FILE = "links.json"

def load_links():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_links(links):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(links, f, indent=4)

def add_link(title, url, category):
    links = load_links()
    links.append({
        "title": title,
        "url": url,
        "category": category
    })
    save_links(links)
    print("✅ Link saved!")

def view_links():
    links = load_links()

    if not links:
        print("No links saved.")
        return

    print("\n🔗 Saved Links\n")

    for i, link in enumerate(links, start=1):
        print(f"{i}. {link['title']}")
        print(f"   URL: {link['url']}")
        print(f"   Category: {link['category']}")
        print()

def search_links(keyword):
    links = load_links()
    keyword = keyword.lower()

    results = [
        link for link in links
        if keyword in link["title"].lower()
        or keyword in link["category"].lower()
    ]

    if not results:
        print("No matching links found.")
        return

    print("\n🔍 Search Results\n")

    for link in results:
        print(f"- {link['title']} ({link['category']})")
        print(f"  {link['url']}")
