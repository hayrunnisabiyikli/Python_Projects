for i in range(1, 20):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Algoritma oldukça basit. 3 ile tam bölünebilen sayılar için Fizz, 5 ile tam bölünebilen
# sayılar için Buzz, hem 3 hem 5 ile tam bölünebilen sayılar için FizzBuzz yazılması
# isteniyor. Dizideki diğer sayılar içinse sayının kendisi yazılmalı.
# Pek tabii bu pratiği TDD felsefesi ile geliştirmemiz bekleniyor.