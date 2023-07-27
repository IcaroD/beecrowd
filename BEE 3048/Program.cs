class URI {

    static void Main(string[] args) { 

        int N = int.Parse(Console.ReadLine());

        int[] vet = new int[N];

        for (int i = 0; i < N; i++) 
        {
            vet[i] = int.Parse(Console.ReadLine());
        }

        int soma = 0;
        int atual = 0;
        for (int i = 0; i < N; i++)
        {
            if (vet[i] != atual)
            {
                soma++;
            }
            atual = vet[i];
        }

        Console.WriteLine(soma);

    }

}
