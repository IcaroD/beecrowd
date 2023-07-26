class URI {

    static void Main(string[] args) { 

        int n = int.Parse(Console.ReadLine());

        int fatorial = 1;
        for (int i = 0; i < n; i++) 
        {
            fatorial *= (i + 1);
        }

        Console.WriteLine(fatorial);

    }

}
