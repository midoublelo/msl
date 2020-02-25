# Millo's Script Library

## Introduction
My name is Millo and this is a library filled with various algorithms that I use frequently.

## Usage
Download the `msl.py` file and place it in your workspace. Import it using `import msl` or use from imports to import a specific featureset. For example, if you only want to use array functions use this: `from msl import array`.

All functions can be called in the following way.
`msl.<category>.<function>(function args)`
Here is an example of the merge sort function:
```
import msl

sample = [2, 52, 156, 2948, 223, 5, -22]
msl.array.mergeSort(sample)
```
This file returns:
```
Splitting  [2, 52, 156, 2948, 223, 5, -22]
Splitting  [2, 52, 156]
Splitting  [2]
Final sorted list: [2]
Splitting  [52, 156]
Splitting  [52]
Final sorted list: [52]
Splitting  [156]
Final sorted list: [156]
Merging  [52, 156]
Final sorted list: [52, 156]
Merging  [2, 52, 156]
Final sorted list: [2, 52, 156]
Splitting  [2948, 223, 5, -22]
Splitting  [2948, 223]
Splitting  [2948]
Final sorted list: [2948]
Splitting  [223]
Final sorted list: [223]
Merging  [223, 2948]
Final sorted list: [223, 2948]
Splitting  [5, -22]
Splitting  [5]
Final sorted list: [5]
Splitting  [-22]
Final sorted list: [-22]
Merging  [-22, 5]
Final sorted list: [-22, 5]
Merging  [-22, 5, 223, 2948]
Final sorted list: [-22, 5, 223, 2948]
Merging  [-22, 2, 5, 52, 156, 223, 2948]
Final sorted list: [-22, 2, 5, 52, 156, 223, 2948]
```
## Feature List

