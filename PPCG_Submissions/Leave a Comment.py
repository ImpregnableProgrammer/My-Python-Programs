# This Challenge: http://codegolf.stackexchange.com/questions/84546/leave-a-comment

# The First Test Version
# from selenium.webdriver import*
# import time
# U=input('Email: ')
# P=input('Password: ')
# C='comment'
# driver=Firefox()
# driver.get('http://ppcg.lol')
# driver.find_element_by_link_text('log in').click()
# driver.find_element_by_id('email').send_keys(U)
# driver.find_element_by_id('password').send_keys(P)
# driver.find_element_by_id('submit-button').click()
# time.sleep(5)
# driver.get('http://ppcg.lol/q/84546')
# driver.find_element_by_link_text('add a '+C).click()
# E=driver.find_element_by_name(C)
# E.click()
# E.send_keys('1234567890123456')
# time.sleep(1)
# E.submit()

# Firefox – Golfed: Only lambda function = 432 bytes
# O=lambda U,P:exec("from selenium.webdriver import*;import time;D=Firefox();I=lambda k:D.find_element_by_name(k);C='comment';D.get('http://www.codegolf.stackexchange.com/users/login');I('email').send_keys(U);Z=I('password');Z.send_keys(P);Z.submit();D.get('http://www.codegolf.stackexchange.com/questions/84546');D.find_element_by_link_text('add a '+C).click();E=I(C);E.send_keys('1234567890123456');time.sleep(1);E.submit()",locals())
# O('kapur2001@gmail.com',''.join([chr((ord(i)>>8)-2)for i in'倀挀䨀儀吀☀㈀⨀']))

# Chrome – Golfed: Only lambda function = 431 bytes
O=lambda U,P:exec("from selenium.webdriver import*;import time;D=Chrome();I=lambda k:D.find_element_by_name(k);C='comment';D.get('http://www.codegolf.stackexchange.com/users/login');I('email').send_keys(U);Z=I('password');Z.send_keys(P);Z.submit();D.get('http://www.codegolf.stackexchange.com/questions/84546');D.find_element_by_link_text('add a '+C).click();E=I(C);E.send_keys('1234567890123456');time.sleep(1);E.submit()",locals())
O('kapur2001@gmail.com',''.join([chr((ord(i)>>8)-2)for i in'倀挀䨀儀吀☀㈀⨀']))

# Required for bottom two answers
# U='kapur2001@gmail.com';P=''.join([chr((ord(i)>>8)-2)for i in'倀挀䨀儀吀☀㈀⨀'])

# Firefox – Golfed Fully: 404 bytes
# from selenium.webdriver import*;import time;D=Firefox();I=lambda k:D.find_element_by_name(k);C='comment';D.get('http://www.codegolf.stackexchange.com/users/login');I('email').send_keys(U);Z=I('password');Z.send_keys(P);Z.submit();D.get('http://www.codegolf.stackexchange.com/questions/84546');D.find_element_by_link_text('add a '+C).click();E=I(C);E.send_keys('1234567890123456');time.sleep(1);E.submit()

# Chrome – Golfed Fully: 403 bytes
# from selenium.webdriver import*;import time;D=Chrome();I=lambda k:D.find_element_by_name(k);C='comment';D.get('http://www.codegolf.stackexchange.com/users/login');I('email').send_keys(U);Z=I('password');Z.send_keys(P);Z.submit();D.get('http://www.codegolf.stackexchange.com/questions/84546');D.find_element_by_link_text('add a '+C).click();E=I(C);E.send_keys('1234567890123456');time.sleep(1);E.submit()