#!/usr/bin/env python
# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------------------------------------------------#

# Titel:            dns_test.py
# Beschreibung:     Testen des schnellsten DNS-Servers
# Autor:            Hinrik Taeger
# Version:          1.0
# Kategorie:        Internet
# Probs:            The Morpheus Tutorial
# Ziel:             MacOS

# Eine Reihe von Seiten werden mit verschiedenen DNS-Diensten angesprochen.
# Die durchschnittliche Antwortzeit wird errechnet.
# Ein sortiertes Dictionary wird zurückgegeben, sowie der Beste DNS-Server

#----------------------------------------------------------------------------------------------------------------------#

#                           Importe
import dns.resolver
import time

#----------------------------------------------------------------------------------------------------------------------#

#                           Globale Variablen

# DNS-Dienste
dnsserver = ['1.1.1.1',
             '4.2.2.1',
             '8.8.8.8',
             '80.80.80.80',
             '208.67.222.123',
             '199.85.126.20',
             '185.228.168.168',
             '77.88.8.7',
             '176.103.130.132',
             '156.154.70.3',
             '8.26.56.26'
             ]

# Webseiten
domains = ['google.com',
           'amazon.com',
           'facebook.com',
           'the-morpheus.de'
           ]

#----------------------------------------------------------------------------------------------------------------------#

#                           Funktionen


# Funktion zum DNS-Test
def find_best_dns_server():
    results = {}
    for i in dnsserver:
        avg = 0
        for j in domains:
            try:
                resolv = dns.resolver.Resolver()
                resolv.nameservers = [i]
                start = time.time()
                result = resolv.query(j)
                end = time.time()
                avg += (end-start)
            except Exception:
                avg += 100000
        avg /= len(domains)
        # Alles in ein Dict packen
        results[i] = avg
    # Sortieren des Dicts nach den Values
    sorted_dns_server = sorted(results.items(), key=lambda x: x[1])
    # Erstellen des besten Ergebnisses
    best_result = "Best DNS-Server: " + sorted_dns_server[0][0] + "-- Responsetime: " + str(sorted_dns_server[0][1])
    # Rückgabe des Dictionaries und des besten Ergebnisses
    return sorted_dns_server, best_result

#----------------------------------------------------------------------------------------------------------------------#

#                           MAIN


if __name__ == '__main__':
    res, best = find_best_dns_server()
    print(res)
    print(best)
