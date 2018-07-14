# DeepMoji-docker

The [DeepMoji](https://github.com/bfelbo/DeepMoji]) project by @bfelbo et. al. uses a neural network trained on billions of tweets to select emoji that most accurately represent the emoji of input text. Their code is written in Python 2.7 using Tensorflow, and is available on [Github](https://github.com/bfelbo/DeepMoji]) 

This repository is a docker container for a web service to call the neural network as an API.

After deploying the container to `127.0.0.1`, you can send a POST request with sentences to find the emoji for.

```cURL
curl -X POST \
  http://127.0.0.1 \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 748a5055-d93a-4c2a-91ef-1b3bd1135845' \
  -d '{
	"sentences": ["I love this band!", "I hate this album."]
}'

```

The respose is, for each sentence, the a set of tuples containing the emoji, and the probability that emoji is related to the sentence:

```json
{
    "emoji": [
        [
            {
                "emoji": "😅",
                "prob": 0.00611169869080185890
            },
            {
                "emoji": "😒",
                "prob": 0.00045027132728137076
            },
            {
                "emoji": "😫",
                "prob": 0.00971820019185543060
            },
            {
                "emoji": "😭",
                "prob": 0.01060504186898469925
            }, ...

```