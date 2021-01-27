from Word import *

from collections import defaultdict
from pathlib import Path
#import pandas as pd
import os
import re

class Actions:

    def __init__(self):
        self

    def remove(self, list):
        pattern = '[0-9]'
        list = [re.sub(pattern, '', i) for i in list]
        return list

    def train(self):
        list_of_words=[]
        my_dir_path = os.path.abspath("../pythonProject1/enron1/ham")



        print(my_dir_path)
        k=0
        word=""
        word2=""
        check=False

        results = defaultdict(list)
        for file in Path(my_dir_path).iterdir():
            #counter_ham = counter_ham+1
            k=k+1
            print(k)
            with open(file, "r") as file_open:
                results["file_name"].append(file.name)
                results["text"].append(file_open.read())
                #results["text"].translate(None, '0123456789')
                results["text"]=self.remove(results["text"])

                for line in results["text"]:
                # reading each word
                    for word in line.split():
                        for char in word:
                            if char.isalnum():
                                word2 += char
                        if word2=="":
                            continue
                        #print(word2)

                        for x in list_of_words:
                            if x.word == word2:
                                #print("i found it!")
                                check =True
                                x.add_ham()
                                break
                        if not check:
                            list_of_words.append(Word(word2))
                            #x.add_ham()
                            #print("add it!")
                            list_of_words[len(list_of_words) -1].add_ham()

                        check=False
                        word2=""
            results["text"].clear()


        my_dir_path = os.path.abspath("../pythonProject1/enron1/spam")


        print(my_dir_path)
        k=0
        results = defaultdict(list)
        for file in Path(my_dir_path).iterdir():
            #counter_spam = counter_spam+1
            k=k+1
            print(k)
            with open(file, "r") as file_open:
                results["file_name"].append(file.name)
                results["text"].append(file_open.read())
                #results["text"].translate(None, '0123456789')
                results["text"]=self.remove(results["text"])

                for line in results["text"]:
                # reading each word
                    for word in line.split():
                        for char in word:
                            if char.isalnum():
                                word2 += char
                        if word2=="":
                            continue
                        #print(word2)

                        for x in list_of_words:
                            if x.word == word2:
                                #print("i found it!")
                                check =True
                                x.add_spam()
                                break
                        if not check:
                            list_of_words.append(Word(word2))
                            #x.add_ham()
                            #print("add it!")
                            list_of_words[len(list_of_words) -1].add_spam()

                        check=False
                        word2=""
            results["text"].clear()

            file1 = open("dane1234.txt", "w+")
            for obj in list_of_words:
                file1.write(obj.word)
                file1.write(" ")
                file1.write(str(obj.spam))
                file1.write(" ")
                file1.write(str(obj.ham))
                file1.write("\n")
            file1.close()


        ##for obj in list_of_words:
        ##    print( obj.word, obj.spam, obj.ham, sep =' ' )

        # sum= counter_ham + counter_spam
        # ps=counter_spam/sum
        # ph=counter_ham/sum
        # print(ps)
        # print(ph)

    def check_all(self, isHam):
        list_data = []

        counter_spam = 8996
        counter_ham = 13545

        sum = counter_ham + counter_spam
        ps = counter_spam / sum
        ph = counter_ham / sum
        print(ps)
        print(ph)

        with open("dane1234.txt", "r") as file_open:

            for line in file_open:
                tmp = Word("")
                i = 0
                # reading each word
                for word in line.split():
                    if i == 0:
                        tmp.word = word
                    if i == 1:
                        tmp.spam = int(word)
                    if i == 2:
                        tmp.ham = int(word)
                        list_data.append(tmp)
                        tmp = None
                    i = i + 1

        list_mail = []
        word2 = ""


        result_spam = 0
        result_ham = 0
        my_dir_path = os.path.abspath("../pythonProject1/enron6/spam")

        print(my_dir_path)
        k = 0
        results = defaultdict(list)
        for file in Path(my_dir_path).iterdir():

            k = k + 1
            print(k)
            with open(file, "r") as file_open:
                results["file_name"].append(file.name)
                results["text"].append(file_open.read())
                results["text"] = self.remove(results["text"])

                for line in results["text"]:
                    # reading each word
                    for word in line.split():
                        for char in word:
                            if char.isalnum():
                                word2 +=char
                        if word2 == "":
                            continue

                        list_mail.append(Word(word2))
                        word2 = ""


                results["text"].clear()

                for x in list_mail:
                    for y in list_data:
                        if x.word == y.word:
                            x.spam = y.spam
                            x.ham = y.ham
                            break


                probability_spam = 0
                probability_ham = 0



                for obj in list_mail:

                    if probability_ham == 0:
                        if obj.probability_ham() != 0:
                            probability_ham = obj.probability_ham()
                    else:
                        if obj.probability_ham() != 0:
                            probability_ham = probability_ham * obj.probability_ham()
                    if probability_spam == 0:
                        if obj.probability_spam() != 0:
                            probability_spam = obj.probability_spam()
                    else:
                        if obj.probability_spam() != 0:
                            probability_spam = probability_spam * obj.probability_spam()



                if probability_ham * ph == 0:
                    result = 2
                else:
                    result = (probability_spam * ps) / (probability_ham * ph)

                if result > 1:

                    result_spam = result_spam + 1
                else:

                    result_ham = result_ham + 1
                list_mail.clear()


        print(result_ham)
        print(result_spam)
        if isHam:
            all = result_ham * 100 / (result_ham + result_spam)
        else:
            all = result_spam * 100 / (result_ham + result_spam)
        print(all)


    def check_one(self):
        list_data = []

        counter_spam = 3672
        counter_ham = 1500

        sum = counter_ham + counter_spam
        ps = counter_spam / sum
        ph = counter_ham / sum
        print(ps)
        print(ph)

        with open("danetest.txt", "r") as file_open:

            for line in file_open:
                tmp = Word("")
                i = 0
                # reading each word
                for word in line.split():
                    if i == 0:
                        tmp.word = word
                    if i == 1:
                        tmp.spam = int(word)
                    if i == 2:
                        tmp.ham = int(word)
                        list_data.append(tmp)
                        tmp = None
                    i = i + 1

        list_mail = []
        word2 = ""

        with open("mail.txt", "r") as mail:

            mail=self.remove(mail)

            for line in mail:
            # reading each word
                for word in line.split():
                    for char in word:
                        if char.isalnum():
                            word2 += char
                    if word2=="":
                        continue

                    list_mail.append(Word(word2))


                    word2=""
        for x in list_mail:
            for y in list_data:
                if x.word == y.word:
                    x.spam = y.spam
                    x.ham = y.ham
                    break



        probability_spam = 0
        probability_ham = 0



        for obj in list_mail:
            # if not check_first:
            #    probability_ham=obj.probability_ham()
            #    probability_spam=obj.probability_spam()
            #    check_first=True
            # else:
            #    probability_ham=probability_ham*obj.probability_ham()
            #    probability_spam=probability_spam*obj.probability_spam()
            if probability_ham == 0:
                if obj.probability_ham() != 0:
                    probability_ham = obj.probability_ham()
            else:
                if obj.probability_ham() != 0:
                    probability_ham = probability_ham * obj.probability_ham()
            if probability_spam == 0:
                if obj.probability_spam() != 0:
                    probability_spam = obj.probability_spam()
            else:
                if obj.probability_spam() != 0:
                    probability_spam = probability_spam * obj.probability_spam()


        if probability_ham * ph == 0:
            result = 2
        else:
            result = (probability_spam * ps) / (probability_ham * ph)

        if result > 1:
             print("Podana wiadomość jest spamem")

        else:
              print("Podana wiadomość nie jest spamem")

        list_mail.clear()






