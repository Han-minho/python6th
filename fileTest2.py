import os

# filename = "example.txt"
# print("파일이 존재하는지 확인하기")
# if os.path.isfile(filename):
#     print(f"{filename}이 존재합니다.")
# else:
#     print(f"f{filename}이 없습니다.")

# file_object = open('list_example.txt','w')
# content_list = ["Python","Java","C++","JavaScript"]
# for item in content_list:
#         file_object.write(item + '\n')
#
# file_object.close()

#현재 작업 위치 확인하기
current_directory = os.getcwd()
print(current_directory)

# 파일 생성
# os.mkdir('new_directory')

# 파일 중첩 생성
# os.makedirs('parent_directory/child_directory/grandchild_directory')

# os.chdir('new_directory')
# current_directory2 = os.getcwd()
# print(current_directory2)

# with open('example.txt','w') as file_object:
#     file_object.write("Hello, World")
#
# print("done")

# os.rename("old_directory",'new_directory')

# os.rmdir('new_directory')
#os.removedirs('parent_directory/child_directory/grandchild_directory1/2/3/4/5')

current_directory2 = os.getcwd()
print(current_directory2)

for dirpath, dirnames,filenames in os.walk('parent_directory'):
    print(f"디렉토리 경로 : {dirpath}")
    print(f"디렉토리 이름 : {dirnames}")
    print(f"파일 이름 : {filenames}")