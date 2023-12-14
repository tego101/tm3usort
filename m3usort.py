#!/usr/bin/env python3

"""
#######################################################
#   TM3U Sort                                         #
#   A Quick tool to sort out elements in a m3u file.  #
#######################################################
#   http://github.com/tego101/tm3usort                #
#######################################################
#   BITCOIN -> 1KouUcQ7o4rVh8gTg6W3HPUDsBBdoC6G1K     #
#######################################################
#   CASHAPP -> REDTVME                                #
#######################################################
#   ALL DONATIONS WILL BE USED FOR SUSHI & .. SUSHI   #
#######################################################
"""

import os
import glob
import time


class TM3U:
    @classmethod
    def intro(cls):
        #   Intro.
        intro_text = "\n########################################################\n"
        intro_text += "#   TM3U Sort                                          #\n"
        intro_text += "#   A Quick tool to sort out elements in a m3u file.   #\n"
        intro_text += "#   ###########################                        #\n"
        intro_text += "#   http://github.com/tego101                          #\n"
        intro_text += "#   ####################################               #\n"
        intro_text += "#   # IF THIS HELPED, PLEASE DONATE :) #               #\n"
        intro_text += "#   ####################################               #\n"
        intro_text += "#   BITCOIN -> 1KouUcQ7o4rVh8gTg6W3HPUDsBBdoC6G1K      #\n"
        intro_text += "#   CASHAPP -> $redtvme                                #\n"
        intro_text += "########################################################\n"
        intro_text += "#    ALL DONATIONS WILL BE USED FOR SUSHI & .. SUSHI   #\n"
        intro_text += "########################################################\n\n"
        intro_text += "### THANK YOU TO ALL MY SUPPORTERS!!  ##################\n"
        intro_text += "########################################################\n"
        intro_text += "#### @realiptv                                      ####\n"
        intro_text += "#### @TheOGKillz                                    ####\n"
        intro_text += "#### @@Ultimate_scraper                             ####\n"
        intro_text += "#### @codelinux89                                   ####\n"
        intro_text += "#### @billybadson                                   ####\n"
        intro_text += "#### @cafterburn77                                  ####\n"
        intro_text += "#### @ytvm4u                                        ####\n"
        intro_text += "#### @jbrad                                         ####\n"
        intro_text += "########################################################\n"
        intro_text += "#### ==> <3 <3 I APPERCIATE YOU GUYS!!!! <3 <3 <=== ####\n"
        intro_text += "########################################################\n\n"

        print(intro_text)

        time.sleep(1)

    @classmethod
    def outro(cls):
        #   Pay homage to my first contributors for this script.
        #   If this helped you please donate!
        outro_text = "==> THANK YOU TO MY SUPPORTERS!!! \n\n"
        outro_text += " ==> @realIPTV (BOSS OF STREAMS!) \n\n"
        outro_text += "   ==> @TheOGKillz \n\n"
        outro_text += "    ==> @Ultimate_scraper \n\n"
        outro_text += "     ==> @codelinux89 \n\n"
        outro_text += "      ==> @billybadson \n\n"
        outro_text += "       ==> @cafterburn77 \n\n"
        outro_text += "        ==> @ytvm4u \n\n"
        outro_text += "         ==> @jbrad \n\n"
        outro_text += "          ==> <3 <3 I APPERCIATE YOU GUYS!!!! \n\n"

        print(outro_text)

        time.sleep(1)

    @classmethod
    def local_list(cls):
        print("\n")

        files = []
        print(" ###### Available Lists to Scan: ######\n")
        print(" Please place your files in the 'lists' folder to scan them. \n")
        for file in glob.glob("lists/*.m3u"):
            alists = file
            print(alists.replace("lists/", "----> "))

        print("\n")

        #   Request File Name.
        r_file = 'lists/' + input(" Enter File Name: ")

        #   Request year or element to search.
        if not os.path.isfile(r_file):
            print("\n")
            print(" ### ERROR ### ---> " + r_file.replace("lists/", " ") + '.m3u Does not exist! <---- ### ERROR ### \n')

            #   Search again
            again = input(" Try Again? (Y/N)")
            #   Do the dooo
            if again.lower() == 'y':
                cls.local_list()
            else:
                print("\n OK! \n")
                print("########################")
                cls.outro()
        else:
            print("\n")
            r_year_title = input(" What Year or Title? ")

            #   Lets open up the requested file and search it.
            with open(r_file) as input_file:
                content_generator = (line for line in input_file.read().splitlines())
                print("\n")
                #   Iter the results.
                print(" #### RESULTS ####\n")
                for line in content_generator:
                    if r_year_title in line:
                        next_line = next(content_generator)
                        print(line)
                        print(next_line)

                print("\n")

                #   Save List to File.
                save = input(" Save to file? Yes or No: \n ")
                print("\n")
                #   Save the file?
                if save.lower() == 'yes':
                    #   Name the file.
                    file_name = input(" What should we name the file? \n   ")

                    new_list = open('saved/' + file_name + '.m3u', 'w+')
                    new_list.write("#EXTM3U \n")

                    with open(r_file) as input_file:
                        content_generator = (line for line in input_file.read().splitlines())

                        for line in content_generator:
                            if r_year_title in line:
                                next_line = next(content_generator)
                                new_list.write(line + '\n')
                                new_list.write(next_line + '\n')

                        #   Process complete!!!
                        print(" \n Operation Complete!!! file saved as " + file_name + '.m3u in the SAVED folder! \n')

                        #   Search again?
                        again = input(" Search Again? (Y/N) \n ")

                        if again.lower() == 'y':
                            cls.local_list()
                        else:
                            print("\n OK! \n")
                            print("########################")
                            cls.outro()

                elif save.lower() == 'no':
                    print("OK!")


if __name__ == "__main__":
    TM3U.intro()
    TM3U.local_list()
