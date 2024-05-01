No Sql Injection |  | 200 points

![image](https://github.com/msthione/ctfs/assets/99500478/d0013efa-1b72-40fe-a928-b43b11703046)

We have a login page, and when I look at the source I see in <code>app/utils/database.ts</code>:

```
import mongoose, { ConnectOptions } from "mongoose";
```

When we tried the payloads on the hacktricks (<url>https://book.hacktricks.xyz/pentesting-web/nosql-injection</url>)

I used <code>{"username": {"$gt":""}, "password": {"$gt":""}}</code> as payload and sent <code>{"$gt":""}</code> as email and password

![image](https://github.com/msthione/ctfs/assets/99500478/b8caf37a-9ec9-47f9-aca6-28b9ab9d5f13)

and I can <code>/admin</code> page but there is no clue about flag. after that i checked the <code>HTTPhistory</code> in Burp.

while checking de responses after logging in:

![image](https://github.com/msthione/ctfs/assets/99500478/c61759c4-6bc4-4fcc-996c-5c0168543a30)

I found an encoded token and when I decode it:

```
$ echo "cGljb0NURntqQmhEMnk3WG9OelB2XzFZeFM5RXc1cUwwdUk2cGFzcWxfaW5qZWN0aW9uXzVlMjQ1ZDZlfQ==" | base64 -d
picoCTF{Challenge_Flag}
```
