### Setup
1. Install docker
1. In the root of the repository, run `docker-compose build`.
    This step will need to be re-executed if the code changes.

### Usage
1. Run `docker-compose run --rm crawler [ARGS]` to run the crawler,
    for example `docker-compose run --rm crawler --help` to see the options available.
1. To stop the crawling send SIGINT (for example by pressing CTRL-C)
1. To use crawling results, connect to `mongodb://localhost:27018/` (database: crawler, collection: pastes)

### Cleanup
1. To turn off the DB run `docker-compose down`.
   Note that this will preserve the volume containing the results.
1. To remove the volume, run `docker-compose down --volumes`
