using System.Linq.Expressions;
using System.Text;

public abstract class Coder
{
    public string Signature { get; set; }
    public int InitialLength { get; set; } = 0;
    public byte Version { get; set; } = 1;

    public Coder(string signature, byte version)
    {
        Signature = signature;
        Version = version;

    }

    public void Code(string startFileName, string encodedFileName, string decodedFileName)
    {
        Encode(startFileName, encodedFileName);
        Decode(encodedFileName, decodedFileName);
    }
    public abstract void Encode(string inputFileName, string outputFileName);

    public abstract void Decode(string inputFileName, string outputFileName);


}