#!/usr/bin/ python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/<binario>")
def binf(binario):
	binari = {}
	with open("binari.txt") as f:
		for line in f:
			(key, val) = line.split("\\")
			binari[int(key)] = val
	work = binari[int(binario)].split("|")
	destinazione = work[0].upper()
	gestore =  work[1].upper()
	partenza = work[2]
	numero =work[3] 
	altreinfo=work[4].upper()
	return render_template('binari.html',
                           bin=binario,
                           dest=destinazione,
						   gest=gestore,
							part=partenza,
							num=numero,
							altro=altreinfo,
)
if __name__ == "__main__":
	app.run()
