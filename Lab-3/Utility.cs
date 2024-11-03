public class Utility
{
    public static void PrintBinary(string fileName)
    {
        var fileData = File.ReadAllBytes(fileName);
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