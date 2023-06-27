Name: Yao Liu
NetID: yliu204

How to run:
1. download and unzip the file
2. cd to directory
3. "python import.py input.txt output.txt bonus-input.txt bonus-output.txt"


Files in zip:
import.py, input.txt, output.txt, bonus-input.txt, bonus-output.txt, README

input.txt is exactly same with the sample-input.txt file on the blackboard.
bonus-input.txt contains 4 pairs of words for users to test.
After compiling the import.py, output.txt has exactly same result with sample-output.txt on the blackboard;
In the bonus-output.txt, it generates 'green' for the first given word 'asd', 'black' for the second given word 'qwe';
'you can find matched word in brown corpus' for the third word 'hair', 'No such color name starts with this letter' for the fourth word 'zxc'

Strategies:
For words that have exact matches in Brown corpus:
The test sample for words that have exact matches in Brown corpus named "input.txt", the output file is named "output.txt".
Read the strings in the input.txt file, put them into list named "inputArray" while separate the original text with with spaces and new lines.
(eg: ['b', 'ribbon', 'b', 'hair',...'w', 'teeth'])
Connect the adjacent two elements together, assign every element into new list named connectArray.
(eg: ['bribbon', 'ribbonb', 'bhair',...'wteeth'])
Put the even-index elements into test function, which return the color name words with the maximum occurrence.
(eg: pass ['bribbon', 'bhair',...'wteeth'] into test(noun) function)

In test(noun) function, we accept the arguments. In nested loop, the first loop searches sentences in brown corpus and the second loop searches each word in this sentence.
For two words that next to each other, concatenate the first letter in the first word with the second word, and lemmatize them before comparision.
Compare the concatenation and lemmatisation results with the passed argument.
If they are equal, append the first word to the list named "firstWord". Return the firstWord list after all loops end.
Calculate the word with maximum occurrence, write it in output.txt file

For words that do not have exact matches in Brown corpus:
I used two functions, ifContain(word) and initialTestBonus(initial), to make a guess. 
ifContain(word) takes the second word as argument and test if brown corpus has at least one exact match with this word.
Returns True if corpus has the match word, returns False if no match word.
initialTestBonus(initial) takes the given initial letter as the argument. The colorArray list contains most color names
(not includes compound color names, like "lightblue", "deepskyblue", "dimgray" because they can be searched by the stem color names they contains)
First check the initial letter of each element in colorArray. If same, store this color word in a new array.
Loop the brown corpus, calculate the occurrence of each selected color name words. Return the color name with maximum occurrence with the given initial.
If no color name with the given initial letter, return 'No such color name starts with this letter'
When testing the bonus, first use ifContain(word) func to determine if the second word in bonus-input.txt exists in the brown corpus.
If exists, append 'you can find matched word in brown corpus' to list.
If not exist, call initialTestBonus func, passing the first letter in the bonus-input.txt as initial.
Append the return result to the list, generate the bonus-output.txt file.

