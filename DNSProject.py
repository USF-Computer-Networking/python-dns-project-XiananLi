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

'''
    Source:https://www.youtube.com/watch?v=kuSXK4gNYqw&t=1464s
    learned twisted internet, and dns datagram protocol through this link
'''
