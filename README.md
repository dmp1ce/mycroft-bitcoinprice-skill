# Mycroft bitcoin price skill

> You: "Hey Mycroft, what is the bitcoin price?"
> Mycroft: "600 USD is the bitcoin daily average price."

## Usage

Start Mycroft:
```
docker-compose up -d
```

Ask Mycroft enabled device about the "bitcoin price".


Or use the CLI by running:

```
$ docker-compose exec mycroft bash
$ cd ai; ./start cli
$ bitcoin price
```

## Issues

- This skill never actually successfully returned a bitcoin price to me, although it really should. I saw no problem with the request code. To prove that the code works I created a small python script called `bitcionaverage.py` which was able to get the bitcoin price from bitcoinaverage.com. Just run `python bitcionaverage.py` from within the Mycroft container.
- I had trouble getting Mycroft voice to work on my computer. Mycroft would usually understand what I'm saying but I could not hear responses. I had to use the logs at `/var/log/mycroft*` to get feedback. Only once did I get voice responses, but I don't know why.
