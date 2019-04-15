![KahlaLogo](https://raw.githubusercontent.com/AiursoftWeb/Kahla.App/dev/src/assets/144x144.png)

# Kahla.CLI
Kahla for CLI. An implementation for Kahla API: [here](https://wiki.aiursoft.com/ReadDoc/Kahla/What%20is%20Kahla.md)

[![Build status](https://aiursoft.visualstudio.com/Star/_apis/build/status/Kahla%20CLI%20CI)](https://aiursoft.visualstudio.com/Star/_build/latest?definitionId=9)

## How to Use
View Help

```bash
$ kahla --help
```

Use the release version or stagging version

The default is to use the release version without setting it

```bash
$ kahla usemaster # use release version
$ kahla usestagging # use stagging version
```

Login

```bash
$ kahla login --email <username> --password <password>
```

Logout

```bash
$ kahla logout
```

View all friends

```bash
$ kahla friends
```

Search for friends

```bash
$ kahla searchfriends --searchinput <username>
```

View all groups

```bash
$ kahla groups
```

Search for groups

```bash
$ kahla searchgroups --searchinput <username>
```

Get Messages

```bash
$ kahla getmessages --username <username> --take 15
```

Send Message

```bash
$ kahla send --username <username> --message <message>
```

Delete friend

```bash
$ kahla deletefriends --username <username>
```

Leave the group chat

```bash
$ kahla leavegroups --group <groupname>
```

Listen to the message

```bash
$ kahla listen
```

## How to run
Before running, you need to install the dependencies
```bash
$ pip install -r requirement.txt
$ pip install -r devrequirement.txt
```

You can run this project by running the following shell command:
```bash
$ kahla xxxx
```

## Project Dependencies
We developed this using Python3.7 and recommend downloading the latest version of Python3.7 directly.

Windows users also need to install the Python runtime when using executables

## Project Support OS
This project supports Windows Mac Linux.

Currently, Mac and Linux only support bash scripting, and Windows supports exe executables

## Project Dependencies SDK Download Address

[Python 3.7](https://www.python.org/downloads/release/python-373/)

Other packages use the pip installation directly.
If you are a normal user, you only need to install requirement.txt. 

If you are a developer, you need to install devrequirement.txt

## How to build to exe

This command depends on all the packages that need to be installed above

```bash
./publishforwindows.sh
```

The files under the dist/Program/ directory are the compiled files

## Document

For more info please view [Kahla Wiki](https://wiki.aiursoft.com/ReadDoc/Kahla/What%20is%20Kahla.md)

## How to contribute

There are many ways to contribute to the project: logging bugs, submitting pull requests, reporting issues, and creating suggestions.

Even if you have push rights on the repository, you should create a personal fork and create feature branches there when you need them. This keeps the main repository clean and your personal workflow cruft out of sight.

We're also interested in your feedback for the future of this project. You can submit a suggestion or feature request through the issue tracker. To make this process more effective, we're asking that these include more information to help define them more clearly.
