import os

def main():
  i = 1
  path = input('Enter directory path: ')
  output_name = input('Enter new name for files: ')
  output_file_ext = input('Enter output file extension: ')

  for filename in os.listdir(path):
    output = f'{path}{output_name}{i}{output_file_ext}'
    source = path + filename
    os.rename(source, output)
    i += 1

if __name__ == '__main__':
   main()