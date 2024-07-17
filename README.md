# Fibonacci Service

![CI](https://github.com/holms/api-fibonacci/actions/workflows/docker-image.yml/badge.svg)


This repository contains a simple web service that calculates the nth Fibonacci number. The service is implemented using Python and CherryPy, and it is containerized using Docker. This document provides instructions on how to build, test, deploy, and scale the service.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running Locally](#running-locally)
  - [Running Tests](#running-tests)
- [CI/CD](#cicd)
  - [GitHub Actions](#github-actions)
- [Deployment](#deployment)
  - [Using Helm](#using-helm)
- [Monitoring and Logging](#monitoring-and-logging)
- [Scaling](#scaling)

## Features

- Calculate the nth Fibonacci number.
- Containerized using Docker.
- Automated CI/CD pipeline using GitHub Actions.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker
- Docker Compose

### Running Locally

1. Run the service:

    ```sh
    make run
    ```

2. Access the service at `http://localhost:8080`.

### Running Tests

Run the tests:

```sh
make test
```

## CI/CD

### GitHub Actions

This repository uses GitHub Actions for Continuous Integration (CI) and Continuous Deployment (CD). The workflow file is located at `.github/workflows/docker-image.yml`.

- The workflow:
  - Builds and tests the Docker image.
  - Pushes the Docker image to GitHub Container Registry.

## Deployment

### Using Helm

To deploy the Fibonacci service using Helm:

1. **Add Helm Repository**:

    ```sh
    helm repo add api-fibonacci https://holms.github.io/api-fibonacci/charts/
    ```

2. **Install the Chart**:

    ```sh
    helm install my-fibonacci-release api-fibonacci/fibonacci
    ```

3. **Upgrade the Chart**:

    ```sh
    helm upgrade my-fibonacci-release api-fibonacci/fibonacci
    ```

4. **Uninstall the Chart**:

    ```sh
    helm uninstall my-fibonacci-release
    ```

5. **Check the Deployment**:

    ```sh
    kubectl get deployments
    kubectl get services
    ```

## Monitoring and Logging

To monitor and log the service:

- **Monitoring**:
  - Use Prometheus and Grafana to monitor the service's health and performance.
  - Set up alerts for critical metrics (e.g., response time, error rates).

- **Logging**:
  - Use a centralized logging system like ELK Stack (Elasticsearch, Logstash, Kibana) to aggregate and analyze logs.
  - Ensure logs include detailed information about incoming requests and errors.

## Scaling

To scale the service:

1. **Increase Replicas**:
   - Use the `replicaCount` value in the `values.yaml` file of the Helm chart to increase the number of replicas.
