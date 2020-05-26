# Web-based github API display

How to use:

1. Set up a personal access  token on GitHub, (or use an existing one) see [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) for instructions.
2. Set up an environment variable called `GITTOKEN` containing your shiney new hash.
```
export GITTOKEN=<hash you got with your PAT in step 1>
```
3. Create a new venv environment and install the dependencies
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
4. Run the app
```
flask run
```
5. Navigate your browser to the address Flask gives you.


Other useful environment variables:
- `$SEARCH_ORG`: which GitHub organization to search
- `$SEARCH_VARIABLES`: Colon separated list of github API variables to show. Full list of choices is available [here](https://developer.github.com/v3/repos/#get-a-repository).
- `$SEARCH_REPO`: string to search for in the repo.
