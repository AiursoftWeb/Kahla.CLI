![KahlaLogo](https://raw.githubusercontent.com/AiursoftWeb/Kahla.App/dev/src/assets/144x144.png)

# Kahla.CLI
Kahla for CLI. An implementation for Kahla API: [here](https://wiki.aiursoft.com/ReadDoc/Kahla/What%20is%20Kahla.md)

## How to Use
View Help

```bash
# Windows
> kahla --help
# Linux
$ ./kahla --help
```

Use the release version or stagging version

The default is to use the release version without setting it

```bash
# Windows
> kahla usemaster # use release version
> kahla usestagging # use stagging version
# Linux
$ ./kahla usemaster # use release version
$ ./kahla usestagging # use stagging version
```

Login

```bash
# Windows
> kahla login --username <username> --password <password>
# Linux
$ ./kahla login --username <username> --password <password>
```

Logout

```bash
# Windows
> kahla logout
# Linux
$ ./kahla logout
```

View all friends

```bash
# Windows
> kahla friends
# Linux
$ ./kahla friends
```

Search for friends

```bash
# Windows
> kahla searchfriends --searchinput <username>
# Linux
$ ./kahla searchfriends --searchinput <username>
```

View all groups

```bash
# Windows
> kahla groups
# Linux
$ ./kahla groups
```

Search for groups

```bash
# Windows
> kahla searchgroups --searchinput <username>
# Linux
$ ./kahla searchgroups --searchinput <username>
```

Get Messages

```bash
# Windows
> kahla getmessages --username <username> --take 15
# Linux
$ ./kahla getmessages --username <username> --take 15
```

Send Message

```bash
# Windows
> kahla send --username <username> --message <message>
# Linux
$ ./kahla send --username <username> --message <message>
```

Delete friend

```bash
# Windows
> kahla deletefriends --username <username>
# Linux
$ ./kahla deletefriends --username <username>
```

Leave the group chat

```bash
# Windows
> kahla leavegroups --group <groupname>
# Linux
$ ./kahla leavegroups --group <groupname>
```

Listen to the message

```bash
# Windows
> kahla listen
# Linux
$ ./kahla listen
```

## How to run
Before running, you need to install the dependencies
```bash
# Windows
> pip install -r requirement.txt
# Linux
$ pip install -r ./requirement.txt
```

You can run this project by running the following shell command:
```bash
# Windows
> kahla xxxx
# Linux
$ ./kahla xxxx
```

## Document

For more info please view [Kahla Wiki](https://wiki.aiursoft.com/ReadDoc/Kahla/What%20is%20Kahla.md)

## How to contribute

There are many ways to contribute to the project: logging bugs, submitting pull requests, reporting issues, and creating suggestions.

Even if you have push rights on the repository, you should create a personal fork and create feature branches there when you need them. This keeps the main repository clean and your personal workflow cruft out of sight.

We're also interested in your feedback for the future of this project. You can submit a suggestion or feature request through the issue tracker. To make this process more effective, we're asking that these include more information to help define them more clearly.