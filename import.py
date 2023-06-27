import nltk
import math


nltk.download('brown')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import brown
# Given list
# listA = [45, 20, 11, 50, 17, 45, 50,13, 45]
# print("Given List:\n",listA)
# res = max(set(listA), key = listA.count)
# print("Element with highest frequency:\n",res)
# print(brown.sents())

# list_of_words=['Cars', 'Cats', 'Flowers', 'Cats']
# # frequency_distribution = nltk.FreqDist(list_of_words)
# # print("The Frequency distribution is -",frequency_distribution)
# most_common_element = nltk.FreqDist(list_of_words).max()
# print ("The most common element is -",most_common_element)
#
# # list = ['1', '1', '1', '2', '2', '3']
# mostCommon = max(list, key=list.count())
# print(mostCommon)

# print(len(brown.words()))

def test(noun):
    firstWord = [];
    lemmatizer = WordNetLemmatizer()
    sents = brown.sents()
    for i in sents:
        for j in range((len(i)-1)):
            if ([lemmatizer.lemmatize(i[j][0:1]).lower()+lemmatizer.lemmatize(i[j+1])]) == noun:
            # if ([lemmatizer.lemmatize(i[j][0:1])+lemmatizer.lemmatize(i[j+1])]) == ['bribbon']:
            #     print(([lemmatizer.lemmatize(i[j][0:1]), lemmatizer.lemmatize(i[j+1])]))
    #         if [lemmatizer.lemmatize(i[j][0:1]), lemmatizer.lemmatize(i[j+1])] == item:
                firstWord.append(i[j])
    return firstWord
    # for i in range(1000):
    # for i in range(len(brown.sents())):
    #     # if noun in brown.sents()[i]:
    #         for j in range(1, len(brown.sents()[i])):
    #             if brown.sents()[i][j] == noun and brown.sents()[i][j-1][0] == singleLetter:
    #                 firstWord.append(brown.sents()[i][j-1])
    #                 break
    # return (nltk.FreqDist(firstWord).max())


# ifContain function determines if the given word is in brown corpus or not
# if contain, return True; else return False
def ifContain(word):
    sent = brown.sents()
    for i in sent:
        if word in i:
            return True
    return False


# For bonus test, I created a list that contains color names from https://www.w3.org/wiki/CSS/Properties/color/keywords#Color_keywords
# I included all basic color and part of the extended colors
# I didn't include the entended colors name that includes other color names (for example, not include names like "lightblue", "deepskyblue", "dimgray" because they can be searched by the smaller color name)
def initialTestBonus(initial):
    # initial = initial.lower()
    lemmatizer = WordNetLemmatizer()
    colorArray = ['black', 'silver', 'gray', 'white', 'maroon', 'red', 'purple', 'fuchsia', 'green', 'lime', 'olive', 'yellow', 'navy', 'blue', 'teal', 'aqua', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'brown', 'chocolate', 'chartreuse', 'coral', 'crimson', 'cyan', 'firebrick', 'fuchsia', 'gold', 'goldenrod', 'honeydew', 'indigo', 'ivory', 'khaki', 'lavender', 'linen', 'magenta', 'moccasin', 'navy', 'olive', 'orchid', 'peru', 'plum', 'pink', 'salmon', 'seashell', 'sienna', 'snow', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'wheat']
    possibleWord = [];
    sents = brown.sents()
    arrayLen = len(colorArray)
    for i in range(arrayLen):
        if colorArray[i][0:1] == initial:
            possibleWord.append(colorArray[i])
    #if no such color name that starts with the input letter
    # stop and return
    if possibleWord == []:
        return "No such color name starts with this letter"
    arrAll = [];
    for x in range(len(possibleWord)):
        for i in sents:
            for j in range((len(i))):
                if lemmatizer.lemmatize(i[j])== possibleWord[x]:
                    arrAll.append(possibleWord[x])
    maxWord = nltk.FreqDist(arrAll).max()
    return maxWord

# def check(noun, sents):
#     output = []
#     length = len(noun)
#     lemmatizer = WordNetLemmatizer()
#     for i in sents:
#         for j in range((len(i) - length +1)):
#             if [lemmatizer.lemmatize(i[j][0:1]), lemmatizer.lemmatize(i[j+1])] == ['b', 'ribbon', 'b', 'hair', 'g', 'hair', 'g', 'eye', 'r', 'lip', 'b', 'box', 'w', 'teeth']:
#                 output.append([i[j], i[j+1]])
#     return output


    # # # lemmatizer = WordNetLemmatizer()
    # # # for i in range(len(brown.words())):
    # # #     if lemmatizer.lemmatize(brown.words()[i]) == noun:
    # # #         firstWord.append(brown.words()[i-1])
    # # #         secondWord.append(brown.words()[i])
    # # # check if words in firstWord array have same first letter with given letter
    # # # only remains the matched words, put them into finalList
    # for word in firstWord:
    #     if word[0] == letter1 or word[0] == letter2:
    #         finalList.append(word)
    #
    # check the occurrence of each word in finalList
    # put result in dictionary
    # for i in range(len(firstWord)):
    #     key = firstWord[i]
    #     if statDict.get(key) == None:
    #         statDict.update({key: 1})
    #     else:
    #         statDict[key] = statDict.get(key)+1
    # since the first word is always color
    # build a dictionary that contains all one-word color word
    #
    # get the word with the highest occurrence (the highest possibility)
    # maxPossibility = max(statDict, key=statDict.get)
    # return maxPossibility
    # # print(maxPossibility)


def main():
    # test regular file
    connectArray = []
    maxList = []
    with open('input.txt', 'r') as file:
        inputString = file.read().replace('\n', ' ')
        inputArray = inputString.split()
    for x in range(len(inputArray)-1):
        connectArray.append(inputArray[x]+inputArray[x+1])
    for x in range(math.ceil(len(connectArray)/2)):
        list = test([connectArray[2*x]])
        maxm = nltk.FreqDist(list).max()
        maxList.append(maxm)
    with open('output.txt', 'w') as file:
        for i in range(len(maxList)):
            file.write(maxList[i]+' '+inputArray[2*i+1])
            file.write('\n')

    # test bonus file
    bonusMaxList = []
    with open('bonus-input.txt', 'r') as file:
        bonusString = file.read().replace('\n', ' ')
        bonusArray = bonusString.split()
    # check if the second word is in brown corpus
    for i in range(math.ceil(len(bonusArray)/2)):
        # print((ifContain(bonusArray[2*i+1])))
        # if the second word is not in the corpus(which is the hard cases where there are not any exact matches in the Brown corpus
        if (ifContain(bonusArray[2*i+1])):
            bonusMaxList.append("you can find matched word in brown corpus")
        else:
            maxiumWord = initialTestBonus(bonusArray[2*i])
            bonusMaxList.append(maxiumWord)
    with open('bonus-output.txt', 'w') as file:
        for i in range(len(bonusMaxList)):
            file.write(bonusMaxList[i]+' '+bonusArray[2*i+1])
            file.write('\n')



if __name__ == "__main__":
    main()
