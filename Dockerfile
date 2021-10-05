# init a base image (Alpine is small Linux distro)
FROM python:3.8-alpine
# define the present working directory
WORKDIR /Flask_Blog
# copy the contents into the working dir
COPY . /Flask_Blog
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
EXPOSE 5000

# define the command to start the container
CMD ["python", "flaskblog.py","--host", "127.0.0.1", "--port", "5000"]