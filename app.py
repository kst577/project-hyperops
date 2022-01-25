from flask import Flask, render_template, request,redirect
import random
import numpy as np
import pandas as pd

app = Flask(__name__)
hours = []
df = pd.DataFrame({'Hour':[],'Group 1':[],'Group 2':[],'Group 3':[],'Group 4':[],'Group 5':[],'Group 6':[]})
df2 = pd.DataFrame({'Total':[]})
# group1_full_operations=[]
# group2_full_operations=[]
# group3_full_operations=[]
# group4_full_operations=[]
# group5_full_operations=[]
# group6_full_operations=[]

def rd(n, total_sum):
    nums = np.random.rand(n)
    return nums/np.sum(nums)*total_sum
def hello():
	return "Hello"

@app.route("/index", methods=['GET','POST'])
def index():
	global hours
	
	if request.method=='POST':
		inp1 = request.form.get('input1')
		inp2 = request.form.get('input2')
		inp3 = request.form.get('input3')
		inp4 = request.form.get('input4')
		inp5 = request.form.get('input5')
		inp6 = request.form.get('input6')
		inp7 = request.form.get('input7')
		inp8 = request.form.get('input8')
		inp9 = request.form.get('input9')
		inp10 = request.form.get('input10')
		inp11 = request.form.get('input11')
		inp12 = request.form.get('input12')
		inp13 = request.form.get('input13')
		inp14 = request.form.get('input14')
		inp15 = request.form.get('input15')
		inp16 = request.form.get('input16')
		inp17 = request.form.get('input17')
		inp18 = request.form.get('input18')
		hours.append([inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11,inp12,inp13,inp14,inp15,inp16,inp17,inp18])
		print(hours)
		return redirect('operations')
		
	return render_template('index.html', data2=hours)

@app.route("/operations")
def operations():
	global hours
	global df
	group1_full_operations=[]
	group2_full_operations=[]
	group3_full_operations=[]
	group4_full_operations=[]
	group5_full_operations=[]
	group6_full_operations=[]
	for i in hours[0]:
		nums = np.random.rand(13)
		a = nums/np.sum(nums)*float(i)
		b=a.tolist()
		c=[int(i) for i in b]
		summ=0
		#per_minute_flow=int(i/60)

		# Assigning the number of people to respected platforms

		p1=c[0]
		p2=c[1]
		p3=c[2]
		p4=c[3]
		p5=c[4]
		p6=c[5]
		p7=c[6]
		p8=c[7]
		p9=c[8]
		p10=c[9]
		p11=c[10]
		p12=c[11]
		p13=c[12]
		 
		group1_full_operations.append(p1+p2+p3)
		group2_full_operations.append(p4+p5)
		group3_full_operations.append(p6+p7)
		group4_full_operations.append(p8+p9)
		group5_full_operations.append(p10+p11)
		group6_full_operations.append(p12+p13)

	time=['6:00 AM','7:00 AM','8:00 AM','9:00 AM','10:00 AM','11:00 AM','12:00 PM','1:00 PM','2:00 PM','3:00 PM','4:00 PM','5:00 PM','6:00 PM','7:00 PM','8:00 PM','9:00 PM','10:00 PM','11:00 PM']
		# print(len(time))
		# print(len(group1_full_operations))
		# print(len(group2_full_operations))
		# print(len(group3_full_operations))
		# print(len(group4_full_operations))
		# print(len(group5_full_operations))
		# print(len(group6_full_operations))
	df['Hour']=time
	df['Group 1'] = group1_full_operations
	df['Group 2'] = group2_full_operations
	df['Group 3'] = group3_full_operations
	df['Group 4'] = group4_full_operations
	df['Group 5'] = group5_full_operations
	df['Group 6'] = group6_full_operations
	df2['Total']=hours
	#df = pd.concat([df,df2],axis=1)
	result = df.to_html()
	print(result)
	return render_template("operations.html",output=[df.to_html(index=False)], titles=df.columns.values, hours=hours,output2=[df2.to_html(index=False)], titles2=df2.columns.values)



if __name__ == '__main__':
	app.run(debug=True)