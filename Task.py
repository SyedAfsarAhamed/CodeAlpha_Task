import os
import shutil
import re
import requests

def move_jpg_files():
    source = input("Enter the source folder path: ").strip()
    dest = input("Enter the destination folder path: ").strip()

    if not os.path.exists(dest):
        os.makedirs(dest)

    moved = 0
    for filename in os.listdir(source):
        if filename.lower().endswith(".jpg"):
            shutil.move(os.path.join(source, filename), os.path.join(dest, filename))
            print(f"Moved: {filename}")
            moved += 1
    print(f"\n✅ Total .jpg files moved: {moved}\n")


def extract_emails():
    input_file = input("Enter the path to the input .txt file: ").strip()
    output_file = input("Enter the path for the output file: ").strip()

    with open(input_file, 'r') as f:
        text = f.read()

    emails = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', text)

    with open(output_file, 'w') as f:
        for email in emails:
            f.write(email + '\n')

    print(f"\n✅ {len(emails)} email(s) extracted and saved to {output_file}\n")


def scrape_webpage_title():
    url = input("Enter the full URL of the webpage: ").strip()
    output_file = input("Enter the path for the output file: ").strip()

    try:
        response = requests.get(url)
        if response.status_code == 200:
            match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
            if match:
                title = match.group(1)
                with open(output_file, 'w') as f:
                    f.write(title)
                print(f"\n✅ Title saved to {output_file}: {title}\n")
            else:
                print("❌ Title not found in the webpage.")
        else:
            print(f"❌ Failed to access URL. Status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")


def main_menu():
    while True:
        print("\n🎯 Python Automation Tasks Menu")
        print("1. Move .jpg files to a new folder")
        print("2. Extract emails from a .txt file")
        print("3. Scrape title from a webpage")
        print("4. Exit")

        choice = input("Select a task (1-4): ")

        if choice == '1':
            move_jpg_files()
        elif choice == '2':
            extract_emails()
        elif choice == '3':
            scrape_webpage_title()
        elif choice == '4':
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("❌ Invalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    main_menu()
