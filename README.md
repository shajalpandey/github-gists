### Exercise
If you have any questions on the below exercise, please do get in touch and we’ll answer as soon as possible.

#### Build an API, test it, and package it into a container
- Build a simple HTTP web server API in any general-purpose programming language[^1] that interacts with the GitHub API and responds to requests on `/<USER>` with a list of the user’s publicly available Gists[^2].
- Create an automated test to validate that your web server API works. An example user to use as test data is `octocat`.
- Package the web server API into a docker container that listens for requests on port `8080`. You do not need to publish the resulting container image in any container registry, but we are expecting the Dockerfile in the submission.
- The solution may optionally provide other functionality (e.g. pagination, caching) but the above **must** be implemented.

Best of luck,  
Equal Experts
__________________________________________
[^1]: For example Go, Python or Ruby but not Bash or Powershell.  
[^2]: https://docs.github.com/en/rest/gists/gists?apiVersion=2022-11-28


# GitHub Gists Flask API

A simple Flask application that fetches public GitHub Gists for a given username and exposes them via an API endpoint. Includes pytest-based tests to validate success and error cases.

---

## 🚀 Steps to Implement

### 1. Build the Docker Image
```bash
docker build -t github-gists:v1 .
```

### 2. Run the Flask API Container
```bash
docker run -d -p 8080:8080 --name flask-gists-api github-gists:v1
```

### 3. Run Tests with Pytest
```bash
docker run --rm github-gists:v1 pytest -vs
```