import subprocess,os,time,random















def voicemode():
    seed = random.randint(5,20)
    for x in range(30):    
        print("Loading",x+seed,"%")
        time.sleep(0.05)
        os.system('clear')
        if x==29:
            os.system('clear')
            print("Loading",100,"%")
            time.sleep(1)
            print("Starting Systems")
            time.sleep(2)
            os.system('clear')        

    print("---Welcome to IEMA Smart Bot System---")
    print("|READY|\n")

    # Voice Triggers
    greet = ["hello","hi","hey","ok","morning","fine"]
    cam = ["can you see me","camera","take a photo","picture","selfie"]
    m_activity = ["play music","song","songs","gaan","audio","music"]

    # Unknown Word Processing
    unknown = []

    # Voice List
    player = "/usr/bin/cvlc"
    voices = ["/home/nine/Desktop/voices/audio1.mp3","/home/nine/Desktop/voices/bored.mp3","/home/nine/Desktop/voices/camerasmile.mp3","/home/nine/Desktop/voices/canhelp.mp3","/home/nine/Desktop/voices/comment1.mp3","/home/nine/Desktop/voices/howyoudoin.mp3"]

    # Process Controller
    timer = 0
    i = 3

    # Bot Logic
    while(True):
        
        command = str(input())
        if command in greet:
            i = 5
            timer = 5
        elif command == "Bye" or command == "bye":
            os.system('clear') 
            print("Goodbye !!")
            exit()
        elif command in cam:
            i = 2 
            timer = 5             
        elif command in m_activity:
            i = 0
            timer = 100
        else:
            new = random.choice([1,3,4])
            i = new
            timer = 5
            os.system('clear')
            if command not in unknown:
                unknown.append(command) # Added Unknown Word to System Once       
        
    # Intelli Playback System    
        try:    
            subprocess.call([player, voices[i]],timeout = timer)        
        except:
            pass
            os.system('clear') 
            print("|SYSTEM PASS|")
            time.sleep(0.5)
            os.system('clear')
            print("---Welcome to IEMA Smart Bot System---")
            print("|READY|\n")
            if len(unknown)>0:
                print("Currently Unknown Words")
                print(unknown)
                print("------")

voicemode() # Voice Activity of Bot














# Voice Files Directory

'''
Saudade Music - /home/nine/Desktop/voices/audio1.mp3
Hello - 
Nice day, right -
I'm bored -
I'm looking at you....Smile -
Can I help you - 

'''
