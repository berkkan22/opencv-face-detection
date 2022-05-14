# OpenCV
In diesem "Test-Projekt" habe ich ein wenig mit der [OpenCV](https://opencv.org) Libary rum gespielt. <br>
Im Folgenden wird erklärt, wie man die benötigten packeges installiert und einrichtet.
Bevor mit der Installation begonnen wird sollte das [git Repository](https://github.com/berkkan22/opencv-face-detection) geklont oder runtergeladen werden.

---

## Requirements
Die letzten beiden packeges werden im Abschnitt [Installtion](#installation) installiert. <br>
Auf meinem System läuft es mit:
- python &emsp;&emsp;&emsp;&emsp; 3.9.12 (andere Versionen sollten auch gehen)
- numpy &emsp;&emsp;&emsp;&emsp; 1.22.3
- opencv-python &ensp; 4.5.5.64

## Installation
Um die packeges zu installieren und konflikte mit lokalen packeges zu verhindern ist es am bessten eine virtuelle Umgebung einzurichten. Bevor mit den Schritten weiter gemacht wird sollte sichergestellt sein, dass das [git Repository](https://github.com/berkkan22/opencv-face-detection) herruntergeladen ist und der Terminal sollte in dem Root Path befinden. <br>
Nun gebe dafür Folgende Kommands nach einander ein um die virtuelle Umgebung zu erstellen und die packeges zu installieren:
1. `python -m venv ./venv`
2. `python -m pip install -r requirements.txt`


## Ausführung
Bevor man die Scripts ausführen kann muss man die virtuelle Umgebung aktivieren. Die Kommands für [Windows Terminal (CMD)](#windows) und [Linux shell (z.B. bash)](#linux) sind unterschiedlich. Dafür in die entsprechende Abschnitte gucken.

### Windows
Mit `call ./venv/Scripts/activate.bat` wird die virtuelle Umgebung Aktiviert. <br>
Zum deaktivieren `deactivate.bat` eingeben.

### Linux
Mit `source ./venv/Scripts/activate` wird die virtuelle Umgebung Aktiviert. <br>
Zum deaktivieren `deactivate.bat` eingeben.

---
<br>

**Fertig** nun können die einzelen Scripts mit `python <filename>` ausgeführt werden. <br> 
Viel Spaß