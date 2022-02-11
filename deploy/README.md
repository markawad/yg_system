# Deployment

To run a deployment, make sure to create a .env file under docker directory and fill in the variables from the template.env.

## Run docker containers
Under docker directory run:
```bash
sudo docker-compose up -d 
```
If you would also like to (re)build the image while running it, you can type:
```bash
sudo docker-compose up --build -d
```
## Stop docker containers
```bash
sudo docker-compose down
```