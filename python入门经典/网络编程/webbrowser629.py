
def web():
    import webbrowser
    url = 'www.baidu.com'
    #webbrowser.open_new_tab(url)
    webbrowser.open_new(url)

def  testlib():
    import urllib,re
    f = urllib.urlopen('http://www.baidu.com/')
    lines = f.read()
    line_1 = re.findall('title',lines)
    print (line_1)

if __name__ == '__main__':
    #web()
    testlib()
