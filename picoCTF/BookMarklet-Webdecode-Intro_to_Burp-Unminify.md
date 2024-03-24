IntroToBurp |  | 100 points

![image](https://github.com/msthione/ctfs/assets/99500478/aa436af6-6314-477a-8e56-18af0c95b749)

We have a registration form, let's fill it and sent

![image](https://github.com/msthione/ctfs/assets/99500478/3cb2dae7-f0be-4b65-9d36-d501306b3139)

Based on the name of the challenge, I started examining it directly with Burp.

![image](https://github.com/msthione/ctfs/assets/99500478/c81d8c9e-8683-46dd-9797-6c408a6cccf6)

and followed page

![image](https://github.com/msthione/ctfs/assets/99500478/edb9c878-5f90-4ff2-aa87-88bd79a6a4d6)

let's check the OTP

![image](https://github.com/msthione/ctfs/assets/99500478/79b2c5fa-557b-4924-8a47-df5ebe2bcfb2)

At this point, I tried many things, but eventually I decided that I needed to think differently and tried again by changing "otp" to "flag" and the result:

![image](https://github.com/msthione/ctfs/assets/99500478/f668f900-5261-4212-bb91-dc384e0cfb9e)


--------------------------------------------------------------------------------------------------------------------------

Unminify |  | 100 points

![image](https://github.com/msthione/ctfs/assets/99500478/2864b038-283d-4a2c-8f49-26ddc3b9cc09)


When I visit the website I got a simple page

![image](https://github.com/msthione/ctfs/assets/99500478/fdee86bf-ed9e-43e3-b4ed-71cbaa24ea8e)

I viewed the page source

<code>Page-source</code>
```
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>picoCTF - picoGym | Unminify Challenge</title><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png"><style>body{font-family:"Lucida Console",Monaco,monospace}h1,p{color:#000}</style></head><body class="picoctf{}" style="margin:0"><div class="picoctf{}" style="margin:0;padding:0;background-color:#757575;display:auto;height:40%"><a class="picoctf{}" href="/"><img src="picoctf-logo-horizontal-white.svg" alt="picoCTF logo" style="display:inline-block;width:160px;height:90px;padding-left:30px"></a></div><center><br class="picoctf{}"><br class="picoctf{}"><div class="picoctf{}" style="padding-top:30px;border-radius:3%;box-shadow:0 5px 10px #0000004d;width:50%;align-self:center"><img class="picoctf{}" src="hero.svg" alt="flag art" style="width:150px;height:150px"><div class="picoctf{}" style="width:85%"><h2 class="picoctf{}">Welcome to my flag distribution website!</h2><div class="picoctf{}" style="width:70%"><p class="picoctf{}">If you're reading this, your browser has succesfully received the flag.</p><p class="picoCTF{Challenge_Flag}"></p><p class="picoctf{}">I just deliver flags, I don't know how to read them...</p></div></div><br class="picoctf{}"></div></center></body></html>
```
when i read the code I found the flag but 
Let's make it more funny. :)
Since I knew where the flag was, I tried just printing the flag by pipetting the "curl" command with "grep" 

```
$ curl http://titan.picoctf.net:63873/ | grep -Eo "picoCTF{.*}"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1352  100  1352    0     0   5445      0 --:--:-- --:--:-- --:--:--  5473
picoCTF{Challenge_Flag}"></p><p class="picoctf{}">I just deliver flags, I don't know how to read them...</p></div></div><br class="picoctf{}
```

Let's print it more clean

```
$ curl -s  http://titan.picoctf.net:63873/ | grep -Eo "picoCTF{.*}" | cut -d'"' -f1
picoCTF{Challenge_Flag}
```

Thanks a lot
