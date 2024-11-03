using System.Linq.Expressions;
using System.Text;

public class Task1
{
    public string Signature { get; set; }

    public long InitialLength { get; set; } = 0;
    public int Version { get; set; } = 1;

    public Task1(string startFileName, string encodedFileName, string DecodedFileName)
    {
        Signature = "MYSIGN";
        string folderName = "Task1/";
        Encode(folderName + startFileName, folderName + encodedFileName);
        Decode(folderName + encodedFileName, folderName + DecodedFileName);
        PrintEncoded(folderName + encodedFileName);

    }


    public void Encode(string inputFileName, string outputFileName)
    {
        byte[] fileData = File.ReadAllBytes(inputFileName);
        InitialLength = fileData.Length;
        Console.WriteLine("Длина исходного файла: " + InitialLength);
        byte[] SignatureByte = Encoding.ASCII.GetBytes(Signature);
        byte[] InitialLengthByte = BitConverter.GetBytes(InitialLength);
        byte[] VersionByte = BitConverter.GetBytes(this.Version);

        using (BinaryWriter writer = new BinaryWriter(File.Open(outputFileName, FileMode.OpenOrCreate)))
        {
            writer.Write(SignatureByte);
            writer.Write(InitialLengthByte);
            writer.Write(VersionByte);
            writer.Write(fileData);
        }
        Console.WriteLine($"Файл успешно закодирован в {outputFileName}.");
    }

    public void Decode(string inputFileName, string outputFileName)
    {
        using (BinaryReader reader = new BinaryReader(File.Open(inputFileName, FileMode.Open)))
        {
            var CurrentSignature = Encoding.ASCII.GetString(reader.ReadBytes(6));
            if (Signature != CurrentSignature)
            {
                throw new Exception("Некорректная сигнатура файла");
            }

            InitialLength = BitConverter.ToInt64(reader.ReadBytes(8));
            var CurrentVersion = BitConverter.ToInt32(reader.ReadBytes(4));
            if (CurrentVersion != Version)
            {
                throw new Exception("Некорректная версия файла");
            }
            byte[] fileData = reader.ReadBytes((int)InitialLength);
            File.WriteAllBytes(outputFileName, fileData);
        }
        Console.WriteLine($"Файл успешно раскодирован в {outputFileName} .");

    }

    public void PrintEncoded(string encodedFileName)
    {
        var fileData = File.ReadAllBytes(encodedFileName);
        int stringsNumber = fileData.Length / 4;
        for (int i = 0; i < stringsNumber; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                var currentByte = fileData[i * 4 + j];

                Console.Write(Convert.ToString(currentByte, 2).PadLeft(8, '0') + " ");
            }
            Console.WriteLine();
        }
    }

}