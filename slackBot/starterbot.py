import time

from slackclient import SlackClient

from slackBot.recommender import recommend, query_item

# starterbot's ID as an environment variable
# BOT_ID = os.environ.get("BOT_ID")
BOT_ID = "U3FJUCJ4A"

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "!do"
CHECK = "!check"
LAKSHMI = "!lakshmi"
CODE = "!code"
THINK = "!think"
RECOMMEND = "!recommend"
PRODUCT = ""
COUNT = 0

# instantiate Slack & Twilio clients
# slack_client = SlackClient(os.environ.get('xoxb-117640426146-oCZScxy8XJKzpHPJ0IALFoL5'))
slack_client = SlackClient('xoxb-117640426146-oCZScxy8XJKzpHPJ0IALFoL5')


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"

    if command.startswith(CHECK):
        response = "Hi! What do you want me to check?"

    if command.startswith(LAKSHMI):
        response = "Hi Chunnu! :3"

    if command.startswith(CODE):
        response = "```This is a code snippet```"

    if command.startswith(THINK):
        response = ":thinking_face:"

    if command.startswith(RECOMMEND):
        PRODUCT = command.split(" ")[1]
        COUNT = command.split(" ")[2]
        response = COUNT + " products similar to " + query_item(PRODUCT) + " : \n" + 
            recommend(int(PRODUCT), int(COUNT))

    # print("Command : " + command.split(" ")[0])
    # print("Command : " + command.split(" ")[1])

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
