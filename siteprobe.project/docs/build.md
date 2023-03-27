Application must be build and run in Docker containers.

### Build container image for metrics collector
```bash
docker build -f keeper.Dockerfile -t keeper:1 .
```

### Build container image for site checker
```bash
docker build -f checker.Dockerfile -t checker:1 .
```