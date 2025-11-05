
#这个项目是为了验证字符串是否回文，并且需要忽略中间出现的空格，标点和大小写


def clean_and_judge():

        string=input(">")
        cleaned_string=[]
        character=0

        for character in string:
            if 48<=ord(character)<=57 or 65<=ord(character)<=90 or 97<=ord(character)<=122 :
                cleaned_string.append(character)

        if character==character[::-1]:
            print("Yes, it is a palindrome.")


        else:
            print("No, it is not a palindrome.")

clean_and_judge()


