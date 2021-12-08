text = "X-DSPAM-Confidence:    0.8475"
tex= text.find(':')
print (tex)
te=text[tex+2:]
print (te)
final = float(te)
print (final)

print ('done!!!')

#end
