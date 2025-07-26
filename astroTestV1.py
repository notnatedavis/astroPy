# --- astroTestV1.py --- #
# (purpose & execution of file)

# internal notes :

# --- Imports --- #
# example imports , update later
import os
import re
from PIL import Image

# Hardcoded variables
# var here

# --- Helper Functions --- #

def natural_sort_key(s) :
    # function for natural sorting of anything file related (v/ useful)
    # ex. ['a10', 'a2'] -> ['a2', 'a10']
    return [int(part) if part.isdigit() else part.lower() 
            for part in re.split('([0-9]+)', s)]

# --- Main Entry Point --- #

if __name__ == "__main__" :

    # --- 1. Step 1 --- #

    # (purpose & intention + execution
    # execution call here
    
    if not #executioncall :
        print("ERROR#STEP1")
        exit()
  
    try :
      #functioncall
        
    except ValueError :
        print("TRYFIRSTCALL")
        exit()

    # --- N. Step N --- #
    
    # (purpose & intention + execution
    # execution call here
    
    if not #executioncall :
        print("ERROR#STEP1")
        exit()
  
    try :
      #functioncall
        
    except ValueError :
        print("TRYNCALL")
        exit()


    # --- Final Step. Step X --- #
      
      # (purpose & intention + execution
      # execution call here
      
      if not #executioncall :
          print("ERROR#STEP1")
          exit()
    
      try :
        #functioncall
          
      except ValueError :
          print("TRYFINALCALL")
          exit()
