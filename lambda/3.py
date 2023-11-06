# Given a list of strings, find all palindromes.

my_list = ["zeez", "haah", "hello", "world", "justtest", "pap"] 


result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))
print(result)


"""
filter ile her my_list elemanı üzerinde dönüm yaparız
ve her x değeri 
sırasıyla my_list'in bir elemanına eşlenir

reversed(x) ile o anki x'i ters çeviririz fakat bu bize parçalanmış bir çeviri yapar
yani örneğin x = zeez ise
reversed(x) = "z","e","e","z"

bu aradaki virgülleri de kaldırıp tek parça haline getirmek için "".join() kullanırız


sonra x'in ilk hali ile x'in son hali == ise result'a göndeririz

"""