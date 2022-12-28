def splitmulti(msg):
    return msg.split('\n')

msg = '''hello this is
a multiline string'''
print(splitmulti(msg))
