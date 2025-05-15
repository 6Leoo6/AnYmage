# AnYmage
### Convert any file to a lossless PNG

You can convert any file on your system to a losslessly compressed png image. It can be useful to share it on platforms where no other file formats are supported, but media uploads are lossless. Other than that, this project doesn't really have any use cases.

---

### Example
The famous play from Shakespear - Romeo and Juliet - converted to a png looks like this:
![Romeo and Juliet as an image](samples/romeo_and_juliet.png)

---

### Usage
To convert any file to a png:

`python convert.py -i "C:/path/to/file" -o "C:/path/to/image.png"`

Use the `-r` flag to convert a png back to the original file:

`python convert.py -i "C:/path/to/image.png" -o "C:/path/to/file" -r`