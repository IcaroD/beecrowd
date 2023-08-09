using System.Data;

class URI {

    static void Main(string[] args) { 

        int dentro, fora;

        int n = int.Parse(Console.ReadLine());

        int[] x = new int[n];

        for (int i = 0; i < n; i++) 
        {
            x[i] = int.Parse(Console.ReadLine());
        }

        dentro = 0;
        fora = 0;
        for (int i = 0; i < n; i++)
        {
            if (x[i] >= 10 && x[i] <= 20)
            {
                dentro++;
            }
            else
            {
                fora++;
            }
        }

        Console.WriteLine($"{dentro} in");
        Console.WriteLine($"{fora} out");

    }

}