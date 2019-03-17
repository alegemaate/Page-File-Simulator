import sys

def page_sim(frames, pagestring, algo):
    # Validate algorithm requested
    valid_algos = ["FIFO", "LRU", "OPT"]
    if algo not in valid_algos:
        print ("Sorry, you must enter algorithm as being FIFO, OPT or LRU")
        return
    else:
        print ("Beginning " + algo + " simulation on " + pagestring + " with " + str(frames) + " frames.")
        print ("============")
        
    # Separate pages
    pages = [int(x.strip()) for x in pagestring.split(',')]

    # Create tables
    table_contents  = [-1] * frames
    table_last_used = [-1] * frames

    swaps = 0

    for i in range (0, len(pages)):
        print ("Page requested:" + str(pages[i]))
        
        # Hit
        if pages[i] in table_contents:
            print ("  Hit!")
            index = table_contents.index(pages[i])
            
            # LRU this counts as 'new'
            if algo == "LRU":
                table_last_used[index] = i
            
        # Miss
        else:
            print ("  Miss!")
            
            index = -1
            
            # FIFO, Replace most recently used
            if algo == "FIFO":
                index = table_last_used.index(min(table_last_used))

            # LRU, Replace least recently used
            elif algo == "LRU":
                index = table_last_used.index(min(table_last_used))

            # OPT find index not used for longest amount of time
            elif algo == "OPT":
                index = -1
                distances = [-1] * frames

                # Calculate next occurence from i
                temp_pages = pages[i:len(pages)]
                for t in range(0, frames):
                    if table_contents[t] in temp_pages:
                        distances[t] = temp_pages.index(table_contents[t])
                    else:
                        distances[t] = len(temp_pages)

                # Replace one with max index
                index = distances.index(max(distances))

            table_last_used[index] = i  
            table_contents[index] = pages[i]
            swaps += 1

        # Output table
        print ("  Pages are:")

        for i in range(0, frames):
            print ("    Page " + str(i) + " contains " + str(table_contents[i]) + " : last used " + str(table_last_used[i]))

    print ("============")
    print ("There were " + str(swaps) + " page faults")
    print ("============ \n \n")

# Entry point
def main():
  if len(sys.argv) != 4:
    print ("Must provide 3 arguments, number of frames available, a page string and the algorithm.\n  (For example pagesim.py 3 \"7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1\" \"FIFO\")")
  else:
    page_sim(int(sys.argv[1]), sys.argv[2], sys.argv[3])

main()

# Simulate FIFO
#page_sim(3, "7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1", "FIFO")

# Simulate LRU
#page_sim(3, "7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1", "LRU")

# Simulate OPT
#page_sim(3, "7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1", "OPT")
