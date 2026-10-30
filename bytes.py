# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:11:30 2026

@author: matos
"""




nbits=int(input("nbits:"))
nbytes=nbits / 8
nkbytes=nbytes/1024
nMbytes=nkbytes/1024

resto_1=int(nMbytes)
resto_2=int(nkbytes) % 1024
resto_3=int(nbytes) % 1024

print(f"{resto_1} Mbytes, {resto_2} Kbytes, {resto_3} bytes")


