import urllib
def read_text():
    quote = open("/Users/souvikbanerjee/Desktop/Data_Science/Full-Stack-Nanodegree/1_Programming_Fundamentals_and_the_Web/lesson_8/movie_quotes.txt")
    contents_file = quote.read()
    print(contents_file)
    quote.close()
    check_profenity(contents_file)

def check_profenity(text_to_check):
    ''' function to check curse words'''
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    connection.close()
    if 'true' in output:
        print('Contains Curse words')
    else:
        print('No Curse Words')

read_text()