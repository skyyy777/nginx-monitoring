# nginx-monitoring
A simple flask app that displays stats from your nginx servers stub_status page.
## Currently shown stats
- [x] Requests/s
- [ ] Connections
- [ ] Reading
- [ ] Waiting
- [ ] Writing
## How it works
For this tool to work, you need to enable the stub_status page of
your nginx server. To do so, add following lines to your nginx
server config, usually located at /etc/nginx/nginx.conf
```
location = /basic_status {
    stub_status;
}
```
If you visit this location in your browser, you will see an output
somewhat like that:
```
Active connections: 291
server accepts handled requests
 16630948 16630948 31070465
Reading: 6 Writing: 179 Waiting: 106
```
This tool takes the data from this page and puts it into **nice
looking charts.**
![chart](./assets/nginx-monitoring.png)
## Setup
Make sure you have docker installed and configured correctly
1. Build the container by running ```docker build . -t nginx-monitoring```
2. Run the container using
```docker run -p 5000:5000 --env STATUS_URL=https://example.com/basic_status nginx-monitoring```
and feel free to edit parameters so they fit your needs.
3. Now you can access nginx-monitoring at 127.0.0.1:5000

Make sure to replace _https://example.com/basic_status_ with your stub_status url.
