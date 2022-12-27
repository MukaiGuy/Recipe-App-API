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



### What is Test Driven Development

Its where you write your tests first, knowing it will fail the writing the code that will make it pass.

 



unittest.mock allows you to mock an object

- MagicMock/Mick - replace real objects
-  



Testing API, 

Make actual API calls

Import APIClient from rest_framework

Check results

Override Authentication



```py
from django.test import SimpleTestCase
from rest_framework.test import APIClient

class TestViews(SimpleTestCase):
    
    def test_get_greetings(self):
        """ Test getting greeting"""
        client = APIClient()
        res = client.get('/greeting/')
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
        	res.data,
            ["Hello!", "Hola!"]
        )
```



## DB Adapter for Django

Psycopg2



### Race Problem



### Adding our first Unit test

```python
"""Test custom Django management commands
    """

from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    """Test Command"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db ready"""

        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=["default"])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db when OperationalError"""

        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=["default"])

```





### Working With Auto Generated API Docs

DjangoREST Framework (drf)

Library

drf-spectacular 



#### OpenAPI Schema - Swagger



## What is a view

- Handles a request made to a URL
- Django uses functions
- DRF Uses Classes
  - Reusable Logic
  - Override Behavior
- DRF also supports decorators `@Example`
- APIView and Viewsets are DRF base classes

### APIView

- Focused around HTTP Methods
- Class methods for HTTP methods
  - GET, POST, PUT, PATCH, DELTE
- Provide flexibility over URLs and Logic
- Useful for non-CRUD APIs
  - Create, Read, Update, Delete APIs
  - Bespoke logic (Auth, jobs, external apis)

### Viewsets

- Focused around actions
  - Retrieve, list, update, partial update, destroy
- Map to Django Models
- User Routers to generate URLs
- Great for CRUD operations on models