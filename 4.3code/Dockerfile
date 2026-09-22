FROM python:3.11-slim
#prevents python from creating .pyc cachce files 
ENV PYTHONDONTWRITEBYTECODE=1 
#sends python output to container logs 
ENV PYTHONUNBUFFERED=1
#set the working directors inside the container 
WORKDIR /app
# copy requirements before running anything 
COPY requirements.txt .
#install app dependecies without retaining pip cache
RUN pip install --no-cache-dir -r requirements.txt
#copy the flask application into the container
COPY app.py .
#document that the application listens on port5000
EXPOSE 5000
#create and run app as non-root user
RUN useradd --create-home appuser
USER appuser
#gunicorn starts the flask app, 
#app:app loads the object named app from app.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]