import os
import threading

def sceneRunner(scene):
    os.chdir('./Control/Scenes')
    os.system(f'python {scene}')
    
def startScene(scene):
    print("Starting scene: " + scene)
    # run the python file in scenes with the same name as the scene
    thread = threading.Thread(target=sceneRunner, args=(scene,))
    thread.start()
    thread.join()
    print("Scene finished")

def stopScene():
    print("Stopping scene")
    # kill the python process
    print("Scene stopped")
    
startScene("colorWave.py")
