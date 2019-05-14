# PyAuto

Repo to automate basic sanity flow

PyAuto is build on pytest.


---
## Requriments:
* Firefox   - 65.0 (64-bit)
* Chrome    - 
* Python    - 3.4.3

---
## Installation
1. Clone the repo
```sh
  $ git clone https://github.com/sureshpathipati/pyauto.git
```
2. Install virtualenv
```sh
  $ pip3 install virtualenv
```
3. Create virtual env
 ```sh
  $ virtualenv <env_name>
    ex: virtualenv pyauto
```
4. Open the virtual env(For winodows omit source)
```sh
  $ source <folder_name>/bin/activate
    ex: source pyauto/bin/activate
```
5. Install dependencies using requirements file
```sh
  $ pip3 install -r requirements.txt
```
6. To Deactivate the virtual env use "deactivate" command
```sh
  $ deactivate
```
---

# Steps to uninstall virtualEnvironment
1. Remove packages
```sh
  $ pip uninstall -r requirements.txt -y
```
2. Come out off virtual env
```sh
  $ deactivate
```
3. Remove the environment folder
```sh   
  $ rm -r pyauto/
```

## How to run a test suite file
1.use the following command
```sh
  $ pytest <file_name> --html=report.html
    ex: pytest login_test.py --html=report.html
```
