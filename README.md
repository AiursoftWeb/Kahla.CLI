# Kahla.CLI
Kahla for CLI. An implementation for Kahla API: [here](https://wiki.aiursoft.com/ReadDoc/Kahla/What%20is%20Kahla.md)

## How to use

View Help

```bash
$ ./kahla --help
```

Log in

```bash
$ ./kahla login -u <username> -p <password>
```

Listen

```bash
$ kahla listen
```

Friendship

```bash
$ ./kahla friends
```

```bash
$ ./kahla searchfriends -u <username>
```

```bash
$ ./kahla deletefriends -u <username> # 未实现
```

Conversation

```bash
$ ./kahla send -u <username> -m <content>
```

```bash
$ ./kahla get-messages -u <username> -t 15
```

## How to run

```bash
$ pip install requirement.txt
$ python Program.py
```