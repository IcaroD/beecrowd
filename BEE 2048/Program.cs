class URI {

    static void Main(string[] args) { 

        int N = int.Parse(Console.ReadLine());

        int[] vet = new int[N + 1];

        int soma = -1;
        vet[0] = 1;
        for (int i = 1; i <= N; i++)
        {
            vet[i] = int.Parse(Console.ReadLine());

            if (vet[i] == vet[i-1] && soma <= 7)
            {
                soma += vet[i];
            }
            else if (vet[i] != vet[i-1] && vet[i-1] == vet[i-2] && soma <= 7)
            {
                soma += vet[i-1];
            }
        }

        if (soma > 7)
            {
                soma = 7;
            }
        else if (soma < 3)
        {
            soma = 3;
        }

        Console.WriteLine(soma);

    }

}
