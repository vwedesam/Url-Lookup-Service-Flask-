# URL Lookup Service
## 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

### Setup
Create project with virtual environment
```console
$ mkdir myproject
$ cd myproject
$ python3 -m venv env
```
clone git repo
```
$ git clone git@github.com:vwedesam/Url-Lookup-Service-Flask-.git
```
#### Run the app
```console
$ python app.py
```
Activate it
```console
$ . env/bin/activate
```
or on Windows
```console
env\Scripts\activate
```
## API Reference

### URL Lookup
```sh
GET /urlinfo/1/:hostname/:path
```
#### Parameters
hostname: hostname and port
path: original path and query string
#### Payload
No payload
#### Response
```js
{ message: "", safe: true }
```
### Update URL
```sh
POST /update_malwares
```
#### Parameters
no parameters
#### Payload
- arrays of url
```
['example.com', 'google.com/keep?auth=2', 'mail.yahoo.com']
```
#### Response
```
{
    status : "success", message: ""
}
```
