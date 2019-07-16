#!/usr/bin/python3
paragraph= 'Hello, i am Jaime Marquez. And i am a programer'


def isVowel(c):
    return c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'

def countAndExchange(p):
    numVowels = 0
    vDictionary ={'a': 'e','e':'i','i':'o','o':'u','u':'a',
              'A': 'E','E':'I','I':'O','O':'U','U':'A'}
    newP = ''
    for v in p:
        if isVowel(v):
            numVowels+=1
            newP+=vDictionary[v]
            continue
        newP+=v      
    return numVowels,newP

def main():
    numV,exParagraph= countAndExchange(paragraph)
    print ('El número de vocales es: ',numV)
    print ('El párrafo o frase original es: {0} y la de las vocales intercambiadas es: {1} '.format(paragraph,exParagraph))

if __name__ == '__main__':
    main()

    