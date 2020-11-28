//defined the string.
let string = "Kushagra Singh Bisen is an M1 student in CPS2."
//encode
let encodedString = (Buffer.from(string).toString('base64'));
console.log(encodedString)
console.log("--------LINE-BREAK-------")
//decode
let decodedString = Buffer.from(encodedString, 'base64').toString()
console.log(decodedString)

/* 
The output of the code when you try to run this.


S3VzaGFncmEgU2luZ2ggQmlzZW4gaXMgYW4gTTEgc3R1ZGVudCBpbiBDUFMyLg==
--------LINE-BREAK-------
Kushagra Singh Bisen is an M1 student in CPS2.

*/