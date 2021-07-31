
import argparse
import os
import json
    
    
DATA_DIR = ""
TEST_DIR = ""
MODEL_DIR = ""
MEDIA_DIR = ""
INC_DIR = ""
DIRS = []


    
parser = argparse.ArgumentParser(description="Script to run to configure your environment")
parser.add_argument("--setting", "-s", type=str, help="How you'd like to configure your environment. You can choose from `build`, `clean`, and `clean-build",
                    default="clean-build", choices=["clean", "build", "clean-build"])
   
args = parser.__dict__   
     
     
        
def clean():
    with open("parameters.json", "r") as f:
        print("Loading parameters...")
        params = dict(json.load(f))
        
        DATA_DIR = params["DATA_DIR"]
        TEST_DIR = params["TEST_DIR"]
        MODEL_DIR = params["MODEL_DIR"]
        MEDIA_DIR = params["MEDIA_DIR"]
        INC_DIR = params["INC_DIR"]
        
    DIRS = [DATA_DIR, TEST_DIR, MODEL_DIR, MEDIA_DIR, INC_DIR]
    
    for dirs in DIRS:
        os.remove(dirs)
        
                 
def build(): 
    with open("parameters.json", "r") as f:
        print("Loading parameters...")
        params = dict(json.load(f))
        
        DATA_DIR = params["DATA_DIR"]
        TEST_DIR = params["TEST_DIR"]
        MODEL_DIR = params["MODEL_DIR"]
        MEDIA_DIR = params["MEDIA_DIR"]
        INC_DIR = params["INC_DIR"]
          
    DIRS = [DATA_DIR, TEST_DIR, MODEL_DIR, MEDIA_DIR, INC_DIR]
    
    for dirs in DIRS:
        os.makedirs(dirs, exist_ok=True)
  
        
def clean_build():
    takedown()
    setup()
        

if __name__ == "__main__()":
    print("Main")
    settings = args["settings"]
    print(settings)
    
    if settings == "clean":
        clean()
        
    if settings == "build":
        build()
        
    if settings == "clean-build":
        clean_build()
    
    