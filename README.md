<h3 align='center'>
    <img align='left' src='https://github.com/Kourva/uagent/blob/main/ua.png' width=120>
    <h3><b>uagent</b></h3>
    <p>Uagent allows you to retrieve a random user-agent string each time it is executed. It can be used for various web scraping and testing purposes.</p>
</h3>
<div style="display: flex; justify-content: space-between;">
    <img src="https://img.shields.io/github/directory-file-count/Kourva/uagent?logoColor=white&logo=Files&style=plastic&labelColor=black">
    <img src="https://img.shields.io/github/languages/count/Kourva/uagent?logoColor=yellow&logo=Python&style=plastic&labelColor=black">
    <img src="https://img.shields.io/github/issues/Kourva/uagent?logoColor=red&logo=openbugbounty&style=plastic&labelColor=black">
    <img src="https://img.shields.io/github/license/Kourva/uagent?logoColor=green&logo=lospec&style=plastic&labelColor=black&color=pink">
    <img src="https://img.shields.io/github/languages/code-size/Kourva/uagent?logoColor=blue&logo=databricks&style=plastic&labelColor=black">
    <img src="https://img.shields.io/github/watchers/Kourva/uagent?logoColor=pink&logo=freepik&style=plastic&labelColor=black">
</div>
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

<br>

# Usage
+ For simple usage just type:
```bash
uagent
```
> Example result: `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0`
+ If you want to use this tool alongside other tools like **sqlmap**:
```bash
sqlmap -u 'https://example.com?id=1' --user-agent=$(uagent)
```

<br>

# Uninstall
```bash
sudo python setup.py uninstall
```
You need **root privilege** to uninstall this tool! so use `sudo` before command.

<br>

# Manual 
to see **Manual**:
```bash
man uagent
```

<br>

# Thank You

Thank you for checking out this repository! Your interest and support are greatly appreciated. If you find this project useful or have any feedback, please feel free to open issues or contribute.

> Happy coding!

