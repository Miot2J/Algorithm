# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# ------
# input =
# 3
# 12:00 ~ 23:59
# 11:00 ~ 18:00
# 14:00 ~ 20:00

user_input = int(input())
timeLists = [list(input()) for _ in range(user_input)]
sh,sm,eh,em = 0,0,23,59
case = True

for i in range(len(timeLists)):
	timeLists[i] = ''.join(timeLists[i])
	tmp = timeLists[i].replace(":",' ')
	tmp = tmp.replace("~",'')
	nSh,nSm,nEh,nEm = map(int,tmp.split())
	# print(sh,sm,eh,em)
	# print("new",nSh,nSm,nEh,nEm)
	# 1 시간대가 겹치는지 판단
	if nSh > eh:
		case = False
		break
	if nSh == eh:
		if nSm > em:
			case =False
			break
		elif nSm == em:
			pass
		elif nSm < em:
			if nEm >= sm:
				em = sm
			else:
				case = False
	if nSh < eh:
		pass
	# 2 시작 시간은 둘중 큰쪽으로 초기화
	if nSh < sh:
		pass
	if nSh == sh:
		if nSm <= sm:
			pass
		elif nSm >= sm:
			sm = nSm
	if nSh > sh:
		sh = nSh
		sm = nSm
	# 3 마지막 시간은 작은쪽으로 초기화
	if nEh > eh:
		pass
	if nEh == eh:
		if nEm >= em:
			pass
		elif nEm <= em:
			if nEm <= sm:
				em = sm
			else:
				em = nEm
	if nEh < eh:
		eh = nEh
		em = nEm
	# print(timeLists[i])
# print(timeLists)
if (sh == eh and sm == em or case ==False):
	print(-1)
elif (sh == 0 or sm ==0 or eh ==0 or em ==0):
	if sh == 0:
		sh ="00"
	if sm == 0:
		sm ="00"
	if eh ==0:
		eh="00"
	if em ==0:
		em ="00"
	print(str(sh) + ":"+ str(sm),"~",str(eh) +":"+str(em))
else:
	print(str(sh) + ":"+ str(sm),"~",str(eh) +":"+str(em))
