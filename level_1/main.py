# http://www.pythonchallenge.com/pc/def/map.html

raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

from_chr = "abcdefghijklmnopqrstuvwxyz. ()'"
to_chr   = "cdefghijklmnopqrstuvwxyzab. ()'"

dic = dict(zip(from_chr, to_chr))

print(''.join(dic[x] for x in raw))