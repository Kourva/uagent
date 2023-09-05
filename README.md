<h3 align='center'>
    <img align='left' src='https://github.com/Kourva/uagent/blob/main/ua.png' width=120>
    <h3><b>uagent</b></h3>
    <p>Uagent allows you to retrieve a random user-agent string each time it is executed. It can be used for various web scraping and testing purposes.</p>
</h3>
<br><br>

# Setup
+ **Clone repository**
```bash
git clone https://github.com/Kourva/uagent
```
+ **Navigate to source directory**
```bash
cd uagent
```
+ **Make scripts executable**
```bash
chmod +x *.py
```
+ **Install the tool**
```bash
sudo python setup.py install
```
You need **root privilege** to install this tool! so use `sudo` before command.
This tool is only compatible with **Linux**!

# Usage
+ For simple usage just type:
```bash
uagent
```
+ If you want to use this tool alongside other tools like **sqlmap**:
```bash
sqlmap -u 'https://example.com?id=1' --user-agent=$(uagent)
```

# Uninstall
```bash
sudo python setup.py uninstall
```
You need **root privilege** to uninstall this tool! so use `sudo` before command.

# Manual 
to see **Manual**:
```bash
man uagent
```

# Thank You

Thank you for checking out this repository! Your interest and support are greatly appreciated. If you find this project useful or have any feedback, please feel free to open issues or contribute.

> Happy coding!

