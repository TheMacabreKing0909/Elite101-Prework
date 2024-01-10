print('hello world!!!')
name=input('Please enter your name.')
print('Hello,',name)
age=input('Please enter your age.')
print('You are',age,'years old.')
print('How may I assist you today',name,'?')
list=input('Would you like to see a list of commands?')
if list=='no':
  print('Okay, have a nice day!')
if list=='yes':
  print('Here is a list of commands:')
  print('1.        ')
  print('2.        ')
  print('3.        ')
  print('4.Generate exit')
  commands=input('Please enter the number of the command you would like to use.')
  if commands=='1':
    print('')
  elif commands=='2':
    print('')
  elif commands=='3':
    print('')
  elif commands=='4':
    print('Okay, have a nice day!')
