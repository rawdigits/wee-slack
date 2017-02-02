import glob
import json

#from wee_slack import render
from wee_slack import ProcessNotImplemented

def test_process_message(monkeypatch, realish_eventrouter, mock_websocket):

    eventrouter = realish_eventrouter

    t = eventrouter.teams.keys()[0]
    #u = eventrouter.teams[t].users.keys()[0]

    #user = eventrouter.teams[t].users[u]
    #print user

    socket = mock_websocket
    eventrouter.teams[t].ws = socket

    datafiles = glob.glob("_pytest/data/websocket/*.json")

    print datafiles
    #assert False

    notimplemented = set()

    for fname in sorted(datafiles):
        try:
            data = json.loads(open(fname, 'r').read())
            socket.add(data)
            eventrouter.receive_ws_callback(t)
            eventrouter.handle_next()
        except ProcessNotImplemented as e:
            notimplemented.add(str(e))


    if len(notimplemented) > 0:
        print "####################"
        print sorted(notimplemented)
        print "####################"
        #assert False




