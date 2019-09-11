#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Diana Rocha Botello
"""
import re
import string
from nltk.corpus import stopwords
from nltk.metrics.distance import edit_distance
from AnalisisFrecuencias import AnalisisFrecuencia

class CorrectorOrtografico():

	def __init__(self):
		self.Namearchivo = "corrigeme.txt"
		self.af = AnalisisFrecuencia()
		self.af.getLematizacionDiccionarioSimple()
		self.diccionarioGeneral = self.af.lematizacionD.copy()
		self.getListadoGeneral()

	def getListadoGeneral(self):
		with open('listado-general.txt', 'r', encoding='utf8') as f:
			for line in f:
				l = line.split()
				self.diccionarioGeneral.update({l[0]:"-1"})
			f.close()

	def LevenshtineDistance (self, w1, w2):
		distance = edit_distance(w1, w2)
		return distance

	def getMenorDistancia(self, lista, word):
		distanciaMenor = 10000
		palabra = word
		for w in sorted(lista):
			distancia = self.LevenshtineDistance(word, w)
			if distancia < distanciaMenor:
				distanciaMenor = distancia
				palabra = w
		if distanciaMenor > 2:
			palabra = word
		return palabra

	def correctorOrtografico(self, corregido):
		self.af.tokenizeFile(self.Namearchivo)
		f = open(corregido, 'w', encoding='utf8')
		for sentence in self.af.tokenListbySentence:
			line = ''
			for token in sentence:
				word = token
				if token.lower() not in stopwords.words("spanish") and token not in string.punctuation and token not in ['¿','¡', '——','–','…','«','»']:
					#print("---------------------------------------------")
					result = [(key) for key, value in self.diccionarioGeneral.items() if key.startswith(token[0]) and key.endswith(token[len(token)-1])]
					word = self.getMenorDistancia(result, token)
					#print("Token: "+token+" Palabra: "+word)
				line += word + " "
			f.write(line+"\n")
			print("---------------------------------------------")
			print(line)

if __name__ == "__main__":
	corrector = CorrectorOrtografico()
	corrector.correctorOrtografico("corregido.txt")