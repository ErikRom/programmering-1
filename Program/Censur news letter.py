letter = "Be not alarmed, madam, on receiving this letter, by the apprehension of its containing any repetition of those sentiments or renewal of those offers which were last night so disgusting to you. I write without any intention of paining you, or humbling myself, by dwelling on wishes which, for the happiness of both, cannot be too soon forgotten: and the effort which the formation and the perusal of this letter must occasion, should have been spared had not my character required it to be written and read. You must, therefore, pardon the freedom with which I demand your attention; your feelings, I know, will bestow it unwillingly, but I demand it of your justice." and "Two offenses of a very different nature, and by no means of equal magnitude, you last night laid to my charge. The first-mentioned was, that, regardless of the sentiments of either, I had detached Mr. Bingley from your sister,- and the other, that I had, in defiance of various claims, in defiance of honor and humanity, ruined the immediate prosperity and blasted the prospects of Mr. Wickham.- Willfully and wantonly to have thrown off the companion of my youth, the acknowledged favorite of my father, a young man who had scarcely any other dependence than on our patronage, and who had been brought up to expect its exertion, would be a depravity, to which the separation of two young persons, whose affection could be the growth of only a few weeks, could bear no comparison. But from the severity of that blame which was last night so liberally bestowed, respecting each circumstance, I shall hope to be in future secured, when the following account of my actions and their motives has been read. If, in the explanation of them, which is due to myself, I am under the necessity of relating feelings which may be offensive to yours, I can only say that I am sorry. The necessity must be obeyed, and further apology would be absurd."




#words_to_pass = ["I", "a", "on", "letter"]
#letter = letter.split()
#censored_output = ""
#for word in letter:
 #   if word in words_to_pass:
  #      censored_output += word
 #   elif word[-1] == "," and word[:len(word)-1] in words_to_pass:
   #     censored_output += "*" * (len(word)-1) + "*"
    #else:
     #   censored_output += "*" * len(word)
      #  censored_output += "*" * len(word)
       # censored_output += " "
#print(censored_output)


tillåtna = ["I", "a", ",", "on", "letter"]

for i in letter:
    if tillåtna[0] in i or tillåtna[1] in i or tillåtna[2] in i:
        print(i)
    if tillåtna[0] nt in i or tillåtna[1] not in i or tillåtna[2]  not in i:
        i = i.replcae(i, "*")

        print(i)

for i in range(0, 5):
    if tillåtna[i] not in x:
        x = x.replace(x, tillåtna[i])


#if x != tillåtna:
 #   x = x.replace(x, "*")

#print(x)
