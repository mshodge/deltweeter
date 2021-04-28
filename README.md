# deltweeter

A simple python script (`main.py`) that uses GitHub Actions and GitHub Secrets to delete tweets, retweets and likes before a certain number of days in the past (default is `31`).

# Setup

1. Fork this repository
2. Edit main.py variable `days_to_delete_after` if you want to
2. Create your API tokens (API Secret, API Key, Access Token, and Access Token Secret) at [developer.twitter.com](developer.twitter.com)
3. Add these tokens as GitHub Secrets (settings/secrets)
4. Edit the cron time in the GitHub Action workflow if you want it to run at a different time

# Errors or Bugs

Please raise an Issue.

# Acknowledgements

Code and concept built upon [Mathew Inkson's](https://www.mathewinkson.com/2015/03/delete-old-tweets-selectively-using-python-and-tweepy)
