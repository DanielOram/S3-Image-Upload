# S3-Image-Upload
 Simple Django App that uploads images to an AWS S3 bucket using gunicorn for handling requests/responses and nginx as a webserver. Celery and redis are used to manage automated tasks and queue tasks for automated deletion of images after 24hrs. This app also uses a postgres database.
 
 This app uses docker containerization to run 6 docker containers
 - web: Container containing the django application
 - nginx: Container running the nginx image and configuration
 - redis: Container running redis server as the broker and backend for celery tasks
 - db: Container running a postgres server to handle all db queries.
 - celery: Container running the celery worker process
 - celery-beat: Container running the celery beat process for scheduled tasks



To run this application, install `Docker` and `docker-compose`. Then run `docker compose up` inside the root directory. Open `http://localhost:1337/` to see the running app.
