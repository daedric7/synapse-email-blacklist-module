This little module os mostly produced by ChatGPT so... i guess you get what you pay for.

The [module file](https://github.com/daedric7/synapse-email-blacklist-module/blob/main/emailblacklist.py) must be in a dir that the python running synapse can find (if docker, you can mount the file in /usr/local/lib/python3.XX/site-packages/emailblacklist.py)

The [email_blacklist.yaml](https://github.com/daedric7/synapse-email-blacklist-module/blob/main/emailblacklist.py) must be in a dir Synapse can find (you can set it next to homeserver.yaml)

Add this little snippet in homeserver.yaml:

```
modules:
    - module: emailblacklist.EmailBlacklistModule
      config: "/data/email_blacklist.yaml"
```
