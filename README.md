# Page File Simulator

## What is it
This is a simple page swapping simulator that takes a page-string and a number of available pages and simulates FIFO, LRU and OPT swapping.

## How to use
Just download the python script and run as follows:
python pagesim.py #frames pagestring algorithm

## Example

python pagesim.py 3 "7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1" "FIFO"

python pagesim.py 7 "7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1" "LRU"

python pagesim.py 1 "7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1" "OPT"
