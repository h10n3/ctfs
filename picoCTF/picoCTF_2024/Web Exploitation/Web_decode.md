WebDecode |  | 50 points

![image](https://github.com/msthione/ctfs/assets/99500478/5a651fb4-0514-489f-a377-18533c40a630)

We have a simple website:

![image](https://github.com/msthione/ctfs/assets/99500478/6f867bb9-b011-4224-97b3-5a16d4916831)

I read the page source and saw that we have just three pages to navigate.

![image](https://github.com/msthione/ctfs/assets/99500478/bb6bdd55-5420-44f4-a3d0-06900375681e)

<code>contact.html</code> has same comment: 
```
Keep searching page.
Don't give up!!!
```

But in <code>about.html</code> we have this:

![image](https://github.com/msthione/ctfs/assets/99500478/948965e2-57ea-4b08-bcdc-d71bc5f63159)

and in source code:

![image](https://github.com/msthione/ctfs/assets/99500478/e81e57b6-923a-400e-8637-fff8af569309)

Because I'm a lazy person :) I tried to decode it with "curl" command:

```
$ curl -s http://titan.picoctf.net:53646/about.html | grep "notify_true" | cut -d '"' -f4 | base64 -d
picoCTF{Challenge_Flag}
```
