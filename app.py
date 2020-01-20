
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding:utf-8
from flask import Markup,Flask,Response,render_template, flash, request, redirect, url_for, send_from_directory
import codecs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xlsxwriter 
import os
app = Flask (__name__)



@app.route("/")
def index():
	rows = []
	dosya = open("TumKelimeKokleri.txt", "r", encoding="utf-8").read()
	words = dosya.split()
	for wor in words:
		rows.append(wor)
	return render_template('index.html',rows=rows)


txt=["1945-1962-KelimeKok.txt","1963-1980-KelimeKok.txt","1981-1999-KelimeKok.txt","2000-2019-KelimeKok.txt"]

labels = [
    '1945-1962', '1963-1980', '1981-1999', '2000-2019',
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

values=[]
@app.route('/', methods=['GET', 'POST'])
def line():
	values=[]
	if request.method == 'POST':
		for t in txt:
			dosya = open(t, "r", encoding="utf-8").read()
			word = request.form['word']
			count = 0
			words = dosya.split()
			for wor in words:
				if(wor == word):
					count += 1
			values.append(count)
	return render_template('grafik.html', title=word+' Kelimesinin Kullanım Sıklığı', max=max(values)+20, labels=labels, values=values)





if __name__ == "__main__":
	app.run(debug=True,threaded=True,host='127.0.0.1')
