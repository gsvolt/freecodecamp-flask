import os
import sass
sasstext = ''
#with open('test.scss', 'r') as testsass:
#    sasstext = testsass.read()
sass.compile(dirname=('sass', 'css')) #, output_style='compressed')

#for dirpath,_,filenames in os.walk('sass'):
#    for f in filenames:
#        print(f)

#with open('css/test.css') as testcss:
#    print(testcss.read())
