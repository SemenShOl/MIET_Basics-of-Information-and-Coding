using System.Linq.Expressions;
using System.Text;

public class SimpleCoder : Coder
{

    public SimpleCoder(string signature, byte version) :
    base(signature, version)
    { }

    public override void Encode(string inputFileName, string outputFileName)
    {
        byte[] fileData = File.ReadAllBytes(inputFileName);
        InitialLength = fileData.Length;
        Console.WriteLine("Длина исходного файла: " + InitialLength);
        byte[] SignatureByte = Encoding.ASCII.GetBytes(Signature);
        byte[] InitialLengthByte = BitConverter.GetBytes(InitialLength);

        using (BinaryWriter writer = new BinaryWriter(File.Open(outputFileName, FileMode.Create)))
        {
            writer.Write(SignatureByte);
            writer.Write(this.Version);
            writer.Write(InitialLengthByte);

            writer.Write(fileData);
        }
        Console.WriteLine($"Файл успешно закодирован в {outputFileName}.");
    }

    public override void Decode(string inputFileName, string outputFileName)
    {
        using (BinaryReader reader = new BinaryReader(File.Open(inputFileName, FileMode.Open)))
        {
            var CurrentSignature = Encoding.ASCII.GetString(reader.ReadBytes(6));
            if (Signature != CurrentSignature)
            {
                throw new Exception("Некорректная сигнатура файла");
            }

            var CurrentVersion = reader.ReadBytes(1)[0];
            if (CurrentVersion != Version)
            {
                throw new Exception("Некорректная версия файла");
            }
            InitialLength = BitConverter.ToInt32(reader.ReadBytes(4));

            byte[] fileData = reader.ReadBytes((int)InitialLength);
            File.WriteAllBytes(outputFileName, fileData);
        }
        Console.WriteLine($"Файл успешно раскодирован в {outputFileName} .");

    }


}