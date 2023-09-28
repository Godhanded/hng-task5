# hng-task5
## Simple file Uploads. Minimal
## Table Of Contents
- [Set up server for Local Machine](#set-up-the-server-local)
- [Base Uri/Live Deployment](#base-uri)
- [Error Handling](#error-handling)
- [EndPoints](#endpoints)
  - [Upload Video](#upload-video)
  - [get all user uploaded videos](#get-all-user-uploaded-videos)
  - [get a video uploaded by user](#get-a-video-uploaded-by-a-user)
- [Limitations or Assumptions](#assumptionslimitations)
- [Authors](#authors)

## **ESimple file Uploads. Minimal**
---
<br>
<br>

### **Base Uri**
----
----
Hosted for live testing on **https://upload-man.onrender.com**
....
<br>

### **Set up the server (local)**
### Clone The Repository
```bash
$ git clone https://github.com/Godhanded/hng-task5.git

$ cd hng-task5
```

### Install Dependencies
```bash
# create Virtual Environment
$ python3 -m venv venv

# Activate Virtual Env
$ source venv/bin/activate

# Install Dependencies
$ pip install -r requirements.txt
```

#### if you use pipenv

```bash
$ pip install pipenv

# create virtuel environment
$ pipenv --python 3.10

# Activate virtual env
$ pipenv shell

# install dependencies in requirements.txt or pipfile
$ pipenv install
```

### Run the Server
```bash
$ flask run
```

<br>



#### **Error Handling**
---
---
>Errors are returned as JSON objects in the following format with their error code

```json
{
  "error": "error name",
  "message": "error description"
}
```
The API will return 4 error types, with diffreent descriptions when requests fail;
- 403: Forbidden
- 404: resource not found
- 400: Bad Request
- 500: Internal server error

<br>


<br>

### **EndPoints**
---
---
<br>

#### **upload video**

  `POST '/${user_name}'`
- uploads a video of only the following file extensions
```python
 [
        ".mp4",
        ".MP4",
        ".gif",
        ".FLV",
        ".flv",
        ".avi",
        ".AVI",
        ".WebM",
        ".webm",
        ".3gp",
        ".3GP",
    ]

```
- Path Parameter: `user_name`- string user name of person to uploading
- expects a form with inpute field of type file [see sample here](index.html)
- Returns: JSON object containing message generated video_name and video_url

```json
 {
  "message": "success",
  "video_name": "test.webm",
  "video_url": "http://baseuri/test/test.webm"
}
```
*status code: 201*

---

<br>

#### **get all user uploaded videos**

  `GET '/${user_name}'`
- gets all videos uploaded by a particular username
- Path Parameter: `user_name`- string user name of person 
- Returns: JSON object containing message list of uploaded video_name and video_url if exists else []

```json
{
  "message": "success",
  "videos": [
    {
      "video_name": "test.webm",
      "video_url": "http://baseuri/test/test.webm"
    }, 
    {
        "video_name":"test2.mp4", 
        "video_url":"http://baseuri/test/test2.mp4"
    }
  ]
}
```
*status code: 200*

---

<br>

#### **get a video uploaded by a user**

  `GET '/${user_name}/${video_name}'`
- get a video uploaded by a user
- Path Parameter: `user_name`, `video_name`- string user name of person to uploading name of video uploaded
- Returns: Video. see sample query and use [here](index.html)

*status code: 302 redirect to video file*

---

<br>

## Authors
- [@Godhanded](https://github.com/Godhanded)