### Millo's Script Library
from tkinter import *
import pygame

class array:

    @staticmethod
    def listMedian(list):
        # This finds the median value of the list
        print("The original list is: " + str(list))
        list.sort()
        med = len(list) // 2
        res = (list[med] + list[~med]) / 2
        print("Median of the list is: " + str(res))
        return res

    @staticmethod
    def binarySearch(list, item):
        first = 0
        last = len(list) - 1
        found = False
        while first <= last and not found:
            mid = (first + last) // 2
            if list[mid] == item:
                found = True
            else:
                if item < list[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        if found == True:
            print("Item " + str(item) + " found at element " + str(list[mid]))
        else:
            print("Item " + str(item) + "not found in list")
        return list[mid]

    @staticmethod
    def linearSearch(list, item):
        for i in range(len(list)):
            if list[i] == item:
                found = True
                break
            else:
                found = False
        if found == True:
            print("Item " + str(item) + " found at element " + str(list[i]))
        else:
            print("Item " + str(item) + "not found in list")
        return list[i]

    @staticmethod
    def bubbleSort(list):
        n = len(list)

        for i in range(n):
            for j in range(0, n-i-1):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
        print("Sorted list is: ")
        for i in range(len(list)):
            print("%d" %list[i])
        return list[i]

    @staticmethod
    def insertionSort(list):
        for i in range(1, len(list)):
            key = list[i]
            j = i-1
            while j >= 0 and key < list[j]:
                list[j+1] = list[j]
                j -= 1
            list[j+1] = key
        print("Sorted list is: ")
        for i in range(len(list)):
            print("%d" %list[i])
        return list[i]

    @staticmethod
    def mergeSort(list):
        
        print("Splitting ", list)

        if len(list) > 1:
            mid = len(list)//2
            lefthalf = list[:mid]
            righthalf = list[mid:]

            array.mergeSort(lefthalf)
            array.mergeSort(righthalf)

            i, j, k = 0, 0, 0

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    list[k] = lefthalf[i]
                    i = i + 1
                else:
                    list[k] = righthalf[j]
                    j=j+1
                k = k + 1
            while i < len(lefthalf):
                list[k] = lefthalf[i]
                i = i+1
                k = k+1

            while j < len(righthalf):
                list[k] = righthalf[j]
                j = j+1
                k=k+1

            print("Merging ", list)
        print("Final sorted list: " + str(list))
        return list
        

class tkinterhelper:

    @staticmethod
    def createWindow(title, width, height):
        window = Tk()
        window.title(title)
        print("Window " + title + " created with size of " + str(width) + " x " + str(height))
        window.geometry(str(width)+'x'+str(height))
        window.mainloop()

class pygamehelper:

    @staticmethod
    def createWindow(title, width, height, r, g, b):
        pygame.init()
        display = pygame.display.set_mode((width, height))
        fillColour = (r, g, b)
        display.fill(fillColour)
        pygame.display.update()