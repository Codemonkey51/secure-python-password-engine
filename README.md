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
  * the supported hash types are: 
    * sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), and blake2s()
