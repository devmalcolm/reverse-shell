![Logo](https://i.ibb.co/svH6jZk/Shape-1-1.png)

<h1 align="center">REVERSE SHELL</h1>

<div align="center">
  <strong>Lookup information software, open-source project made with Python3 - Flask</strong>
  <br>
  <br>

  <a href="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Travis" />
  </a>
  
  <a href="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white">
    <img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" alt="Documentation Status" />
  </a>

  <a href="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="Py Versions" />
  </a>

  <a href="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="PyPi" />
  </a>

  <a href="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="LICENSE" />
  </a>

  <a href="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="LICENSE" />
  </a>

</div>
<br>

Open-source project to easily find information about a specific user (Social Media Hunt) made with Python3, Flask(HTML5, CSS3)

Please use this program only on consenting people, I remind you that it is only for educational purposes and that I am not responsible for your actions

<br>



# How does it work ?
![Logo](https://i.ibb.co/MZVzZWH/Forme-2-2.png)
<br>

- How does a reverse shell work ? 

The reverse shell principle is easy to understand, here is an example. <br>

A basic shell, it is the attacker who connects to his victim using various ways

In the case of a reverse shell it is quite the opposite, the attacker sends a script / application or other containing a script which will allow to connect to the server of the attacker in case here, our local IP

The attacker has a script (In this case here it is the "**server.py**" which contains the whole backend for him to execute remote commands.

Quick explanation with an image :

![Logo](https://i.ibb.co/0Zf7H73/Forme-2-1.png)

**To summarize instead of having the attacker who connects to his victim it is the victim who connects to the attacker.**


## 🛠 Installation

![Logo](https://i.ibb.co/J59tZ8d/Shape-1-2.png)

Important, you must have the version 3.x of Python installed or higher

* Clone this repository 
```
git clone https://github.com/zaqoQLF/reverse-shell.git
```
* Install the requirements
First way : 
```
python3 setup.py
```
Second way : 
```
pip3 install -r requirements.txt
```
## 🚀 Running Program
![Logo](https://i.ibb.co/jbGbJ6N/wdqd.png)

* **SERVER SIDE :** 

Once all dependencies are installed, run the **server.py** script.

It will check for updates & check if all dependencies are correctly installed.

After that you should have a mode selection. If you want to try it locally select the first one.
It will run on your localhost IP (http://127.0.0.1:5050/).

Once the server connected, it will listen for incoming requests.

If you select the second mode (Custom mode) your will be asked to choose your IP Address and your port.
In order to be able to use this program with other computer (different IP address) you need to open your ports (Port forwarding)
Once done you can choose your IP then your port (avoid port 80 etc...)

If the connection is established, it will listening for incoming requests.


* **CLIENT SIDE :**

**IMPORTANT :** In order to connect the client to the server, the server needs to run

Before running the **client.py** script, you need to configure manually the host & ports parameters 

```python
# Change the ip here
self.HOST_IP = "IP HERE"
# Change the port here
self.PORT_SERVER = PORT HERE (INT)
# Example
# self.PORT_SERVER = 5050
```
Change the `self.HOST_IP` with your server IP Address & your `self.PORT_SERVER` with your server port number.

Once all done your can run the server.py first, then it should listening and now run the client.py script with the same port & IP as the server.
it will automatically connect to the server.


### Commands to connect (Server Side)

* **Commands before connection to the victim :**

`--connect IP` : Connect to the user (specify IP) 

`--listen` : Close current connection then listen for new incoming connections

`view -r` : View requested connection (Single client handling)

`clear` : Clear your terminal

`exit -f` : Force exit the program & end all connections

`credits` : View project credits

`--setup` : Setup the IP / port (Automatically closing all connections)

`--param --all` : View all parameters (IP, PORT)

`--param -p` : View server port


* In order to execute commands, you need to accept incoming connection : 
(In reality, the connection is already accepted, but for the future i will be multi-client handling. So to prevent this i already coded that)

```
--connect IP HERE
``` 
![Logo](https://i.ibb.co/7QPVTcK/Forme-6.png)

* If you want to view requested connection use this command :
```
    view -r
```
![Logo](https://i.ibb.co/b2sWW0J/Forme-5.png)


## Remote Commands

* **Current remote commands available :**

`disconnect` : Disconnect your from the current session (target)

`exit` :  Exit program & end all connections

`active -session` :  Display information about the active session (target)

`get_info -name` : Display victim Desktop name

`get_info -sys` : Display victim Desktop system (OS, Version...)

`down -f` : Download a file (USAGE: down -f NameOfTheFile) [ Avoid png, or jpeg, it will works but instantly crash, need to fix it in the next update]

`screenshot` : Take a screenshot of the Desktop (will be saved on the victim computer, to get it, use down -f) [ Will fix it in the next update]
`cd` : Basic command

`dir` : Basic command

`mkdir` :  Create a folder (USAGE: mkdir NameOfTheFolder)

`rmdir` : Delete a folder (USAGE: rmdir NameOfTheFolder)

`rename` : Rename a file or a folder

`start` : Open a Command prompt window (obv spotted)

`status` : Get the current user connected to you

`get_info --all` : Get all information system of your victim

* More command coming soon.






