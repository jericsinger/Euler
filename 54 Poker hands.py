def get_hands():
	import urllib2
	response = urllib2.urlopen('http://projecteuler.net/project/poker.txt')
	hands = []
	for line in response:
		hand = response.readline()
		hand = hand.rstrip('\r\n')
		hands.append([hand[:14], hand[15:]])
	return hands


def poker(hands):
    scores = [(i, score(hand.split())) for i, hand in enumerate(hands)]
    winner = sorted(scores , key=lambda x:x[1])[-1][0]
    return hands[winner]

def score(hand):
    ranks = '23456789TJQKA'
    rcounts = {ranks.find(r): ''.join(hand).count(r) for r, _ in hand}.items()
    score, ranks = zip(*sorted((cnt, rank) for rank, cnt in rcounts)[::-1])
    if len(score) == 5:
        if ranks[0:2] == (12, 3): #adjust if 5 high straight
            ranks = (3, 2, 1, 0, -1)
        straight = ranks[0] - ranks[4] == 4
        flush = len({suit for _, suit in hand}) == 1
        '''no pair, straight, flush, or straight flush'''
        score = ([1, (3,2,0)], [(3,2,1), 5])[flush][straight]
    return score, ranks


def euler54():
	hands = get_hands()
	print len(hands)
	win_count = [0, 0]
	wins = 0
	for hand in hands:
		winner = 'p1'
		winning_hand = poker(hand)
		if winning_hand == hand[0]:
			win_count[0] += 1
		else:
			win_count[1] += 1
			winner = 'p2'
		print hand
		print "%s wins with: %s" % (winner, winning_hand)


euler54()