import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('songTable')


def get_single_song(artist_name, song_title):
    response = table.get_item(
        Key={
            'artistName': artist_name,
            'songTitle': song_title
        }
    )
    item = response.get('Item')
    if item:
        print("GetItem result:", item)
    else:
        print("Song not found.")


def query_by_artist(artist_name):
    response = table.query(
        KeyConditionExpression=Key('artistName').eq(artist_name)
    )
    print(f"\nSongs by {artist_name}:")
    for item in response.get('Items', []):
        print(item)


def query_artist_songs_starting_with(artist, starts_with):
    artist_key = Key('artistName').eq(artist)
    song_title_key = Key('songTitle').begins_with(starts_with)
    response = table.query(
        KeyConditionExpression=artist_key & song_title_key
    )
    print("\nRihanna songs starting with 'D':")
    for item in response.get('Items', []):
        print(item)


def scan_all_songs():
    response = table.scan()
    print("\nAll songs in table:")
    for item in response.get('Items', []):
        print(item)


get_single_song('Rihanna', 'Umbrella')
query_by_artist('Shakira')
query_artist_songs_starting_with('Rihanna', 'D')
# Only use scan in more limited contexts
scan_all_songs()
