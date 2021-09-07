from sys import executable
import cx_Freeze
import pygame

executables = [cx_Freeze.Executable("help.py")]


cx_Freeze.setup(
    name="Splonk",
    options={"build_exe" : {"packages" : ["pygame"], "included_files" : ["asteroid.png", "Asteroid1.png", "AsteroidSpawn.wav", "BackGround.png", "BG.png", "ded.png", "DED.wav", "Enemy.png", "RocketNT.png", "RocketOutput.png", "RocketOutput2.png", "RocketOutput2Pix.png", "RocketOutput3.png", "RocketOutput3.png", "RocketOutput3Pix.png", "RocketRotateLeft.png", "RocketRotateRight.png", "RocketThing.png", "rockettrail.png", "Star1", "TutorialRocket.png", "TutorialRocket2.png", "TutorialRocketBig.png"]}},

    executables = executables

)