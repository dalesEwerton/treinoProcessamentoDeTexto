# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:49:34 2016

@author: Dales Ewerton
"""

import nltk
import string
import math


topWordsNumber = 10

"""
This method receives a text file 
and returns the 10 most used words in the file

@return topWords
"""
def getTopWords(textFile):
    text = textFile.read().lower()
    allWords = text.split()
    topWords = nltk.FreqDist(allWords).most_common(topWordsNumber)
    return topWords

"""
this method calculates the euclidian distance between 2 histograms of words

@return distance
"""
def getEuclidianDistance(topWordsText, topWordsPhrases):
    distance = 0
    for i in range(topWordsNumber):
        for j in range(topWordsNumber):
            if(topWordsPhrases[j][0] == topWordsText[i][0]):
                distance = distance + (topWordsText[i][1]**2)
    
    distance = math.sqrt(distance)
    return distance
    
"""
The main method
It is not  automatically called if you use this as a module of another file 
"""    
def main():
    
    fileMachado = open("Machado de Assis.txt", 'r')
    fileBandeira = open("Manoel Bandeira.txt", 'r')
    
    topWordsMachado = getTopWords(fileMachado)
    topWordsBandeira = getTopWords(fileBandeira)
    
    phraseList = raw_input("Informe uma frase de Machado de Assis ou Manoel Bandeira com no minimo 10 palavras: ").split()
    topWordsPhrase = nltk.FreqDist(phraseList).most_common(topWordsNumber)
    
    distanceMachado = getEuclidianDistance(topWordsMachado, topWordsPhrase)
    distanceBandeira = getEuclidianDistance(topWordsBandeira, topWordsPhrase)
    
    if(distanceMachado > distanceBandeira):
        print "A frase provavelmente pertence a Machado de Assis"
    elif(distanceBandeira > distanceMachado):
        print "A frase provavelmente pertence a Manoel Bandeira"
    else:
        print "As frases tem a mesma semelhança tanto com Machado quanto com Manoel"

        
if __name__ == "__main__":
    main()