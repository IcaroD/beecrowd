class URI {

    static void Main(string[] args) { 

        int N = int.Parse(Console.ReadLine());

        int[] vet = new int[N + 1];

        for (int i = 0; i < N; i++) 
        {
            vet[i] = int.Parse(Console.ReadLine());
        }

        int soma = 0;
        for (int i = 1; i < N; i++)
        {
            if (vet[i] != vet[i-1])
            {
                soma += vet[i];
            }
        }
        
        if (soma > 7)
        {
            soma = 7;
        }

        Console.WriteLine(soma);

    }

}
