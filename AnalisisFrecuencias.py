#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Diana Rocha Botello
"""
import nltk
import collections
import string
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

class AnalisisFrecuencia():

	def __init__(self):
		self.tokenListbySentence = []
		self.tokenList = []
		self.tokenListStemming = []
		self.tokenListLemmati = []
		self.diccionarioDF = {}
		self.lematizacionD = {}

	def tokenizeFile (self, fileName):
		toktok = ToktokTokenizer()
		# Tokenizador de oraciones
		es_tokenizador_oraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')
		with open(fileName, 'r', encoding='utf8') as f:
			content = f.read()
			# Obtener oraciones de un parrafo
			parrafo = content
			oraciones = es_tokenizador_oraciones.tokenize(parrafo)
			# Obtener tokens de cada oraciónn
			for s in oraciones:
				tokenSentence = toktok.tokenize(s)
				self.tokenListbySentence.append(tokenSentence)
				for t in tokenSentence:
					self.tokenList.append(t)
			f.close()

	def distribucionFrecuencias(self, tokenList):
		self.diccionarioDF = {}
		for token in tokenList:
			if token not in self.diccionarioDF:
				self.diccionarioDF.update({token:tokenList.count(token)})
		self.diccionarioDF = sorted(self.diccionarioDF.items(), key=lambda x: len(x[0]), reverse=True)
		print(self.diccionarioDF)

	def distribucionFrecuenciasInicial(self):
		self.distribucionFrecuencias(self.tokenList)

	def reduccionDimensionalidad(self):
		print("Número de Tokens Antes de la Reducción: "+str(len(self.tokenList)))
		for stopWord in stopwords.words("spanish"):
			for token in self.tokenList:
				if stopWord == token.lower() or token in string.punctuation or token in ['¿','¡', '——']:
					self.tokenList.remove(token)
		print("Número de Tokens Después de la Reducción: "+str(len(self.tokenList)))

	def reduccionDimensionalidadBySentence(self):
		for stopWord in stopwords.words("spanish"):
			i=0
			for sentence in self.tokenListbySentence:
				for token in sentence:
					if stopWord == token.lower() or token in string.punctuation or token in ['¿','¡', '——']:
						self.tokenListbySentence[i].remove(token)
				i+=1
		print(self.tokenListbySentence)

	def distribucionFrecuenciasStemming(self):
		stemmer = SnowballStemmer("spanish")
		for t in self.tokenList:
		# Obtener la raiz
			self.tokenListStemming.append(stemmer.stem(t.lower()))
		#print(self.tokenListStemming)
		self.distribucionFrecuencias(self.tokenListStemming)

	def getLematizacionDiccionario(self):
		with open('lemmatization-es.txt', 'r', encoding='utf8') as f:
			key = ''
			values = []
			for line in f:
				l = line.split()
				if key == '':
					key = l[0]
					values.append(l[1])
				elif key == l[0]:
					values.append(l[1])
				else:
					self.lematizacionD.update({key:values})
					key = l[0]
					values = []
					values.append(l[1])
			self.lematizacionD.update({key:values})
			#print(self.lematizacionD)
			f.close()

	def getLematizacionDiccionarioSimple(self):
		with open('lemmatization-es.txt', 'r', encoding='utf8') as f:
			key = ''
			values = []
			for line in f:
				l = line.split()
				self.lematizacionD.update({l[1]:l[0]})
			#print(self.lematizacionD)
			f.close()

	def distribucionFrecuenciasLematizacion(self):
		self.getLematizacionDiccionario()
		lematizado = False
		for token in self.tokenList:
			lematizado = False
			for key, values in self.lematizacionD.items():
				if token.lower() in values:
					self.tokenListLemmati.append(key)
					lematizado = True
			if lematizado == False:
				self.tokenListLemmati.append(token)
		#print(self.tokenListLemmati)
		self.distribucionFrecuencias(self.tokenListLemmati)

	def distribucionFrecuenciasLematizacionSimple(self):
		self.getLematizacionDiccionarioSimple()
		for token in self.tokenList:
			diccionarioRaiz = self.lematizacionD.get(token.lower(), -1)
			if diccionarioRaiz != -1:
				self.tokenListLemmati.append(diccionarioRaiz)
			else:
				self.tokenListLemmati.append(token)
		#print(self.tokenListLemmati)
		self.distribucionFrecuencias(self.tokenListLemmati)

if __name__ == "__main__":
	a = AnalisisFrecuencia()
	a.tokenizeFile("practica3.txt")
	print("TOKENS DEL ARCHIVO practica3.txt")
	print(a.tokenList)
	print("-----------------------------------------------")
	input("Press Enter to continue...")
	print("Distribución de frecuencias practica3.txt")
	a.distribucionFrecuenciasInicial()
	print("-----------------------------------------------")
	input("Press Enter to continue...")
	print("Reducción de la Dimensionalidad practica3.txt")
	a.reduccionDimensionalidad()
	print("-----------------------------------------------")
	input("Press Enter to continue...")
	print("Distribución de frecuencias Stemming practica3.txt")
	a.distribucionFrecuenciasStemming()
	print("-----------------------------------------------")
	input("Press Enter to continue...")
	print("Distribución de frecuencias Lematización practica3.txt")
	a.distribucionFrecuenciasLematizacionSimple()
	print("-----------------------------------------------")