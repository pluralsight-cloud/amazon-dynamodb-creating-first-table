import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('songTable')
songs = [
    {'artistName': 'Rihanna', 'songTitle': 'Umbrella', 'year': 2007, 'genre': 'Pop'},  # noqa: E501
    {'artistName': 'Rihanna', 'songTitle': 'Diamonds', 'year': 2012, 'genre': 'Pop'},  # noqa: E501
    {'artistName': 'Rihanna', 'songTitle': 'Work', 'year': 2016, 'genre': 'R&B'},  # noqa: E501
    {'artistName': 'Shakira', 'songTitle': 'Hips Don\'t Lie', 'year': 2006, 'genre': 'Latin Pop'},  # noqa: E501
    {'artistName': 'Shakira', 'songTitle': 'Waka Waka', 'year': 2010, 'genre': 'Pop'},  # noqa: E501
    {'artistName': 'Shakira', 'songTitle': 'Whenever, Wherever', 'year': 2001, 'genre': 'Latin Pop'},  # noqa: E501
    {'artistName': 'Ed Sheeran', 'songTitle': 'Shape of You', 'year': 2017, 'genre': 'Pop'},  # noqa: E501
    {'artistName': 'Ed Sheeran', 'songTitle': 'Perfect', 'year': 2017, 'genre': 'Pop'},  # noqa: E501
    {'artistName': 'Ed Sheeran', 'songTitle': 'Thinking Out Loud', 'year': 2014, 'genre': 'Pop'},  # noqa: E501
    {'artistName': 'Ed Sheeran', 'songTitle': 'Eyes Closed', 'year': 2023, 'genre': 'Pop'}  # noqa: E501
]


def put_item(song):
    table.put_item(Item=song)
    print(f"Inserted: {song['artistName']} - {song['songTitle']}")


def update_item():
    response = table.update_item(
        Key={
            'artistName': 'The Beatles',
            'songTitle': 'Hey Jude'
        },
        UpdateExpression="SET genre = :new_genre",
        ExpressionAttributeValues={
            ':new_genre': 'Classic Rock'
        },
        ReturnValues="UPDATED_NEW"
    )
    print("UpdateItem response:", response)


def delete_item():
    response = table.delete_item(
        Key={
            'artistName': 'The Beatles',
            'songTitle': 'Hey Jude'
        }
    )
    print("DeleteItem response:", response)

# Run the functions
# for song in songs:
#     put_item(song)
# update_item()
# delete_item()
