import os,time
#(Actmanii).TTSModeID = "{CA141FD0-AC7F-11D1-97A3-006008273001}"
f=open("All_the_ACS_characters.msh","w")
f.close()
def write(content):
    f=open("All_the_ACS_characters.msh","a")
    f.write(content)
    f.close()
content_of_directory=os.listdir()
unwanted=[]
for i in range(len(content_of_directory)):
    if ".acs" not in content_of_directory[i].lower():
        unwanted.append(i)
        print(content_of_directory[i])
for i in unwanted:
    content_of_directory.pop(i)

character_list=[]
for i in content_of_directory:
    word=""
    e=i.split()
    for b in range(len(e)):
        if e[b]=="." and e[b+1].lower()=="a" and e[b+2].lower()=="c" and e[b+3].lower()=="s":
            character_list.append(word)
            print(word)
            time.sleep(0.5)
            break
        else:
            word+=e[b]


to_write_per_character={}
for i in range(len(character_list)):
    to_write_in_character=[]
    to_write_in_character.append(f"{character_list[i]}.MoveTo {character_list[i]}CenterX, {character_list[i]}CenterY")
    to_write_in_character.append(f"{character_list[i]}.Show")
    to_write_in_character.append(f"{character_list[i]}.Speak \"I am {character_list[i]}.\"")
    to_write_in_character.append(f"{character_list[i]}.Hide")
    print(to_write_in_character)
    to_write_per_character[f"{content_of_directory[i]}"]=to_write_in_character

print(to_write_per_character)
