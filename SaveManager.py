import json
class SaveManager():
        def __init__(self):
            self.SetupFilePath = "setup.json"
            self.keybindsFilePath = "keybinds.json"
            self.rotations= "rotations.json"
            #check if both files exist if not create them
            try:
                with open(self.SetupFilePath,'r') as f:
                    self.setup = json.loads(f)
            except FileNotFoundError:
                f = open(self.SetupFilePath,'w')
                f.close()
            try:
                with open(self.keybindsFilePath,'r') as f:
                    self.keys = json.loads(f)
            except FileNotFoundError:
                f = open(self.keybindsFilePath,'w')
                f.close()
            try:
                with open(self.rotations,'r') as f:
                    self.rotation = json.loads(f)
            except FileNotFoundError:
                f = open(self.rotations,'w')
                f.close()
        def Loadkeybinds():
            with open(self.keybindsFilePath,'r') as f:
                self.keys = json.loads(f)
            return self.keys
        def Savekeybinds(keys):
            with open(self.keybindsFilePath,'w') as f:
                f = json.dumps(keys)
        def LoadSetup():
            with open(self.SetupFilePath,'r') as f:
                self.setup = json.loads(f)
            return self.keys
        def SaveSetup(Setup):
            with open(self.keybindsFilePath,'w') as f:
                f = json.dumps(setup)
                        
