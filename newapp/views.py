from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time
# Create your views here.
def index (request):
    return render(request, 'index.html')


def videocall_opener(request):
    return render(request, 'videocall.html')


def getToken(request):
    appId = '7b8e56c519e44522b08ba45c28bd7429'
    appCertificate= 'bc35232131b54c189e9e72ced55a4b60'
    channelName=request.GET.get('channel')
    uid = random.randint(1,230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1
    token = token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token, 'uid':uid},safe=False)