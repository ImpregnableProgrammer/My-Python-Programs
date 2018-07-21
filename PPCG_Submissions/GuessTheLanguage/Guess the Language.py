# Following method did not really work out
    # from selenium.webdriver import*
    # from selenium.webdriver.common.keys import Keys
    # import time;
    # o=input().replace('<LN>','\n')
    # D=PhantomJS()
    # Websites={g:i for i,g in enumerate(["https://repl.it/languages/"+i for i in['python','ruby','javascript_web','brainfuck']])}
    # Website=''
    # print(Websites)
    # for i in Websites.keys():
    #     D.get(i)
    #     try:D.switch_to.alert.accept()
    #     except:pass
    #     time.sleep(5)
    #     L=D.find_element_by_class_name("ace_text-input")
    #     L.clear()
    #     L.send_keys(o)
    #     # try:
    #     #     D.save_screenshot('Screenshot.png')
    #     #     print('Screenshot')
    #     # except Exception as e:
    #     #     print(e)
    #     L.send_keys(Keys.COMMAND,Keys.ENTER)
    #     time.sleep(5)
    #     try:
    #         try:
    #             D.switch_to.alert.dismiss()
    #         except:
    #             pass
    #         D.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div[4]/pre/span[@class='error']")
    #         print("hi")
    #         continue
    #     except Exception as e:
    #         print(e)
    #         Website=i
    #         break
    # print(Websites[Website])

with open('Language_Snippets_For_PPCG_Guess_the_Language_Challenge.xlsx','r')as F:
    print(F.readline().encode('UTF-8'))
# 274 bytes
import re;R=re.fullmatch;W=lambda Y:[[[[[[[7,6]['⍵'in Y],5]['@'in Y],4][R('[><-;+\(\)=\-."\[\]!]+',Y)],3][any(i in Y for i in['#include','main(','#define'])],2]['Take Northern Line'in Y],1][any(i in Y for i in['public static void main','java.util'])],0][R('[\[\]<>.\-]+',Y)]