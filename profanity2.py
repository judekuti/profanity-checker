import urllib

def read_text():
    quotes=open("//Users/Udacity Folders/Profanity Checker/profanity.txt")
    file_contents=quotes.read()
    print(file_contents)
    quotes.close()
    check_profanity(file_contents)

def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdyl.com/profanity?q=1" + text_to_check)
    output=connection.read()
    print (output)
    connection.close()
read_text()
 
