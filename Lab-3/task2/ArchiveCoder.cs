using System.Text;

public class ArchiveCoder : Coder
{
    private byte CompressionAlgorithmWithContext = 0; // Код сжатия с учетом контекста
    private byte CompressionAlgorithmWithoutContext = 0; // Код сжатия без учета контекста
    private byte ErrorCorrectionCode = 0; // Код защиты от помех ?

    public ArchiveCoder(string signature, byte version, byte compressionAlgorithmWithContext, byte compressionAlgorithmWithoutContext, byte errorCorrectionCode)
    : base(signature, version)
    {
        CompressionAlgorithmWithContext = compressionAlgorithmWithContext;
        CompressionAlgorithmWithoutContext = compressionAlgorithmWithoutContext;
        ErrorCorrectionCode = errorCorrectionCode;
    }


    public override void Encode(string inputFileName, string outputFileName)
    {
        byte[] fileData = File.ReadAllBytes(inputFileName);
        InitialLength = fileData.Length;
        using (BinaryWriter writer = new BinaryWriter(File.Open(outputFileName, FileMode.Create)))
        {
            writer.Write(Encoding.ASCII.GetBytes(Signature));
            writer.Write(Version);
            writer.Write(CompressionAlgorithmWithContext);
            writer.Write(CompressionAlgorithmWithoutContext);
            writer.Write(ErrorCorrectionCode);
            writer.Write(BitConverter.GetBytes(InitialLength));
            writer.Write(fileData);
        }
        Console.WriteLine($"Заголовки успешно записаны в {outputFileName}.");
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

            var currentVersion = reader.ReadBytes(1)[0];
            if (currentVersion != Version)
            {
                throw new Exception("Некорректная версия файла");
            }
            CompressionAlgorithmWithContext = reader.ReadBytes(1)[0];
            CompressionAlgorithmWithoutContext = reader.ReadBytes(1)[0];
            ErrorCorrectionCode = reader.ReadBytes(1)[0];
            InitialLength = BitConverter.ToInt32(reader.ReadBytes(4));
            byte[] fileData = reader.ReadBytes((int)InitialLength);
            File.WriteAllBytes(outputFileName, fileData);
        }
        Console.WriteLine($"Файл успешно раскодирован в {outputFileName} .");
    }

}