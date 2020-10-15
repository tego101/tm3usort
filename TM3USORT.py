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
    def intro(self):
        #   Intro.
        print('\n########################################################')
        print('#   TM3U Sort                                          #')
        print('#   A Quick tool to sort out elements in a m3u file.   #')
        print('#   ###########################                        #')
        print('#   http://github.com/tego101                          #')
        print('#   ####################################               #')
        print('#   # IF THIS HELPED, PLEASE DONATE :) #               #')
        print('#   ####################################               #')
        print('#   BITCOIN -> 1KouUcQ7o4rVh8gTg6W3HPUDsBBdoC6G1K      #')
        print('#   CASHAPP -> $redtvme                                #')
        print('########################################################')
        print('#    ALL DONATIONS WILL BE USED FOR SUSHI & .. SUSHI   #')
        print('########################################################\n')
        print('### THANK YOU TO ALL MY SUPPORTERS!!  ##################')
        print('########################################################')
        print('#### @realiptv                                      ####')
        print('#### @TheOGKillz                                    ####')
        print('#### @@Ultimate_scraper                             ####')
        print('#### @codelinux89                                   ####')
        print('#### @billybadson                                   ####')
        print('#### @cafterburn77                                  ####')
        print('#### @ytvm4u                                        ####')
        print('#### @jbrad                                         ####')
        print('########################################################')
        print('#### ==> <3 <3 I APPERCIATE YOU GUYS!!!! <3 <3 <=== ####')
        print('########################################################\n')
        time.sleep(1)

    @classmethod
    def outro(self):
        #   Pay homage to my first contributors for this script.
        #   If this helped you please donate!
        print('==> THANK YOU TO MY SUPPORTERS!!! \n ')
        time.sleep(1)
        print(' ==> @realIPTV (BOSS OF STREAMS!) \n')
        time.sleep(1)
        print('   ==> @TheOGKillz \n')
        time.sleep(1)
        print('    ==> @Ultimate_scraper \n')
        time.sleep(1)
        print('     ==> @codelinux89 \n')
        time.sleep(1)
        print('      ==> @billybadson \n')
        time.sleep(1)
        print('       ==> @cafterburn77 \n')
        time.sleep(1)
        print('        ==> @ytvm4u \n')
        time.sleep(1)
        print('         ==> @jbrad \n')
        time.sleep(1)
        print('          ==> <3 <3 I APPERCIATE YOU GUYS!!!! \n')
        time.sleep(1)

    @classmethod
    def localList(self):
        print('\n')

        files = []
        print(' ###### Available Lists to Scan: ######\n')
        print(' Please place your files in the "lists" folder to scan them. \n')
        for file in glob.glob("lists/*.m3u"):
            alists = file
            print(alists.replace("lists/", "----> "))

        print('\n')

        #   Request File Name.
        r_file = 'lists/' + input(' Enter File Name: ')

        #   Request year or element to search.
        if not os.path.isfile(r_file):
            print('\n')
            print(' ### ERROR ### ---> ' + r_file.replace("lists/", " ") + '.m3u Does not exist! <---- ### ERROR ### \n')

            #   Search again
            again = input(' Try Again? (Y/N)')
            #   Do the dooo
            if again is 'Y' or again is 'y':
                TM3U.localList()
            else:
                print('\n OK! \n')
                print('########################')
                TM3U.outro()
        else:
            print('\n')
            r_year_title = input(' What Year or Title? ')

            #   Lets open up the requested file and search it.
            with open(r_file) as input_file:
                content_generator = (line for line in input_file.read().splitlines())
                print('\n')
                #   Iter the results.
                print(' #### RESULTS ####\n')
                for line in content_generator:
                    if r_year_title in line:
                        next_line = next(content_generator)
                        print(line)
                        print(next_line)

                print('\n')

                #   Save List to File.
                save = input(' Save to file? Yes or No: \n ')
                print('\n')
                #   Save the file?
                if 'yes' in save:
                    #   Name the file.
                    file_name = input(' What should we name the file? \n   ')

                    new_list = open('saved/' + file_name + '.m3u','w+')
                    new_list.write("#EXTM3U \n")
                    
                    with open(r_file) as input_file:
                        content_generator = (line for line in input_file.read().splitlines())
                        
                        for line in content_generator:
                            if r_year_title in line:
                                next_line = next(content_generator)
                                new_list.write(line + '\n')
                                new_list.write(next_line + '\n')

                            

                        #   Process complete!!!
                        print(' \n Operation Complete!!! file saved as ' + file_name + '.m3u in the SAVED folder! \n')

                        #   Search again?
                        again = input(' Search Again? (Y/N) \n ')

                        if again is 'Y' or again is 'y':
                            TM3U.localList()
                        else:
                            print('\n OK! \n')
                            print('########################')
                            TM3U.outro()
                        
                elif save == 'NO' or save == 'No' or save == 'no':
                        print('OK!')


TM3U.intro()
TM3U.localList()