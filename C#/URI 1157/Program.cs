class URI {

    static void Main(string[] args) { 

        int n = int.Parse(Console.ReadLine());

        for (int i = 0; i < n; i++) 
        {
            double quadrado = Math.Pow(i+1, 2);
            double cubo = Math.Pow(i+1, 3);

            Console.WriteLine($"{i+1} {quadrado} {cubo}");
        }

    }

}