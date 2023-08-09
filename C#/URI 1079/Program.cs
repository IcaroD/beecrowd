using System.Globalization;

class URI {

    static void Main(string[] args) { 

        int n = int.Parse(Console.ReadLine());

        for (int i = 0; i < n; i++) 
        {
            string[] dados = Console.ReadLine().Split(' ');
            double value1 = int.Parse(dados[0]);
            double value2 = int.Parse(dados[1]);
            double value3 = int.Parse(dados[2]);

            double media = (value1 * 2 + value2 * 3 + value3 * 5) / 10;

            Console.WriteLine(media.ToString("F2"));
        }

    }

}
