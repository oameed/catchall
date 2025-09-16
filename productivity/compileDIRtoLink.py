#############################################
### My Productivity Scripts               ###
### Compile Directory Tree into URL Links ### 
### by: Oameed Noakoasteen                ###
#############################################

import subprocess

def get_sorted_list(LIST):
  tmp        = [x[1] for x in LIST]
  tmp_sorted = sorted(tmp, key=str.lower)
  index      = [tmp.index(x) for x in tmp_sorted]
  return [LIST[idx] for idx in index]

def get_dir_names(PATH):
  tmp = subprocess.check_output(["powershell.exe", 'Get-ChildItem -LiteralPath ' + '"' + PATH + '"' + ' -Name -Directory'], text=True)
  tmp = tmp.split('\n')
  return sorted([x for x in tmp if not x == ''], key=str.lower)

def initialize_run():
  def read_json(FILENAME):
    import json 
    with open(FILENAME, 'r') as file:
      name_dict = json.load(file)
    return name_dict
  import argparse
  parser    = argparse.ArgumentParser()
  parser.add_argument('-root', type=str, required = True)
  parser.add_argument('-dict', type=str, required = True)
  parser.add_argument('-fn'  , type=str, required = True)  
  args      = parser.parse_args()
  dir_names = get_dir_names(args.root)
  name_dict = read_json    (args.dict)
  return args.root, dir_names, name_dict, args.fn

def main():
  list_global                          = []
  root, dir_names, name_dict, filename = initialize_run()
  
  for dn in dir_names:
    prefix      = name_dict[dn]
    names       = get_dir_names(root+"\\"+dn)
    list_local  = [(prefix, name) for name in names]
    list_global = list_global + list_local
  
  list_global = get_sorted_list(list_global)
  
  with open(filename, "w") as fobj:
    for item in list_global:
      fobj.write('['+item[1]+']'+'('+item[0]+item[1]+')'+'  '+'\n')

if __name__ == "__main__":
  main()


# python compileDIRtoLink.py -root <full-path-to-the-root> -dict <full-path-to-the-json-file> -fn <name-of-the-output-file>
