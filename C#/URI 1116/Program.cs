class URI {

    static void Main(string[] args) { 

        int n = int.Parse(Console.ReadLine());

        for (int i = 0; i < n; i++) 
        {
            string[] dados = Console.ReadLine().Split(' ');
            int x = int.Parse(dados[0]);
            int y = int.Parse(dados[1]);

            if (y == 0)
            {
                Console.WriteLine("divisao impossivel");
            }
            else
            {
                double divisao = (double)x / y;

                Console.WriteLine($"{divisao}");
            }
        }

    }

}