
//Задание 1
Console.WriteLine("Задание 1");
var task1Coder = new SimpleCoder("MYSIGN", 1);
task1Coder.Code("task1/start.txt", "task1/encoded.mysign", "task1/decoded.txt");
Utility.PrintBinary("task1/encoded.mysign");
Console.WriteLine("-----------------------------------------");
Console.WriteLine();



//Задание 2-3
Console.WriteLine("Задание 2-3");
var task3Coder = new ArchiveCoder("MYSIGN", 1, 0, 0, 0);
task3Coder.Code("task1/start.txt", "task2/archive.mysign", "task2/decoded.txt");
Utility.PrintBinary("task2/archive.mysign");

