# Dungeon Quest
A console game made in python

# Synopsis

You are walking in the woods in the middle of the night and suddenly a portal opens and take you to a medieval dungeon.

You don't know exactly where you are or when you are, but its clear that the only way to get back is to walk accross the perils of the dungeon searching for the portal that will lead you home.

# Controls

* `Arrows` - movement
* `Space` - interactions

# Running with Docker

```docker
docker run -it --rm --name dungeon-quest -v "$PWD":/usr/src/myapp -w /usr/src/myapp amancevice/pandas python game.py
```

# License

Dungeon Quest is licensed under GNU GPL version 2
