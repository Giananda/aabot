# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,requests,urllib
from gtts import gTTS
import goslate,os,wikipedia,subprocess,shutil,urllib2,urllib3
from bs4 import BeautifulSoup
from random import randint


cl = LINETCR.LINE()
cl.login(qr=True)
#cl.login(token="")
cl.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""_________________________________

Bot Publik B͎̣̫͈̥̗͒͌̃͑̔̾ͅU̟͎̲͕̼̲ͮͫͭ̋ͭ͛ͣ̈K̲̱̠̞̖ͧ̔͊̿̑ͯͅA̘̫͈̭͌͛͌̇̇̍N͉̠̙͉̗̺̋̔ͧ̊ J͇̗̲̞̹̝̫̞ͬ͐̀ͧ̿U̟͎̲͕̼̲ͮͫͭ̋ͭ͛ͣ̈M̘͈̺̪͓̺ͩ͂̾ͪ̀̋P̱̱̬̻̞̩͎̌ͦ̏ͪ͋̚B͎̣̫͈̥̗͒͌̃͑̔̾ͅO̜̓̇ͫ̉͊ͨT̘̟̼̉̈́͐͋͌̊ v 2.6
==========BotMenu===========

Apakah <teks> (seperti kerang ajaib)
kedapkedip <Teks>= coba aja
Dosa @(by tag) = Buat lucu2an
Pahala @(by tag) = Buat lucu2an
Cinta <teks> = buat lucu2an
Mid @(by tag) = melihat mid
Info @(by tag) = info yg di tag
Steal = Menu steal
Say =  menu teks ke suara 
Gift = menu gift
Invite = mengundang by kontak
Pap set <link gambar>
Pap = mengirim gambar yg telah di set
Google <yg dicari>
/set > /tes Untuk Cek Sider
/tagall = Tag semua member
/tid = translate ing > ind
/ten = translate ind > ing
/gcreator = Menunjukkan pembuat grup
/ginfo = Info grup
/cancel = Membatalkan semua undanganan
/ourl = Invite by link on
/curl = Invite by link off
/help = Menampilkan keyword
/keluar = Bot meninggalkan grup
/restart = merestart bot
/cek <tanggal> |contoh: /cek 21-02-2222
/musik <penyanyi> <judul>
/wiki <yg dicari>
/image <yg dicari>
/video <judul>
/ig <nama>
/yt <judul>
/ps <app playstore>

Nb: gausah pake <>
==========BotCreator==========

Ĝ̵͚͈̠̟͎̝͑̎̎̐̀̃͐Ḭ̸̛̞̣̠͓͖͚̽̏̉̍͌͒̅̈́̋̕͠A̴̢̨͕̳͕̲̪͙̰͍̯̲̿̀̅͒̌̌̉̆̏͠ͅN̷̨̨̫̞̭͔̖̳͍͔̗̰͚̺̋̿͛͒̏͜͝Ȁ̵͖̲̥̜̣̞̝̔̀̽̀̆́̐͐́̚͘ͅN̷̨̨̫̞̭͔̖̳͍͔̗̰͚̺̋̿͛͒̏͜͝D̴̯͍̝̯͔̤̟̭̦͓͖̺̣̟͚́͗̈́͛̋̈́̓̄̄͘͜Ȁ̵͖̲̥̜̣̞̝̔̀̽̀̆́̐͐́̚͘ͅ
==>"Instagram.com/gianandaal"<==
_________________________________
"""
qwerty ="""ADMIN KEY
List grup
Gbc
Gbcs
Gbcp
Cbc
Cb
Cn
K on/off
W on/off
Like on/off
Join on/offf
Bye on/off
Tag on/off
Invitemeto <gid>
Keluar dari <gid>
Spam on/off <jumlah> <kata>
"""
hadiah ="""===Key===
/gift1
/gift2
/gift3
/gift4
/all gift
/unicode1

Nb: untuk line versi uptodate unicode tidak menyababkan lag
"""

say =""" /say <teks> = teks ke suara Indo
.say Jepang
-say inggris
*say Arab
#say Korea
!say Jawa
^say Sunda
'say prancis"""

steal ="""Steal dp @(by tag)
Steal home @(by tag)
Steal bio @(by tag)
Steal contact @(by tag)
Steal grup = melihat dp grup
Steal gid = melihat id grup
Myname = nama kalian
Mybio = bio kalian
Mymid = mid kalian
Mydp = dp kalian
Mycover = cover kalian
Mycontact = kontak kalian
"""

KAC=[cl]
mid=cl.getProfile().mid

Bots=[mid, "u7eacf1df769225a00ec981cbd5830e23"]
admin=["u7eacf1df769225a00ec981cbd5830e23"]
staff=["u7eacf1df769225a00ec981cbd5830e23"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"Owner\n=> instagram.com/gianadaal",
    "lang":"JP",
    "comment":"AutoLike by Giananda\n\n=> instagram.com/gianandaal",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":" ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "atjointicket":True,
    "Protectcancl":False,
    "Protectjoin":False,
    "Protectgr":False,
    "Welcomemessage":True,
    "Byemessage":True,
    "likeOn":False,
    "tag":True,
    "winvite":False,
    "displayName":{},
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

#-------------------

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
           if wait["Protectgr"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                   random.choice(DEF).updateGroup(G)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
           if wait["Protectcancl"] == True:
               if op.param2 not in Bots:
                  group = cl.getGroup(op.param1)
                  gMembMids = [contact.mid for contact in group.invitee]
                  random.choice(DEF).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#
        if op.type == 13:
	    if op.param3 in Bots:
		if wait["autojoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
		    cl.sendText(op.param1, "Terimakasih ＼(^o^)／\nSilahkan ketik /help.")
		    cl.sendText(op.param1, "Creator:\n=> Giananda")
		    print "Bot join grup"
#------Cancel Invite User Finish------##
        if op.type == 13:
            if op.param3 in Bots:
                if op.param2 in admin:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendText(op.param1, "Terimakasih ＼(^o^)／\nSilahkan ketik /help.")
                    cl.sendText(op.param1, "Creator:\n=> Giananda")
                    print "Bot join grup"









#-------------------------------------------------------------------------------
        if op.type == 17:
            if wait["Welcomemessage"] == True:
                    group = cl.getGroup(op.param1)
		    cb = Message()
                    cb.to = op.param1
                    cb.text = cl.getContact(op.param2).displayName + " Selamat Datang di Grup : " + group.name + "\n\nGrup Creator => " + group.creator.displayName
                    cl.sendMessage(cb)

	if op.type == 15:
	   if wait["Byemessage"] == True:
	    if op.param2 in Bots:
		return
	    cl.sendText(op.param1, "Good bye..(=ﾟωﾟ)ﾉ")
	    print "MemberLeft"

#------------------------------------------------------
                        
                        
                        
                        
                        
                        
                    
                    
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
#
	if op.type == 26:
            msg = op.message
            try:
		if msg.contentType == 0:
		    try:
			if msg.to in wait2['readPoint']:
			    if msg.from_ in wait2["ROM"][msg.to]:
				del wait2["ROM"][msg.to][msg.from_]
			else:
			    pass
		    except:
		        pass
		else:
	    	    pass
	    except KeyboardInterrupt:
		sys.exit(0)
	    except Exception as error:
		print error
		print ("\n\nRECEIVE_MESSAGE\n\n")
		return

        if op.type == 26:
	    msg = op.message

            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")


               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
	    elif msg.text in ["Say"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,say)

	    elif msg.text in ["Steal"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,steal)


            elif msg.text in ["/help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["help"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,qwerty)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("/gn " in msg.text):
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)

            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])

            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["/bot"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

	    elif msg.text in ["Gift"]:
		cl.sendText(msg.to,hadiah)


            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","/gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","/gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","/gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","/gift4"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","/all gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["/cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["/ourl"]:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link open")
                    else:
                        cl.sendText(msg.to,"Already open")
            elif msg.text in ["/curl"]:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link Close")
                    else:
                        cl.sendText(msg.to,"Already close")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "/ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Steal gid" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mymid" == msg.text:
                cl.sendText(msg.to, msg.from_)
            elif "Mid RA" == msg.text:
                cl.sendText(msg.to,mid)

            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
		ki.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
		ki.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
		ki.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
		ki.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
		ki.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
		ki.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
		ki.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
		ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
		ki.sendMessage(msg)
            elif msg.text in ["TL: "]:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"]) 

	    elif "Cn " in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 9999999999999:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Names >" + string + "<")

	    elif "Cb " in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cb ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio >" + string + "<")

            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Joinn on","joinn on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Joinn off","joinn off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancl on","cancl on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancl off","cancl off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gr on","gr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gr off","gr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["K On","K on","k on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["K Off","K off","k off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Set View"]:
                md = ""
                if wait["Protectjoin"] == True: md+="􀔃􀆑lock􏿿  Block Join\n"
                else: md+=" Block Join Off\n"
                if wait["Protectgr"] == True: md+="􀔃􀆑lock􏿿   Block Group\n"
                else: md+=" Block Group Off\n"
                if wait["Protectcancl"] == True: md+="􀔃􀆑lock􏿿 Cancel All Invited\n"
                else: md+=" Cancel All Invited Off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Grup id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["/gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
         #-------------Fungsi Jam on/off Finish-------------------#           
         
         #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
         #-------------Fungsi Change Clock Finish-----------------#

#--------------------#

	    elif "/lirik " in msg.text.lower():
                songname = msg.text.replace("/lirik ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to, 'Tunggu....')
                    cl.sendText(msg.to,song[5])
                    print "[Command] Lirik"


	    elif msg.text in ["/gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
		    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)

	    elif "kedapkedip " in msg.text.lower():
                txt = msg.text.replace("kedapkedip ", "")
                cl.kedapkedip(msg.to,txt)

#--------------ListGroup------------------#
            elif msg.text in ["List grup"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                h = ""
		for i in gid:
                    h += "[🛫] %s\n" % (cl.getGroup(i).name +"→["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"▒▒▓█[List Grup]█▓▒▒\n"+ h +"Total Group ="+"["+str(len(gid))+"]")

            elif "Steal bio " in msg.text:
                       nk0 = msg.text.replace("Steal bio ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    y = contact.statusMessage
                                    cl.sendText(msg.to,y)
                                except Exception as e:
                                    cl.sendText(msg.to,"Lupa")
                                    print e
















#-------------------#

	    elif "Steal dp @" in msg.text:
		print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
		if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
		    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
			    cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"


	    elif "Steal home @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"

#-----------------------------------------------
            elif "^say " in msg.text.lower():
                    query = msg.text.replace("^say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'su', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)

            elif "!say " in msg.text.lower():
                    query = msg.text.replace("!say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'jw', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)

	    elif "/say " in msg.text:
                 psn = msg.text.replace("/say ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')

	    elif ".say " in msg.text:
                 psn = msg.text.replace(".say ","")
                 tts = gTTS(psn, lang='ja', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')

	    elif "-say " in msg.text:
                 psn = msg.text.replace("-say ","")
                 tts = gTTS(psn, lang='en', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')

	    elif "#say " in msg.text:
                 psn = msg.text.replace("#say ","")
                 tts = gTTS(psn, lang='ko', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')

	    elif "*say " in msg.text:
                 psn = msg.text.replace("*say ","")
                 tts = gTTS(psn, lang='ar', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')

	    elif "'say " in msg.text:
                 psn = msg.text.replace("'say ","")
                 tts = gTTS(psn, lang='fr', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')

            elif "Cinta " in msg.text:
                  tanya = msg.text.replace("Cinta ","")
                  jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                  jawaban = random.choice(jawab)
		  tanyu = ("Cinta " + tanya + " Adalah ")
                  tts = gTTS(tanyu + jawaban, lang='id', slow=False)
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to, 'tts.mp3')

	    elif msg.text in ["Pagi","pagi","selamat pagi","Selamat Pagi","Ohayou","Ohayo","ohayou","ohayo","Met pagi","met pagi"]:
		 sapa = ("オハイオニイちゃんおにちゃんガンバッテクダサイイネ")
                 tts = gTTS(sapa, lang='ja', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')

#-----------------------------------------------------
            elif "/cek " in msg.text:
                tanggal = msg.text.replace("/cek ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
#-----------------------------------------------------

	    elif "/musik " in msg.text:
		songname = msg.text.replace("/musik ","")
		params = {"songname": songname}
		r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
		data = r.text
		data = json.loads(data)
		for song in data:
			abc = song[3].replace('https://','http://')
			cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
			cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
			cl.sendAudioWithURL(msg.to,abc)
			cl.sendText(msg.to, "That's the song for " + song[0])

	    elif '.musik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('.musik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))




#-----------------------------------------------


	    elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lirik Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))

            elif "/ytl " in msg.text:
                query = msg.text.replace("/ytl ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'

#==========================================
            elif "/yt " in msg.text.lower():
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
#========================================



            elif '/wiki ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("/wiki ","")
                      wikipedia.set_lang("id")
                      pesan=wikipedia.page(wiki).title
                      pesan+="\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))

	    elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "===INSTAGRAM INFO USER====\n"
                    details = "\n===INSTAGRAM INFO USER==="
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))

#Restart_Program--------
            elif msg.text in ["/restart"]:
                cl.sendText(msg.to, "Bot has been restarted")
                restart_program()
                print "@Restart"

	    elif ("Add staff " in msg.text):
              if msg.from_ in admin:
                 if msg.toType == 2:
                     key = eval(msg.contentMetadata["MENTION"])
                     key["MENTIONEES"][0]["M"]
                     targets = []
                     for x in key["MENTIONEES"]:
                         targets.append(x["M"])
                     for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Staff Ditambahkan")
                            print "[Command]Staff add executed"
                        except:
                            pass


	    elif ("Del staff " in msg.text):
              if msg.from_ in admin:
                 if msg.toType == 2:
                     key = eval(msg.contentMetadata["MENTION"])
                     key["MENTIONEES"][0]["M"]
                     targets = []
                     for x in key["MENTIONEES"]:
                         targets.append(x["M"])
                     for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Deleting staff")
                            print "[Command]Staff remove executed"
                        except:
                            pass
              else:
                   cl.sendText(msg.to,"Command denied.")
                   cl.sendText(msg.to,"Owner permission required.")

	    elif msg.text.lower() == 'stafflist':
                if admin == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Waiting...")
                    num=1
                    mc = "===[Staff List]==="
                    for mi_d in admin:
                        mc += "\n%i. %s" % (num, cl.getContact(mi_d).displayName)
                    num=1
                    mc = "===[Staff List]==="
                    for mi_d in admin:
                        mc += "\n%i. %s" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"

	    elif msg.text in ["W on"]:
              if msg.from_ in admin:
                if wait["Welcomemessage"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Welcomemessage"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["W off"]:
              if msg.from_ in admin:
                if wait["Welcomemessage"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome message Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Welcomemessage"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome message Off")
                    else:
                        cl.sendText(msg.to,"done")

	    elif msg.text in ["Bye on"]:
              if msg.from_ in admin:
                if wait["Byemessage"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Bye message On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Byemessage"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Bye message On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Bye off"]:
              if msg.from_ in admin:
                if wait["Byemessage"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Bye message Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Byemessage"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Bye message Off")
                    else:
                        cl.sendText(msg.to,"done")

#-----------------------------[Command]----------------------------#
            elif msg.text in ["Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["いいね:オフ","Like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")


	    elif "/image " in msg.text:
                search = msg.text.replace("/image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
		    cl.sendImageWithURL(msg.to,path)
		    print "Image"
                except:
                    pass

#------
            elif msg.text in ["Tag on"]:
	      if msg.from_ in admin:
                if wait["tag"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Tag On")
                else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag On")
                    else:
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Tag off"]:
	      if msg.from_ in admin:
                if wait["tag"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Tag Off")
                else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag Off")
                    else:
                        cl.sendText(msg.to,"Already off")
#-----------------------------[Command]-----------------------------#
            elif "@ই͜͜͡☬Giananda " in msg.text:
	      if wait["tag"] == True:
		resp = ("《《AUTO RESPON》》\n")
                jawab = ("Jgn Tag Si Giananda!!","Berisik jgn tag si Giananda")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,resp + jawaban)

	    elif "@"+cl.getProfile().displayName in msg.text:
	      if wait["tag"] == True:
                resp = ("《《AUTO RESPON》》\n")
                jawab = ("apa kak ? ketik /help untuk bantuan","Cie ngetag bot\nketik /help.")
		jawabam = random.choice(jawab)
                cl.sendText(msg.to,resp + jawabam)

	    elif msg.text in ["Invite"]:
                wait["winvite"] = True
                cl.sendText(msg.to,"send contact 😉\njika ingin membatalkan ketik /restart")
	    if wait["winvite"] == True:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
				 wait["winvite"] = False
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done, Invited this human: \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     cl.sendText(msg.to,"Negative, Error detected\nmaybe limit inv")
                                     wait["winvite"] = False
                                     break




#-----------------------------------------
            elif "Info @" in msg.text:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                van = cl.getGroup(msg.to)
                for linedev in van.members:
                    if target == linedev.displayName:
                        mid = cl.getContact(linedev.mid)
                        try:
                            cover = cl.channel.getCover(linedev.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + mid.displayName + "\n[Mid]:\n" + linedev.mid + "\n[BIO]:\n" + mid.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + mid.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass
#-----------------------------------------------
            elif "Stalk @" in msg.text:
                 print "[Command]Stalk executing"
                 stalkID = msg.text.replace("Stalk @","")
                 subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])
                 files = glob.glob("tmp/*.jpg")
                 for file in files:
                     os.rename(file,"tmp/tmp.jpg")
                 fileTmp = glob.glob("tmp/tmp.jpg")
                 if not fileTmp:
                     cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                     print "[Command]Stalk,executed - no image found"
                 else:
                     image = upload_tempimage(client)
                     cl.sendText(msg.to, format(image['link']))
                     subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                     print "[Command]Stalk executed - succes"

	    elif "/ps " in msg.text.lower():
    		tob = msg.text.lower().replace("/ps ","")
    		cl.sendText(msg.to,"Sedang Mencari...")
    		cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
    		cl.sendText(msg.to,"Tuh link nya boss")

    	    elif "Google " in msg.text:
        	go = msg.text.replace("Google ","")
        	cl.sendText(msg.to,"Search: " + go + "\n Link: google.com/search?q=" + go)


#=================================
            elif "Invitemeto " in msg.text.lower():
		ng = msg.text.lower().replace("Invitemeto ","")
		gid = cl.getGroupIdsJoined()
		try:
		    if msg.from_ in admin:
                        for i in gid:
                            h = cl.getGroup(i).name
		            if h == ng:
		                cl.inviteIntoGroup(i,[Creator])
			        cl.sendText(msg.to,"Success join to ["+ h +"] group")
			    else:
			        pass
		    else:
		        cl.sendText(msg.to,"Hanya admin dan creator yg bisa menggunakan")
		except Exception as e:
		    cl.sendMessage(msg.to, str(e))
#==================================================================
            elif "Keluar dari " in msg.text.lower():
		ng = msg.text.lower().replace("Keluar dari ","")
		gid = cl.getGroupIdsJoined()
		try:
		    if msg.from_ in admin:
                        for i in gid:
                            h = cl.getGroup(i).name
		            if h == ng:
		                cl.leaveGroup(i)
			        cl.sendText(msg.to,"Success leave to "+ h)
			    else:
			        pass
		    else:
		        cl.sendText(msg.to,"Hanya admin dan creator yg bisa menggunakan")
		except Exception as e:
		    cl.sendMessage(msg.to, str(e))
#=================================-------------=================================
            elif '/video ' in msg.text.lower():
                try:
                    textToSearch = msg.text.lower().replace('/video ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght=('https://www.youtube.com' + results['href'])
		    cl.sendVideoWithURL(msg.to,ght)
                except:
                    cl.sendText(msg.to,"Could not find it")
#================================= ========================================
            elif msg.text in ["Myname"]:
                    h = cl.getContact(msg.from_)
                    cl.sendText(msg.to,h.displayName)
#========================================
            elif msg.text in ["Mybio"]:
                    h = cl.getContact(msg.from_)
                    cl.sendText(msg.to,h.statusMessage)
#======================================== ===============Image====================#
            elif msg.text in ["Mydp"]:
                    h = cl.getContact(msg.from_)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
#==============Image finish================# ===============Image====================#
            elif msg.text in ["Mycover"]:
                h = cl.getContact(msg.from_)
                cu = cl.channel.getCover(msg.from_)
                path = str(cu)
                cl.sendImageWithURL(msg.to, path)
 #==============Image finish================#
#//commandnya
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "「Sudah berjalan selama 」"+waktu(eltime)
                cl.sendText(msg.to,van)
            elif msg.text is None:
                return
#----------------
            elif "Steal contact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
#----------------
            elif "Mycontact" in msg.text:
                mmid = cl.getContact(msg.from_)
                msg.contentType = 13
                msg.contentMetadata = {"mid": msg.from_}
                cl.sendMessage(msg)
#=================================================
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")














#-----------------------------------------
	    elif "Pap set " in msg.text:
                wait["Pap"] = msg.text.replace("Pap set ","")
                cl.sendText(msg.to,"Pap Has Ben Set To")

	    elif msg.text in [".Pap","Pap"]:
                cl.sendImageWithURL(msg.to,wait["Pap"])

	    elif "Vid set " in msg.text:
                wait["vid"] = msg.text.replace("Vid set ","")
                cl.sendText(msg.to,"Vid Has Ben Set To")
            elif msg.text in [".vid","Vid"]:
                cl.sendVideoWithURL(msg.to,wait["vid"])




#-------------------------------------------------
	    elif "Mid @" in msg.text:
	          _name = msg.text.replace("Mid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          cl.sendText(msg.to, g.mid)
                      else:
                          pass

	    elif msg.text in ["Remove all chat"]:
	      if msg.from_ in admin:
		cl.removeAllMessages(op.param2)
		cl.sendText(msg.to,"Removed all chat")

	    elif "Gbcs " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Gbcs ", "")
                bc = (".Btw.. Ini adalah Broadcast")
                cb = (bctxt + bc)
		tts = gTTS(cb, lang='id', slow=False)
                tts.save('tts.mp3')
                n = cl.getGroupIdsJoined()
                for manusia in n:
                 cl.sendAudio(manusia, 'tts.mp3')

	    elif "Gbcp " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Gbcp ", "")
                n = cl.getGroupIdsJoined()
                for manusia in n:
                    cl.sendText(manusia,bctxt)

	    elif "Gbc " in msg.text:
	      if msg.from_ in admin:
		bctxt = msg.text.replace("Gbc ", "")
		bc = ("《《BROAD CAST》》\n_________________________________\n")
		cb = ("\n\n_________________________________\nBot creator:\n=> Giananda")
    		n = cl.getGroupIdsJoined()
    	        for manusia in n:
	            cl.sendText(manusia,bc +  bctxt + cb)

	    elif "Cbc " in msg.text:
	      if msg.from_ in admin:
    		bctxt = msg.text.replace("Cbc ", "")
    		t = cl.getAllContactIds()
    		for manusia in t:
         	    cl.sendText(manusia, (bctxt))

#--------------------------------- TRANSLATE --------------------------------
	    elif "/ten " in msg.text:
                txt = msg.text.replace("/ten ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "/tid " in msg.text:
                txt = msg.text.replace("/tid ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')

	#-----------KERANG---------#
	    elif "Apakah " in msg.text:
    		tanya = msg.text.replace("Apakah ","")
    		jawab = ("Iya","Tidak","Mana saya tau sayakan autis","mungkin iya","mungkin tidak")
    		jawaban = random.choice(jawab)
		tts = gTTS(text=jawaban, lang='id')
		tts.save('tts.mp3')
    		cl.sendAudio(msg.to,'tts.mp3')

#----------------------
            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Dosanya " + tanya + "adalah " + jawaban + " Banyak banyak tobat Nak ")
#----------------------
	    elif "Pahala @" in msg.text:
                tanya = msg.text.replace("Pahala @","")
                jawab = ("0%","20%","40%","50%","60%","Tak ada")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Pahalanya " + tanya + "adalah " + jawaban + "\nTobatlah nak")

	#-------------------------------#

	    elif "Steal grup" in msg.text:
                   group = cl.getGroup(msg.to)
                   path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                   cl.sendImageWithURL(msg.to, path)


         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
         #-------------Fungsi Jam Update Finish-------------------#
	    elif msg.text in ["/set"]:
		 if msg.toType == 2:
		    cl.sendText(msg.to, "Set reading point\nSilahkan ketik 「/tes」")
		    try:
			del wait2['readPoint'][msg.to]
			del wait2['readMember'][msg.to]
		    except:
			pass
 		    wait2['readPoint'][msg.to] = msg.id
 		    wait2['readMember'][msg.to] = ""
 		    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
 		    wait2['ROM'][msg.to] = {}
  		    print "Lurkset"

	    elif msg.text in ["/tes"]:
 		 if msg.toType == 2:
 		    print "\nSider check aktif..."
  		    if msg.to in wait2['readPoint']:
 			if wait2["ROM"][msg.to].items() == []:
 			    chiya = ""
 			else:
			    chiya = ""
			    for rom in wait2["ROM"][msg.to].items():
 				print rom
				chiya += rom[1] + "\n"
 			cl.sendText(msg.to, "Pembaca:\n_________________________________%s\n\nSidernya:\n_________________________________\n%s\n\n_________________________________\nIn the last seen point:\n[%s]\n_________________________________" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
			print "\nReading Point Set..."
			try:
			    del wait2['readPoint'][msg.to]
			    del wait2['readMember'][msg.to]
			except:
			    pass
			wait2['readPoint'][msg.to] = msg.id
			wait2['readMember'][msg.to] = ""
			wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
			wait2['ROM'][msg.to] = {}
			print "lukers"
			cl.sendText(msg.to, "Auto set reading point\nSilahkan ketik 「/tes」")
		    else:
			cl.sendText(msg.to, "Ketik 「/set」 dulu kaka...\nHehe")

    #-------------Fungsi Leave Group Start---------------#

	    elif msg.text in ["/keluar"]:
	      if msg.from_ in staff:
		if msg.toType == 2:
		    ginfo = cl.getGroup(msg.to)
		    try:
			cl.sendText(msg.to, "kakak jahatヽ(｀Д´)ﾉ")
			cl.leaveGroup(msg.to)
		    except:
			pass
	      else:
		cl.sendText(msg.to, "Maaf anda kurang beruntung")
    #-------------Fungsim Leave Group Finish---------------#

    #-------------Fungsi Tag All Start---------------#

	    elif msg.text in ["/tagall"]:
                              group = cl.getGroup(msg.to)
                              nama = [contact.mid for contact in group.members]
                              nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                              if jml <= 100:
                                 mention(msg.to, nama)
                              if jml > 100 and jml < 200:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 mention(msg.to, nm1)
                                 for j in range (100, len(nama)-1):
                                        nm2 += [nama[j]]
                                 mention(msg.to, nm2)
                              if jml > 200 and jml < 300:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 mention(msg.to, nm1)
                                 for j in range (100, 199):
                                        nm2 += [nama[j]]
                                 mention(msg.to, nm2)
                                 for k in range (200, len(nama)-1):
                                        nm3 += [nama[k]]
                                 mention(msg.to, nm3)
                              if jml > 300 and jml < 400:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 mention(msg.to, nm1)
                                 for j in range (100, 199):
                                        nm2 += [nama[j]]
                                 mention(msg.to, nm2)
                                 for k in range (200, 299):
                                        nm3 += [nama[k]]
                                 mention(msg.to, nm3)
                                 for l in range (300, len(nama)-1):
                                     nm4 += [nama[l]]
                                 mention(msg.to, nm4)
                              cnt = Message()
                              cnt.text = "Done:"+str(jml)
                              cnt.to = msg.to
                              cl.sendMessage(cnt)

	    elif (msg.text == 'Memlist'):
		a = cl.getGroup(msg.to)
		b = []
  		for i in a.members:
     		    b.append('•'+i.displayName)
  		c = '\n'.join(b)
  		cl.sendText(msg.to,'MEMBER LIST\n' + c)
    #-------------Fungsi Tag All Finish---------------#

         #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Killban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Selamat tinggal")
                        ki.sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,cl]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
         #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Cleanse" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Cleanse","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"maaf kalo gak sopan")
                    cl.sendText(msg.to,"makasih semuanya..")
                    cl.sendText(msg.to,"he")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[cl,ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"Group cleanse")
                                kk.sendText(msg.to,"Group cleanse")
                                kc.sendText(msg.to,"Group cleanse")

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Kasian Di Kick....")
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Ban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                cl.sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                cl.sendText(msg.to,"Error")
           #----------------Fungsi Unbanned User Target Finish-----------------------#

            elif msg.text in ["join"]:
	      if msg.from_ in admin:
		cl.sendText(msg.to,"/join")

            elif msg.text in ["hi"]:
                cl.sendText(msg.to,"Hi 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"follow IG saya 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"instagram.com/gianandaal 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["/unicode1"]:
                cl.sendText(msg.to,"44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.55.44.44.44.44.44.44.44.4444.44.44.4.44.4.44.44.4.440.440.004444.4444.44.33.")
            elif msg.text in ["/creator"]:
                cl.sendText(msg.to,"==========BotCreator==========\n\nĜ̵͚͈̠̟͎̝͑̎̎̐̀̃͐Ḭ̸̛̞̣̠͓͖͚̽̏̉̍͌͒̅̈́̋̕͠A̴̢̨͕̳͕̲̪͙̰͍̯̲̿̀̅͒̌̌̉̆̏͠ͅN̷̨̨̫̞̭͔̖̳͍͔̗̰͚̺̋̿͛͒̏͜͝Ȁ̵͖̲̥̜̣̞̝̔̀̽̀̆́̐͐́̚͘ͅN̷̨̨̫̞̭͔̖̳͍͔̗̰͚̺̋̿͛͒̏͜͝D̴̯͍̝̯͔̤̟̭̦͓͖̺̣̟͚́͗̈́͛̋̈́̓̄̄͘͜Ȁ̵͖̲̥̜̣̞̝̔̀̽̀̆́̐͐́̚͘ͅ\n==>'Instagram.com/gianandaal'<==\nWajib follow􀜁􀅔Har Har􏿿")

            elif msg.text in ["bobo ah","Bobo dulu ah"]:
                cl.sendText(msg.to,"Have a nice dream  􀜁􀅔Har Har􏿿")
            elif msg.text in ["wc"]:
                cl.sendText(msg.to,"Selamat datang")
                cl.sendText(msg.to,"Jangan nakal ok!")
            elif msg.text in ["PING","Ping","ping"]:
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                cl.sendText(msg.to,"Ya gitu deh intinya 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#
	#-------------Fungsi Speedbot Start---------------------#
            elif msg.text in [".sp","Speedbot","speedbot"]:
                start = time.time()
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "seconds" % (elapsed_time))
	#-------------Fungsi Speedbot Finish---------------------#


       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["sp","Speedbot","speedbot"]:
		start = time.time()
		cl.sendText(msg.to, "Tunggu..")
                elapsed_time = time.time() - start
		cl.sendText(msg.to, "%sseconds" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
	      if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
                ki.sendText(msg.to,"send contact")
                kk.sendText(msg.to,"send contact")
                kc.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
	      if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
                ki.sendText(msg.to,"send contact")
                kk.sendText(msg.to,"send contact")
                kc.sendText(msg.to,"send contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
      
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#
	if op.type == 55:
	    try:
		if op.param1 in wait2['readPoint']:
		    Name = cl.getContact(op.param2).displayName
		    if Name in wait2['readMember'][op.param1]:
			pass
		    else:
			wait2['readMember'][op.param1] += "\n👉 " + Name + datetime.today().strftime(' [%d - %H:%M:%S]')
			wait2['ROM'][op.param1][op.param2] = "👉 " + Name
			wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
		else:
		    pass
	    except:
		pass
#
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)

                profile6 = ka.getProfile()
                profile6.displayName = wait["cName6"]
                ka.updateProfile(profile6)

                profile7 = kb.getProfile()
                profile7.displayName = wait["cName7"]
                kb.updateProfile(profile7)

                profile8 = ko.getProfile()
                profile8.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile9 = ke.getProfile()
                profile9.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile10 = ku.getProfile()
                profile10.displayName = wait["cName10"]
                ku.updateProfile(profile10)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
                   cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
		   print "Like"
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
thread1 = threading.Thread(target=autolike)
thread1.daemon = True
thread1.start()

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version: #If the Current Version of Python is 3.0 or above
        import urllib,request #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else: #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1: #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item) #Append all the links in the list named 'Links'
            time.sleep(0.1) #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "▪ @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         cl.sendMessage(msg)
    except Exception as error:
        print error









while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)


