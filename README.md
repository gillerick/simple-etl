## Simple ETL

A simple ETL pipeline

### Database Installation

The ETL uses PostgreSQL as the database server. Below are the instructions for setting it up on a local machine using
Docker.

1. Get the official [PostgreSQL](https://hub.docker.com/_/postgres) Docker image

```bash 
$ docker pull postgres
```

2. Create a container from the image with the following credentials

```bash 
$ docker create \
--name movies_db \
-e POSTGRES_USER=user \
-e POSTGRES_PASSWORD=pass \
-p 5432:5432 \
postgres
```

3. Run the following command to start the container
```bash 
$ docker start movies_db
```

### Database schema

```postgresql
CREATE TABLE `movies` (
  `id` SERIAL PRIMARY KEY,
  `name` varchar,
  `description` varchar,
  `category` varchar
);

CREATE TABLE `users` (
  `id` SERIAL PRIMARY KEY,
  `movie_id` int,
  `rating` varchar
);

ALTER TABLE `movies` ADD FOREIGN KEY (`id`) REFERENCES `users` (`movie_id`);

```

