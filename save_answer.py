from openai import OpenAI
import json 
def save(answer):
    print('You have 3 options : ')
    print('\n')
    print('text file')
    print('json file')
    print('audio file')
    print('\n')
    type_ = input('so, in what type do you want to export the answer to ? [text / json / audio]')
    print('if you regreted it type "exit"')

    print('\n')

    while type_ not in ['text','json','audio', 'exit']:
        print('please choose one of the four...')
        type_ = input('.........')
        print('\n')


    if type_ == 'text':
        print('do you want to save only the answer or also the question? [BOTH/ANSWER]')
        print('\n')
        print('if you regreted it type "EXIT"')
        print('\n')
        response = input('......')
        print('\n')

        while response not in ['BOTH' , 'ANSWER' , 'EXIT']:
            print('please choose one of those three !')
            print('\n')

            response = input('.......')
            print('\n')


        if response == 'EXIT':
            return 0
        
        elif response == 'BOTH':
            print('the result will be exported in a txt file in the folder on witch the program is saved')
            print('\n')
            with open('result.txt','w') as f:
                f.write('Question : \n')
                f.write(answer['query'])
                f.write('\nAnswer : \n')
                f.write(answer['result'])
                f.close()
            return 1
        else:
            print('the result will be exported in a txt file in the folder on witch the program is saved')
            print('\n')

            with open('result.txt','w') as f:
                f.write('Answer : \n')
                f.write(answer['result'])
                f.close()
            return 1 
        

    elif type_ == 'json':

        json_object = json.dumps(answer)

        with open("result.json", "w") as f:
            f.write(json_object)
            return 1
        
    elif type_ == 'audio':
        print('\n')
        print('wait.....')
        print('\n')
        sound = 'the answer to the question ' + answer['query']  +  'is' + answer['result']

        client = OpenAI()
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=sound,
        )

        response.stream_to_file("result.mp3")
        return 1
    
    else:
        print('\n')
        print('okey')
        return 0
     





