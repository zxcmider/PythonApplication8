using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp1
{
    class Inimene
    {
        string perenimi;
        public string Status;
        public int eesnimi;
        public int shirina;
        public int vaanus;
        public int palk;
        public Inimene() { }
        
        public Inimene(string Perenimi)
        {
            perenimi = Perenimi;
        }
        public Inimene(int Nimi, string Perenimi)

        {
            eesnimi = Nimi;
            perenimi = Perenimi;
        }
        public int Eesnimi
        {
            set { eesnimi = value; }
            get { return eesnimi; }
        }
        public string Perenimi
        {
            set { if (perenimi == null) perenimi = value; }
            get { return perenimi; }
        }
        public int Vanus
        {
            set
            {
                Vanus = value;
                if (Vanus < 7)
                {
                    Status = "Laps";
                }
                else if (Vanus < 17)
                {
                    Status = "Koolilaps";
                }
                else if (Vanus < 24)
                {
                    Status = "Ulikooli laps";
                }
                else
                {
                    Status = "Tööline";
                }
            }
            get { return Vanus; }
        }

     
        public void Tervitamine() 
        {
        Console.WriteLine("Minu perenimi on" + perenimi);
        Console.WriteLine("Ma olen {0} aastat vana, olen {1}",vaanus,Status);
        Console.WriteLine("Minu eesnimi on {0}",eesnimi);
        }
    }
}



________________________________________________
using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Inimene naine = new Inimene("Kask");
            naine.Vanus = int.Parse(Console.ReadLine());
            naine.Tervitamine();

            Inimene mees = new Inimene();
            mees.Perenimi = "Logopov";
            mees.Vanus = 45;
            Console.WriteLine(mees.Perenimi,"on",mees.Vanus,"aastane mees");
            mees.Tervitamine();

            Inimene[] Inimesed = new Inimene[5]; 
            for (int i = 0; i < 5; i++)
            {
                Inimesed[i] = new Inimene();
                Console.WriteLine("Mis on sinu nimi");
                Inimesed[i].Perenimi = Console.ReadLine();
                Inimesed[i].Vanus = int.Parse(Console.ReadLine());
            }
            foreach (Inimene inimene in Inimesed)
            {
                inimene.Tervitamine();
            }   

            Console.ReadKey();
        }
    }
}
