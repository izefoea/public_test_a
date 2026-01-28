# public_test_a

## User Identification System

This repository provides a simple user identification system that answers the question "Who are you?"

### Usage

Run the identity script:

```bash
python3 whoami.py
```

This will display:
- Your username
- Your hostname
- Your operating system
- Your home directory
- Current timestamp

### Example Output

```
Who are you?

User Identity:
  Username: runner
  Hostname: myhostname
  OS: Linux 6.11.0-1018-azure
  Home Directory: /home/runner
  Timestamp: 2026-01-28T08:25:49.148301
```

### Python API

You can also use the module programmatically:

```python
from whoami import UserIdentity

identity = UserIdentity()
info = identity.who_are_you()
print(info)  # Returns a dictionary with user information
```