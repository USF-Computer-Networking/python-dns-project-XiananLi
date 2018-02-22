#!/usr/bin/env python

''' this program will simply return the client's ip address from a dns server 
    and the time to live data
'''
from twisted.internet import tast
from twisted.names import dns

def main(reactor):
    proto = dns.DNSDatagramProtocol(controller=None)
    reactor.listenUDP(0, proto)

    d = proto.query(('8.8.8.8', 53)), [dns.Query('www.google.com', dns.AAAA)]
    d.addCallback(printResult)
    return d

def printResult(res):
    print'ANSWERS: ', [a.payload for a in res.answers]

task.react(main)


————————————————————————————————————————————————————————————————————————
''' similar result but from server's side
'''
from twisted.internet import tast
from twisted.names import dns

def main(reactor):
    proto = dns.DNSDatagramProtocol(controller=controller())
    reactor.listenUDP(10053, proto)
    
    return defer.Deferred()

class Controll(object):
    def messageReceived(self, message, proto, address):
        print "MESSAGE_RECEIVED", message.queries, "FROM", address
        message.answer = True
        message.answer = [
            dns.RRHEader(message.queries[0].name.name,
                           payload=dns.Record_A('8.8.8.8'))
        ]
        proto.writeMessage(message, address)
task.react(main)


'''
    Source:https://www.youtube.com/watch?v=kuSXK4gNYqw&t=1464s
    learned twisted internet, and dns datagram protocol through this link
'''
