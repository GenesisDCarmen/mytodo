#!/usr/bin/env python2
#Copyright (C) 2015 Mohamed Aziz knani

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>

import argparse
from sys import argv
from tools import *

a =  loadUserConfig()

def argument_parser():
  parser = argparse.ArgumentParser(description='mytodo script')
  parser.add_argument('-la', '--listall', help='List all todo\'s', dest='listall', action='store_true')
  parser.add_argument('-l', '--list', help='List undone todo\'s', dest='ls', action='store_true')
  parser.add_argument('-u', help='Set up your username from the database' ,dest='user')
  parser.add_argument('-p', help='Set up your password from the database', dest='passwd')
  parser.add_argument('-a', help='Add a new todo', dest='add')
  parser.add_argument('-d', '--done'  , help='Mark as done', dest='done')
  parser.add_argument('-ud', '--undone'  , help='Mark as undone', dest='undone')
  parser.add_argument('-r', '--remove'  , help='Remove an entry', dest='remove')
  parser.add_argument('-t', '--tag', help='Search by tag')
  args = parser.parse_args()
  return (args, args.user or a['username'], args.passwd or a['password'])

def display(out):
  try:
    from colorama import init, Fore
  except ImportError:
    # Well that's my ugly hack
    class Fore:
      YELLOW = ''
      RESET  = ''
      GREEN  = ''
      RED    = ''
  else : init()
  try:
    TICK = u'\u2713'.encode(sys.stdout.encoding, errors='strict')
    ERROR = Fore.RED+u'\u2718'.encode(sys.stdout.encoding, errors='strict')
  except UnicodeEncodeError :
    ERROR = 'Not Yet'
    TICK = 'Done'
  for row in out:
    dayz = dy(row[0])
    print u'%i) %s, %s %s' % (row[3], row[4].encode('utf-8'), Fore.YELLOW+dayz+Fore.RESET,
                            Fore.GREEN+TICK+Fore.RESET \
                          if row[2] else Fore.RED+ERROR+Fore.RESET)


if __name__ == '__main__':
  arguments, a['username'], a['password'] = argument_parser()
  #try:
  me = Client(a['username'], a['password'])
  if arguments.listall:
    out = me.listall()
    #print out
    display(out)
  elif arguments.add:
    me.add(arguments.add)
  elif arguments.done:
    me.done(arguments.done)
  elif arguments.undone:
    me.undone(arguments.undone)
  elif arguments.ls:
    out = me.ls()
    display(out)
  elif arguments.remove:
    me.remove(arguments.remove)
  elif arguments.tag:
    out = me.category(arguments.tag)
    display(out)
  #except Exception as e:
  #  print e
  #  print 'Server is closed, please run it'
  #  exit(0)
  #print user


