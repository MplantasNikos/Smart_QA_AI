from pdf_reader import *
from html_reader import *
from text_reader import *
from youtube_reader import *
from many_text_reader import *
from url_loader import *
from question import *
import warnings 
warnings.filterwarnings("ignore")
from termcolor import colored
import os 
from save_answer import *
from powerpoint_reader import *

round = 0
message = """Welcome! I am a program equipped to answer any question based on information found in documents.
          I can process HTML, powerpoint, text, and PDF files, as well as folders containing multiple text files.
            But the best of all is that i can extract information from YouTube videos and website urls ! :) ;)"""



while True:
    # print welcome message
    if round == 0 :
        print(message)
        print('\n')

        # open ai key 
        print('In order to do my job i need you to provide me an OPEN AI api key')
        print('\n')
        print('if you dont know what that is please visit the url bellow : ')
        print('\n')
        print('https://youtu.be/6Z6J7GQOiOo?si=dSXpHa-PGpwhfhY_')
        print('\n')
        print('Now , i want you to provide me that key so i can do my job :)')
        print('\n')
        print(colored('Note ! i want it NOT in " " ',attrs=['bold']))
        print('\n')
        print(colored('if the key is incorrect i am afraid that i can not provide any results :(',attrs=['bold']))
        key = input('__________')
        print('\n')

        print('I am going to check now if its valid .....')
        print('\n')

        client = openai.OpenAI(api_key=key)

        try:
             client.models.list()

           
        except openai.AuthenticationError as e:
            print('This API KEY is not valid :(')
            print('\n')
            print('Program will close , get a correct key and then open it again !')
            print('\n')
            break



        os.environ["OPENAI_API_KEY"] = key
        print('\n')
        print('key is valid ! :)')
        print('\n')
        print('alright! lets go !')
        print('\n')



    while True:
        print('Please specify the file type you would like to search [pdf, html, text, folder, youtube, url, powerpoint]')
        print('\n')
        print('If you want to exit type "exit"')
        print('\n')
        print('Note ! Folder must contain text files')
        print('\n')
        file_type = input('............')

        if file_type in ['pdf' , 'html' , 'text' , 'folder' , 'youtube','url','powerpoint','exit']:
            break
        else:
            print()
            print(colored('Please choose one of those in the brakets',attrs=['bold']))
            print('\n')



    if file_type == 'pdf':
        while True:
            try : 
                path = input('Please insert the full path of the PDF file in your computer')
                print('\n')
                readed_pdf = pdf_reader(path)
                query = input('Give me a Question that the awnser is inside the PDF file')
                print('\n')
                print('wait.....')
                print('\n')
                awnser = question(query=query,db=readed_pdf)
                print('Question : ' , query)
                print('\n')

                print('Answer : ' , awnser)
                print('\n')
                print('\n')
                
                print('Do you want to save it ?[Y/N]')
                print('\n')

                save_or_not = input('........')
                print('\n')

                while save_or_not not in ['Y','N']:
                    print('please just type Y or N')
                    save_or_not = input('........')
                if save_or_not == 'Y':
                    result_of_save = save(awnser)
                    if result_of_save == 1:
                        print('ITS SAVED :)')
                    else:
                        print('Okey')
                else:
                    print('Okey')
                    break



                break


            except FileNotFoundError:
                print(colored('That file does not exist make sure you write it correct ',attrs=['bold']))
                print('\n')

                again = input('Do you want to try again ?[Y/N]')
                print('\n')
                while again not in ['Y','N']:
                    print('...please just type Y or N')
                    again = input('........')
                    print('\n')

                if again == 'N':
                    break       
            except Exception as e :
                print(e)
                print(colored('Somethink went wrong ! be more carefull',attrs=['bold']))
                print('\n')

                again = input('Do you want to try again ?[Y/N]')
                print('\n')
                while again not in ['Y','N']:
                    print('...please just type Y or N')
                    again = input('........')
                    print('\n')

                if again == 'N':
                    break       



    elif file_type == 'text':
        while True:
            try : 
                path = input('Please insert the full path of the text file in your computer')
                print('\n')

                text_f = text_loaders(path)
                query = input('Give me a Question that the awnser is inside the text file')
                print('\n')
                print('wait.....')
                print('\n')
                awnser = question(query=query,db=text_f)
                print('Question : ' , query)
                print('\n')
                print('Answer : ' , awnser)
                print('\n')
                print('\n')
                
                print('Do you want to save it ?[Y/N]')
                print('\n')

                save_or_not = input('........')
                print('\n')
                while save_or_not not in ['Y','N']:
                    print('please just type Y or N')
                    save_or_not = input('........')
                if save_or_not == 'Y':
                    result_of_save = save(awnser)
                    if result_of_save == 1:
                        print('ITS SAVED :)')
                    else:
                        print('Okey')
                else:
                    print('Okey')
                    break



                break
                
            except FileNotFoundError:
                print(colored('That file does not exist make sure you write it correct',attrs=['bold']))
                print('\n')
                again = input('Do you want to try again ?[Y/N]')
                print('\n')
                while again not in ['Y','N']:
                    print('...please just type Y or N')
                    again = input('........')
                    print('\n')

                if again == 'N':
                    break       
            except Exception as e :
                    print(e)
                    print(colored('Somethink went wrong ! be more carefull',attrs=['bold']))
                    print('\n')

                    again = input('Do you want to try again ?[Y/N]')
                    print('\n')
                    while again not in ['Y','N']:
                        print('...please just type Y or N')
                        again = input('........')
                        print('\n')

                    if again == 'N':
                        break        
                



    elif file_type == 'html':
        while True:
            try : 
                path = input('Please insert the full path of the html file in your computer')
                print('\n')
                html_file = load_html(path)
                query = input('Give me a Question that the awnser is inside the html file')
                print('\n')
                print('wait.....')
                print('\n')
                awnser = question(query=query,db=html_file)
                print('Question : ' ,query)
                print('\n')
                print('Answer : ' , awnser)
                print('\n')
                print('\n')
                
                print('Do you want to save it ?[Y/N]')
                print('\n')

                save_or_not = input('........')
                print('\n')
                while save_or_not not in ['Y','N']:
                    print('please just type Y or N')
                    save_or_not = input('........')
                if save_or_not == 'Y':
                    result_of_save = save(awnser)
                    if result_of_save == 1:
                        print('ITS SAVED :)')
                    else:
                        print('Okey')
                else:
                    print('Okey')
                    break



                break
                
            except FileNotFoundError:
                print(colored('That file does not exist make sure you write it correct ',attrs=['bold']))
                print('\n')
                again = input('Do you want to try again ?[Y/N] ')
                print('\n')
                while again not in ['Y','N']:
                    print('...please just type Y or N')
                    again = input('........')
                    print('\n')

                if again == 'N':
                    break       
            except Exception as e :
                    print(e)
                    print(colored('Somethink went wrong ! be more carefull',attrs=['bold']))
                    print('\n')

                    again = input('Do you want to try again ?[Y/N]')
                    print('\n')
                    while again not in ['Y','N']:
                        print('...please just type Y or N')
                        again = input('........')
                        print('\n')

                    if again == 'N':
                        break       
        


    elif file_type == 'folder':
        while True:
            try : 
                path = input('Please insert the full path of the folder in your computer')
                print('\n')
                directory = directory_loader(path)
                query = input('Give me a Question that the awnser is inside the folder files')
                print('\n')
                print('wait.....')
                print('\n')
                awnser = question(query=query,db=directory)
                print('Question : ' ,query)
                print('\n')
                print('Answer : ' , awnser)

                print('\n')
                print('\n')
                
                print('Do you want to save it ?[Y/N]')
                print('\n')

                save_or_not = input('........')
                print('\n')
                while save_or_not not in ['Y','N']:
                    print('please just type Y or N')
                    save_or_not = input('........')
                if save_or_not == 'Y':
                    result_of_save = save(awnser)
                    if result_of_save == 1:
                        print('ITS SAVED :)')
                    else:
                        print('Okey')
                else:
                    print('Okey')
                    break



                break
                
            except FileNotFoundError:
                print(colored('That file does not exist make sure you write it correct ',attrs=['bold']))
                print('\n')
                again = input('Do you want to try again ?[Y/N]')
                print('\n')
                while again not in ['Y','N']:
                    print('...please just type Y or N')
                    again = input('........')
                    print('\n')

                if again == 'N':
                    break        
            except Exception as e :
                    print(e)
                    print(colored('Somethink went wrong ! be more carefull',attrs=['bold']))
                    print('\n')

                    again = input('Do you want to try again ?[Y/N]')
                    print('\n')
                    while again not in ['Y','N']:
                        print('...please just type Y or N')
                        again = input('........')
                        print('\n')

                    if again == 'N':
                        break       







    elif file_type == 'youtube':
        while True:
            try : 
                path = input('Please insert the url of the youtube video')
                print('\n')
                directory = youtube_loader(path)
                query = input('Give me a Question that the awnser is inside that youtube video')
                print('\n')
                print('wait.....')
                print('\n')
                awnser = question(query=query,db=directory)
                print('Question : ' , query)
                print('\n')
                print('Answer : ' , awnser)
                print('\n')
                print('\n')
                
                print('Do you want to save it ?[Y/N]')
                print('\n')

                save_or_not = input('........')
                print('\n')
                while save_or_not not in ['Y','N']:
                    print('please just type Y or N')
                    save_or_not = input('........')
                if save_or_not == 'Y':
                    result_of_save = save(awnser)
                    if result_of_save == 1:
                        print('ITS SAVED :)')
                    else:
                        print('Okey')
                else:
                    print('Okey')
                    break



                break
            except Exception as e :
                print(e)
                print(colored('Incorect URL',attrs=['bold']))
                print('\n')
                again = input('Do you want to try again ?[Y/N]')
                print('\n')
                while again not in ['Y','N']:
                    print('...please just type Y or N')
                    again = input('........')
                    print('\n')

                if again == 'N':
                    break      




    elif file_type == 'url':
            while True:
                try : 
                    path = input('Please insert the url of the webpage')
                    print('\n')
                    urls = []
                    urls.append(path)
                    directory = load_url(urls)
                    query = input('Give me a Question that the awnser is inside the page content')
                    print('\n')
                    print('wait.....')
                    print('\n')
                    awnser = question(query=query,db=directory)
                    print('Question : ' , query)
                    print('\n')
                    print('Answer : ' , awnser)
                    print('\n')
                    print('\n')
                    
                    print('Do you want to save it ?[Y/N]')
                    print('\n')

                    save_or_not = input('........')
                    print('\n')
                    while save_or_not not in ['Y','N']:
                        print('please just type Y or N')
                        save_or_not = input('........')
                    if save_or_not == 'Y':
                        result_of_save = save(awnser)
                        if result_of_save == 1:
                            print('ITS SAVED :)')
                        else:
                            print('Okey')
                    else:
                        print('Okey')
                        break



                    break
                except Exception as e :
                    print(e)
                    print(colored('Incorect URL',attrs=['bold']))
                    print('\n')
                    again = input('Do you want to try again ?[Y/N]')
                    print('\n')
                    while again not in ['Y','N']:
                        print('...please just type Y or N')
                        again = input('........')
                        print('\n')

                    if again == 'N':
                        break      


    elif file_type == 'powerpoint':
            while True:
                try : 
                    path = input('Please insert the path  of the powerpoint file')
                    print('\n')
                    directory = powerpoint_loader(path)
                    query = input('Give me a Question that the awnser is inside the powerpoint file')
                    print('\n')
                    print('wait.....')
                    print('\n')
                    awnser = question(query=query,db=directory)
                    print('Question : ' , query)
                    print('\n')
                    print('Answer : ' , awnser)
                    print('\n')
                    print('\n')
                    
                    print('Do you want to save it ?[Y/N]')
                    print('\n')

                    save_or_not = input('........')
                    print('\n')
                    while save_or_not not in ['Y','N']:
                        print('please just type Y or N')
                        save_or_not = input('........')
                    if save_or_not == 'Y':
                        result_of_save = save(awnser)
                        if result_of_save == 1:
                            print('ITS SAVED :)')
                        else:
                            print('Okey')
                    else:
                        print('Okey')
                        break



                    break
                except Exception as e :
                    print(e)
                    print(colored('incorect file path or file does not exist ',attrs=['bold']))
                    print('\n')
                    again = input('Do you want to try again ?[Y/N]')
                    print('\n')
                    while again not in ['Y','N']:
                        print('...please just type Y or N')
                        again = input('........')
                        print('\n')

                    if again == 'N':
                        break      
                    
   






    else:
        print('Okey  :( ')
        break

    round += 1
    another = input('Do you want to  go to the main menu and run the program again?[Y/N]')
    print('\n')
    while another not in ['Y','N']:
        print('...please just type Y or N')
        another = input('........')
        print('\n')

    if another == 'N':
        print('Bye Bye ! :) ')
        break       
        

