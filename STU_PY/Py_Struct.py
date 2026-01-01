# c언어의 구조체를 읽어 오는 것

# 아래와 같은 c언어 프로그램 작성
#include <stdio.h>
# typedef struct { 
#     double v; 
#     int t; 
#     char c;
# } save_type;

# int main() {
#     save_type s = {7.5f, 15, 'A'};
#     FILE *f = fopen("output", "w");
#     fwrite(&s, sizeof(save_type), 1, f);
#     fclose(f);
#     return 0;
# }

import struct

# dicccc -> double 1개, int-1개, char-4개의 의미
# 구조체는 double-8바이트, int-4바이트, char-1바이트 인데 왜 16바이트로 읽어야 하면
# c구조체의 전체 크기는 가장 큰 바이트의 2배이기 때문에!!!!!
with open('../output', 'rb') as f:
    chunk = f.read(16)
    result = struct.unpack('dicccc', chunk)
    
    for item in result:
        if item:
            item = str(item).replace("b\'\\x00'","") # 바이트 의미 없는 문자를 치완해야 한다.
            if len(item) > 0:
                item = item.replace("b\'","").replace("'","")
                print(item)

    
        