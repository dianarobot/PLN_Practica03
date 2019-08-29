#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Diana Rocha Botello
"""
import nltk
import collections
from nltk.tokenize.toktok import ToktokTokenizer

class AnalisisFrecuencia():

	def __init__(self):
		self.tokenListbySentence = []
		self.tokenList = []
		self.diccionarioDF = {}

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

	def distribucionFrecuencias(self):
		for token in self.tokenList:
			if token not in self.diccionarioDF:
				self.diccionarioDF.update({token:self.tokenList.count(token)})
		self.diccionarioDF = sorted(self.diccionarioDF.items(), key=lambda x: len(x[0]))
		print(self.diccionarioDF)

if __name__ == "__main__":
	a = AnalisisFrecuencia()
	a.tokenizeFile("practica3.txt")
	print(a.tokenList)
	a.distribucionFrecuencias()
