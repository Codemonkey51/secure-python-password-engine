# secure python password engine docs:

### Functions:
* securePasswordInput(passwordPrompt)
  * sends the promt {passwordPromt} and hashes there answer. Returns the hashed password
* passwordCheck(password, guess)
  * checks if {password} and {guess} are the same returns true or false
* setPassword()
  * goes through password setup
* passwordEncrypt(password)
  * returns hashed version of {password}
### Constimizations:
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
