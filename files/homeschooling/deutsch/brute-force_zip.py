"""
This program try to bruteforce the password for a zip file with an given dictinary file.
Needs Python > 3.5
Uuses the library 'zipfile' to help us complet this easily


Credits: Rishit Dagli
Licence: Apache License 2.0
Version: 1.0.0
Status: Development

This particular programm is not my work, I get it mostly from https://github.com/Rishit-dagli/Bruteforce-tool-for-zip-files
"""

import zipfile
import timeit
import sys

def crack(dictionary_attack, zFile, filename):
    '''
    @Rishit Dagli
    Make a crack function which will do the major work for us
    This function should iterate throught hr dictionary file and try every
        string as a password in the file and then output to us if it found the
        password from the dictionary file.
    '''
    attempts = 0
    flag = 0

    with open(dictionary_attack, 'r') as word:

        print("started cracking password")

        for line in word:

#           Using a try...exception to keep attempting
#           the different passwords from the wordlist

            try:
#               new lines

                passwd = line.strip('\n')
                zFile.extractall(pwd=str.encode(passwd))

            except Exception:

                attempts += 1
                pass

            else:
                print("Password brute forced is %s" % (passwd))
                flag = 1
                break

        print("Attempted %d passwords from %s wordlist" %
              (attempts, filename))

        if flag == 0:
            print("Password not in "+ str(filename))

def main():
    '''
    @Rishit Dagli
    The main() function we call the crack() function from here and also
        calculate the time here
    '''
articular
    file_name=input("Enter Zip file name: ")
    dictionary_name=input("Enter dictionary file name: ")
    zip_file = zipfile.ZipFile(str(file_name))

    start = timeit.default_timer()

    crack(dictionary_name, zip_file, file_name)

    stop = timeit.default_timer()

    print("Crack password in %d secs" % (stop - start))

if __name__ == "__main__":
    main()
