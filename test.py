import vk_api
import asyncio
from vk_api.longpoll import MSGID, VkLongPoll, VkEventType

token = 'c07a86e5e94292b881c62aabf7d453ff76c8dbf8d00b30289ba79f309ac7b2300cb7abc00e4b312d3df8b'
vk = vk_api.VkApi(app_id=6146827, token=token)
longpoll = VkLongPoll(vk, wait=0)

def wrt_msg(peer_id, message):
    vk.method('messages.send', {'peer_id': event.peer_id, 'message': message, 'random_id': 0})

async def ping(peer_id):
	await asyncio.sleep(0.4)
	if event.text.lower() == '!ping':
		wrt_msg(peer_id, 'pong')

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		peer_id = event.peer_id
		asyncio.run(ping(peer_id))