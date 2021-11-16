def fah_convert(cel):
    return ((9/5) * float(cel)) + 32

temperature = input("변환하고 싶은 섭씨 온도를 입력해 주세요:")
fah = fah_convert(temperature)
print("섭씨온도 :", float(temperature))
#string이 아닐 때 +로 출력하면 오류남
print(f'섭씨온도 : {temperature}')
print("화씨온도 : {0:.2f}".format(fah))
print(f"화씨온도 : {round(fah,2)}")
