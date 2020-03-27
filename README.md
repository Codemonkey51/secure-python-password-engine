# secure python password engine docs:
### About:
* password.py is made for python 3.6
* password.py was made origianlly on [repl.it](https://repl.it) by [@codemonkey51](https://repl.it/@codemonkey51/Password-engine), it was made to help secure projects with login info
* password.py is not an official package and can only be downloaded here
* you are not alowed to redistribute password.py without credit
* support discord server [here](https://discord.gg/NQ7fC63)
* example project [here](https://repl.it/@codemonkey51/Password-engine-example)

### Disclaimer:
**We are not liable for any security breaches if you choose to use this module**

### Functions:
* securePasswordInput(passwordPrompt)
  * sends the promt {passwordPromt} and hashes there answer. Returns the hashed password
* passwordCheck(password, guess)
  * checks if {password} and {guess} are the same returns true or false
* setPassword()
  * goes through password setup
* passwordEncrypt(password)
  * returns hashed version of {password}
### Customizations:
* Change hash type:
  * goto your module foler open password.py and find this code:
  ```python 
    def passwordEncrypt(password):
       return(hashlib.sha256(password.encode()).hexdigest())
  ```
  * then replace sha256 with a hash from the list below
  * the supported hash types are: 
    * sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), and blake2s()
  * supported by most platforms but not all:
    * sha3_224(), sha3_256(), sha3_384(), sha3_512(), shake_128(), shake_256()
  * if you can we recomend switching to sha3_256()

