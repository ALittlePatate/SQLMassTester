import requests
import os
import sys, getopt, traceback, types
from bs4 import BeautifulSoup

def write_good_site(website) :
    with open("good.txt", "a") as c :
        c.write(website)
        c.write("\n")
        c.close()

def write_bad_site(website) :
    with open("bad.txt", "a") as c :
        c.write(website)
        c.write("\n")
        c.close()

def main(argv) :
    print(" ")
    if argv == [] :
        ban()
    try:
        opts, args = getopt.getopt(argv,"hi:o:u:",["open=","url="])
    except getopt.GetoptError:
        print('python sqlTester.py -o <file to open>')
        print("python sqlTester.py -u <url to test>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Usage :")
            print('python sqlTester.py -o <file to open>')
            print("python sqlTester.py -u <url to test>")
            sys.exit()
        elif opt in ("-o", "--open"):
            read_text_file(arg)
        elif opt in ("-u", "--url"):
            check(arg)

def ban() :
    os.system("cls")
    os.system("title SQL Mass Tester")
    print("#####################")
    print("#  SQL Mass Tester  #")
    print("#####################")
    print(" ")
    print("{1} - Select a website")
    print("{2} - Use a text file")
    print("{99} - Exit")
    print(" ")
    choix_menu()

def choix_menu() :
    choix_menu = input("Make your choice : ")

    if choix_menu == "99" :
        exit()
    if choix_menu == "1" :
        choix_site()
    if choix_menu == "2" :
        choix_text()
    else :
        exit()

def choix_site() :
    print(" ")
    website = input("Select the website : ")
    print(" ")
    check(website)

def choix_text() :
    print(" ")
    text_file = input("Select your text file path : ")
    print(" ")
    read_text_file(text_file)

def read_text_file(text_file) :
    with open (text_file, "r") as f :
        for line in f :
            try :
                website = line
                check(website)
            except Exception as e:
                break

def check(website) :
    skip = False

    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}

    try :
        try :
            resp = requests.get(website+"'", headers=headers)
        except :
            website = website.replace("\n", "")
            print("[-] "+website+" is not responding...")
            write_bad_site(website)
            skip = True
    except requests.exceptions.MissingSchema :
        try :
            resp = requests.get("https://"+website+"'", headers=headers)
        except :
            website = website.replace("\n", "")
            print("[-] "+website+" is not responding...")
            write_bad_site(website)
            skip = True

    try :
        resp_code = str(resp.content).upper()
    except :
        pass

    website = website.replace("\n", "")


    if skip == False :
        if "MYSQL" in resp_code or "SQL" in resp_code :
            print("[+] "+website+" is vulnerable !")
            write_good_site(website)
        else :
            print("[-] "+website+" is not vulnerable...")
            write_bad_site(website)

if __name__ == "__main__":
    main(main(sys.argv[1:]))
    print(" ")
    exit()