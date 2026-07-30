from vault import add_link, view_links, search_links

while True:
    print("\n===== LinkVaultX =====")
    print("1. Save Link")
    print("2. View Links")
    print("3. Search Links")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Title: ")
        url = input("URL: ")
        category = input("Category: ")
        add_link(title, url, category)

    elif choice == "2":
        view_links()

    elif choice == "3":
        keyword = input("Search keyword: ")
        search_links(keyword)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
