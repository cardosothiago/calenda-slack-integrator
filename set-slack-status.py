from slack import WebClient
from slack.errors import SlackApiError

client = WebClient(token='token')

print(client.users_identity())


def set_slack_status(user_id=str, status_text=str, status_emoji=str, status_expiration=int):
    client.users_profile_set(
        profile={
            "user": user_id,
            "status_text": str(status_text),
            "status_emoji": str(status_emoji),
            "status_expiration": int(status_expiration)
        }
    )


def set_slack_snooze(minutes=int):
    client.dnd_setSnooze(num_minutes=minutes)


def set_slack_presence(is_present=bool):
    try:
        if is_present:
            client.users_setPresence(presence='auto')
        elif not is_present:
            client.users_setPresence(presence='away')
        else:
            client.users_setPresence(presence=is_present)
    except:
        print('is_present is a bool type')
