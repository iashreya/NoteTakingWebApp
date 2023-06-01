from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import os
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello_world():
	try:
		file = open("notes.txt", "r")
	except:
		file = open("notes.txt", "a+")
		file.write("\n")
	
	return render_template('main_page.html', n=file.read())
	
@app.route('/submitted/', methods = ['GET', 'POST'])
def submitted():
	text = request.form['text']
	time = datetime.now()
	time = str(time.day)+"/"+str(time.month)+"/"+str(time.year)+"  "+str(time.hour)+":"+str(time.minute)
	print(time)
	if request.method == 'POST':
		if text!=None:
			print(text)
			temp = open("temp.txt", "w")	
			try:
				file1 = open("notes.txt", "r")
			except:
				file1 = open("notes.txt", "a+")
				file1.write("\n")
			temp.write("\n")
			temp.write(f" > {text}\n {time:>64}\n")
			temp.write("-"*80)
			temp.write(file1.read())
			temp.close()
			file1.close()
			os.remove("notes.txt")
			os.rename("temp.txt", "notes.txt")
			
		else:
			print("Text is Nonee")
			
		return render_template('submitted.html')
	
