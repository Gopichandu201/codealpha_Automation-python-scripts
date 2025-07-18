import os
import shutil
import re
import requests

def move_jpg_files():
    source_folder = input("Enter the source folder path: ")
    destination_folder = input("Enter the destination folder path: ")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    moved = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpg", ".jpeg")):
            src_path = os.path.join(source_folder, filename)
            dst_path = os.path.join(destination_folder, filename)
            shutil.move(src_path, dst_path)
            print(f"Moved: {filename}")
            moved += 1

    print(f"\nTotal .jpg files moved: {moved}")


def extract_emails():
    input_file = input("Enter the path of the .txt file to scan: ")
    output_file = input("Enter the path of the output file: ")

    try:
        with open(input_file, "r") as file:
            content = file.read()

        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

        with open(output_file, "w") as file:
            for email in emails:
                file.write(email + "\n")

        print(f"\nExtracted {len(emails)} email(s) and saved to {output_file}")

    except FileNotFoundError:
        print("File not found. Please check the path and try again.")


def scrape_webpage_title():
    url = input("Enter the full URL of the webpage (e.g., https://example.com): ")

    try:
        response = requests.get(url)
        html = response.text
        match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)

        if match:
            title = match.group(1)
            print("Webpage Title:", title)
            with open("page_title.txt", "w") as file:
                file.write(title)
            print("Title saved to 'page_title.txt'")
        else:
            print("Title not found in the page.")

    except Exception as e:
        print("Error fetching the webpage:", e)


# === Menu ===
def main():
    while True:
        print("\n🔧 Task Automation Tool")
        print("1. Move all .jpg files from one folder to another")
        print("2. Extract all email addresses from a .txt file")
        print("3. Scrape title of a webpage and save it")
        print("4. Exit")

        choice = input("Choose a task (1/2/3/4): ")

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_webpage_title()
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
