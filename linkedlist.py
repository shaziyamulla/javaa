# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:31:52 2024

@author: admin
"""

class node:
    def __init__(self,data=None):
      self.data=data
      self.next-None
class singlylinkedlist:
    def __init(self):
      self.first=None
    def insertFirst(self,data):
      temp=node(data)
      temp.next=self.first
      self.first=temp
    def removeFIrst(self):
      if (self.first==None):
          print("list is empty")
      else:
          cur=self.first
          self.first=self.first.next
          print("the deleted item is",cur.data)
    def display(self):
      if(self.first==None):
          print("list is empty")
          return
      cur=self.first
      while(cur):
          print(cur.data,end="")
          cur=cur.next
    def search(self,item):
        if(self.first==None):
            if cur.data==item:
                print("item is present in linked list")
                return
            else:
                cur=cur.next
                print("item is not present in linked lidt")
                
                
          
          
    
    
        