'''
def copy (orig, cp):
    with open("story.txt", "r", encoding = "utf8") as f:
        with open("story_copy.txt", "w") as f1:
            for line in f:
                f1.write(line)
'''                
                
def copy (orig, cpy):
    with open(orig, "r", encoding = "utf8") as f:
        with open(cpy, "w") as f1:
            for line in f:
                f1.write(line)
                
copy("story.txt", "story_copy.txt")


def copy_and_reverse(orig, reversed_copy):
    with open(orig, "r", encoding = "utf8") as file:
        text = file.read()
 
    with open(reversed_copy, "w") as new_file:
        new_file.write(text[::-1])
                
copy_and_reverse("story.txt", "story_reversed.txt")

def statistics(file_name):
    
    line_count = 0
    word_count = 0
    char_count = 0
    
    with open(file_name, "r", encoding = "utf8") as f:
        for line in f:
            words = line.split()
            line_count += 1
            word_count += len(words)
            char_count += len(line)
    return {"lines":line_count, "words":word_count, "characters":char_count}

statistics("story.txt")

'''
#read in myhiddentext.txt
txt_file = open("myhiddentext.txt",'r')
file_data = txt_file.read()
txt_file.close()

#replace "hidden" with "math"
new_txt_file = file_data.replace("hidden", "math")
txt_file = open("myhiddentext.txt",'w')
txt_file.write(new_txt_file)
txt_file.close()
'''

def find_and_replace(file_name, search_word, replace_word):

    with open(file_name, "r", encoding = "utf8") as f:
        filedata = f.read()        

    filedata = filedata.replace(search_word, replace_word)
    
    with open(file_name, "w", encoding = "utf8") as f:
        f.write(filedata)
            
find_and_replace("story.txt", 'Alice', 'Colt') 
        
        
        
        
        