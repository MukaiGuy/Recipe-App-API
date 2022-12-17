# Basic Notes and Reminders

Using git

```bash
# New Dir
git init .

# New Repo
 git remote add origin git@github.com:MukaiGuy/{REPO_NAME}


# Adds new/updated files
git add .

# Commit those adds
git commit -m "Comment"

# Push the update to the repo
git push 

```



### What is GitHub Actions

GitHub Actions are equivalent to GitLab CI/DL

There is a trigger such as a push to the repo and the action can be a job such as running unit tests.

GitHub gives you 2000 minutes per month for free



### What is Docker Hub

It allows you to pull base images from docker and store your custom images

There are Rate Limits:

	- Anon users: 100 pulls/6hrs
	- Authenticated: 200 pull/6hrs



GitHub Actions uses a Shared IP address thus we should Authenticate

```bash
docker login
```

Add Secrets to the GitHub Project (They are encrypted) 



