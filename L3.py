# 1.
# a.
try:
    a= 1/0
except Exception as e:
    print(f"{e} - Cannot divide by zero.")

# 2.
# Yes. the code will print "finally"

# 3.
# All types.

# 4.
# The indication of the exception that occur is poor.

# 5.
    # a. except IOError
    # This handler wil catch input\ output errors.
    # It is an error raised when an input/output operation fails, such as the print statement or the open() function
    # when trying to open a file that does not exist.

    # b. except ZeroDivisionError
    # Raised when the second argument of a division or modulo operation is zero.

# 6.
with open("words.txt",'w') as writefile:
    writefile.write("Muli")

# 7.
with open("words.txt",'r') as readfile:
    for line in readfile.readlines():
        print(line)

# 8.
with open("hebrew.txt",'w',encoding='utf-8') as file:
    content = "מה המצב"
    file.write(content)

# 9.
from flask import Flask

app = Flask(__name__)

@app.route('/content')
def content():
    return open("hebrew.txt").read(), 200
@app.route('/register')
def register():
    open("hebrew.txt", 'a').write("hello")
    return "success", 201

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=30000)

# 10.
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB',(800,600))
img.save("test.png","PNG")
img.show()