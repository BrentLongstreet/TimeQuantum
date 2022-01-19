"""
Name: Brent Longstreet
Date: 04/13/2020
Project: Round Robin Queue
"""

import random
import time 

TQ = int(input("Enter the time quantum: "))



class Node:

    def __init__(self, val = "",size = TQ, n = None):
        self.value = val
        self.next = n
        self.length = Node.generateProcess(size)
        self.tq = size
        
    def generateProcess(TQ):
        if random.randint(1,5) == 5:
            #Long process
            length = random.randint(TQ,TQ+20)
        else:
            #short process
            length = random.randint(1,TQ)
        return length

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, val):
        self.first = None
        self.last = None
        self.que_length = val
        
        
        
    #appends to list
    def push(self, val):

        current = self.first
        if current == None:
           self.first = Node(val)
           
        else:
            while current.next != None:
                current = current.next
            current.next = Node(val)
            
            
        
    #removes item from list
    def pop(self):
        index = 0
        prev = None
        node = self.first
        i = 0

        while ( node != None ) and ( i < index ):
            prev = node
            node = node.next
            i += 1

        if prev == None:
            self.first = node.next
        else:
            prev.next = node.next
        return node
    
   
    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'TQ:' + str(current.tq) + '[P' + str(current)+':' + str(current.length) + ']'
            current.length -= 1
            current.tq -= 1
            if current.length <= 0:
                ll.pop()
                self.que_length -= 1
            elif current.tq <= 0:
                ll.pop()
                self.que_length -= 1
            while current.next != None:
                current = current.next
                size = current.length
                out += '->[P' + str(current)+':T' + str(size) +  ']'
                
            
                
            return out
        return '[]'

length = 0
ll = LinkedList(length)

def Main():
    pID = 1
    ll.push(pID)
    ll.que_length += 1
    pID += 1
    while True:
        rnd = random.randint(1, ll.que_length)
        if rnd == 1:
            ll.push(pID)
            ll.que_length += 1
            print (str(ll))
            pID += 1
        if pID == 99:
            pID = 1
        else:
            print (str(ll))
            time.sleep(1)
    

Main()