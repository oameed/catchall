###################################
### My Productivity Scripts     ###
### Filter Items from Playlist  ### 
### by: Oameed Noakoasteen      ###
###################################

import os

def rFILE(filename):
    content = []
    with open(filename, "r") as fobj:
      for line in fobj:
        content.append(line.strip())
    return content

def initialize_run():
    import argparse
    parser    = argparse.ArgumentParser()
    parser.add_argument('-n', type = str, required = True)
    args      = parser.parse_args()
    filenames = ['files' + '/' + x for x in os.listdir('files')]
    items     = []
    for filename in filenames:
      items += rFILE(filename)
    filename  = args.n 
    stem      = filename.split('.')[0]
    extension = filename.split('.')[1]
    return items, [stem,extension]

def main():
    items, filename = initialize_run()
    
    playlist        = rFILE(filename[0] + '.' + filename[1])
    playlist        = [x for x in playlist if not x in items]
    
    with open(filename[0] + '-filtered' + '.' + filename[1], "w") as fobj:
      fobj.write("\n".join(playlist))
    
    
if __name__ == "__main__":
  main()


# python MediaListFilter.py -n <filename>
