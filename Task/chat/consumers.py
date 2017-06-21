import json
from channels import Group
from channels.sessions import channel_session
from channels import Channel
from channels.auth import channel_session_user_from_http, channel_session_user

from .models import Room , Status
@channel_session
@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    prefix, label = message['path'].strip('/').split('/')   
    room = Room.objects.get(label=label)
    #'get' will create a Entry in Status for a particular user in 
    #a particular table
    get=Status.objects.create(room=label,uname=message.user)
    Group(label).add(message.reply_channel)
    message.channel_session['room'] = room.label
    #Stat will store the user's status id 
    message.channel_session['stat']= get.id
    ws_status(message, get.id,"online")

@channel_session
def ws_receive(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)
    data = json.loads(message['text'])
    #'msg' will store the data in to the db and send it 
    #back to socket to display
    msg = room.messages.create(**data)
    Group(label).send({'text': json.dumps(msg.as_dict())})
@channel_session
def ws_status(message, id, stat):
    label = message.channel_session['room']
    u_id=Status.objects.get(id=id)
    Group(label).send({"text": json.dumps({
            "state": stat,
            "u_name": u_id.uname,
        }),  })
#ws_status will send online/Offline Status to the channel !! 

@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    id=message.channel_session['stat'] 
    ws_status(message,id,"offline")
    u_id=Status.objects.get(id=id)
    Status.objects.filter(uname=u_id.uname).delete()
    #It will clear the online status of the user
    Group(label).discard(message.reply_channel)

