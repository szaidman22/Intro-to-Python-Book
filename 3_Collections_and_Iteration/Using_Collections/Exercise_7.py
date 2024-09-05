# Write Python code to replace 
# all the : characters in the string 
# below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info = info.replace(':','+')
print(info)


#or 
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info = '+'.join(info.split(':'))
print(info)
