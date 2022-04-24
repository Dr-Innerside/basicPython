# 예제 1번.
# sparta 문자열 중 spa만 나오게 하기
text = 'sparta'
result = text[:3]
# print(result)


# 예제 2번.
# 02-1234-5678 문자열 중 02만 나오게 하기
phone = '02-1234-5678'
result = phone.split('-')[0]
# print(result)

# 예제 3번.
# 반복문 enmerate와 break
people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]
for i, person in enumerate(people):
    name = person['name']
    age = person['age']
    # print(i, name, age)
    if i > 2:
        break

# 예제 4번.
# 짝수만 출력
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
count = 0
sum = 0
max = 0
for num in num_list:
    if num % 2 == 0:
        # print(num)

        # 예제 5.
        # 짝수의 갯수 구하기
        count += 1

        # print(count)

        # 예제 6.
        # 리스트 안의 모든 숫자 더하기
        sum += num

        # print(sum)

        # 예제 7.
        # 리스트 안의 가장 큰 숫자 구하기
        if num > max:
            max = num


# print(max)


# 예제 8.
# 주민등록번호 뒤 부분 첫자리가 홀수면 남자, 짝수면 여자 출력
def is_gender(number):
    # print('주민등록번호 조회 : ',number)
    if int(number.split('-')[1][:1]) % 2 == 1:
        return '남성입니다'
    else:
        return '여성입니다'


id_number = '941025-1555111'
id_number2 = '941025-2555333'
id_number3 = '941024-4555444'
result = is_gender(id_number3)
# print(result)

# 집합 자료형
a = [1, 2, 3, 4, 5, 1, 2, 3]
b = [5, 6, 7, 8, 9, 5, 6, 7]
# print('a: ',set(a), 'b: ',set(b))
c = set(a) & set(b)
d = set(a) - set(b)
e = set(a) | set(b)
# print(c,d,e)

# f-string
scores = [
    {'name': '영수', 'score': 70},
    {'name': '영희', 'score': 65},
    {'name': '기찬', 'score': 75},
    {'name': '희수', 'score': 23},
    {'name': '서경', 'score': 99},
    {'name': '미주', 'score': 100},
    {'name': '병태', 'score': 32}
]
for s in scores:
    name = s['name']
    score = s['score']
    # print(name+' 의 점수는 '+str(score)+' 점 입니다')
    # print(f'{name}(이)의 점수는 {str(score)}점 입니다!!!')

people1 = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]
for s in people1:

    # print(name, age)
    #  예외처리
    try:
        if s['age'] < 20:
            print(s['name'])
    except:
        print(s['name']+': Error')

a_list = [1,3,5,7,9]
b_list =[a*2 for a in a_list]
print(b_list)

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

def is_adult(person):
    return ('성인' if person['age']< 20 else '미성년')

result = map(is_adult, people)
print(list(result))

result = map(lambda person: ('성인' if person['age']< 20 else '미성년'), people)

result = filter(lambda person: person['age']>20, people)
print(list(result))

class Monster():
    hp = 100
    alive = True

    def damage(self, attack):
        self.hp = self.hp - attack
        if self.hp == 0:
            self.alive = False

    def status(self):
        if self.alive:
            print('살아있음')
        else:
            print('죽었음')


m1 = Monster()
m1.damage(150)
m1.status()