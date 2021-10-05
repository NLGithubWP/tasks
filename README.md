# CS5424

project

To use dbinit-workload-A.sql

firstly run a cockroachDB cluster

And then, run python file http sever.

```bash
  python -m http.server 3000

```

Start clusters

```

cockroach start \
        --certs-dir=certs \
        --store=node1 \
        --listen-addr=localhost:26257 \
        --http-addr=localhost:8080 \
        --join=localhost:26257,localhost:26258,localhost:26259 \
        --background

cockroach start \
        --certs-dir=certs \
        --store=node2 \
        --listen-addr=localhost:26258 \
        --http-addr=localhost:8081 \
        --join=localhost:26257,localhost:26258,localhost:26259 \
        --background

cockroach start \
        --certs-dir=certs \
        --store=node3 \
        --listen-addr=localhost:26259 \
        --http-addr=localhost:8082 \
        --join=localhost:26257,localhost:26258,localhost:26259 \
        --background

```

And then, can run dbinit-workload-A.sql to load tables, 


```bash

cockroach sql \
    --host=localhost:26258 \
    --certs-dir=certs \
    --user=root \
    -f ./sqls/dbinit-workload-A.sql

```
