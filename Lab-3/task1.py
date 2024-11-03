import struct 

signature = b'MYFORM' #ASCII

def encode(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    initial_size = len(data)

    version = 0
    header = struct.pack

     # Открываем выходной файл для записи
    with open(output_file, 'wb') as f:
        # Пишем сигнатуру
        f.write(signature)
        # Пишем версию в виде 16-битного целого числа (big-endian)
        f.write(struct.pack('>H', version))
        # Пишем длину исходного файла как 64-битное целое число (big-endian)
        f.write(struct.pack('>Q', initial_size))
        # Пишем сырые данные файла
        f.write(data)
    print(f"Файл '{input_file}' успешно закодирован в '{output_file}'.")

def decode(input_file, output_file):
    with open(input_file, 'rb') as f:
        signature = f.read(8)
        version = struct.unpack('>H', f.read(2))[0]
        initial_size = struct.unpack('>Q', f.read(8))[0]
        data = f.read()