# something-like
Slack bot for recommending similar items for a given product.

## What's inside
Content-based engine on a 500 item dataset!

## Instructions to use the slack bot
1. Send a message to the slackbot using "@somethinglike"
2. Pass in commands using "!recommend".

## Usage
--
The following example will find for a product stored in the dataset by the ID of 12 and return 5 similar products.

> @somethinglike !recommend 12 5

The outcome of for this request will be as follows

> 5 products similar to Baggies shorts :
> River shorts (score:0.246533861773)
> Baby baggies shorts (score:0.168165313005)
> Baggies shorts (score:0.164444723414)
> Girl's baggies shorts (score:0.149769047639)
> Baggies shorts (score:0.147408544023)
