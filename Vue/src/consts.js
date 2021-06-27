export const SETTINGS_FIELDS = { 
  WaterContainer1: [
    { name: 'Pow. przekroju poprz. zbiornika', initialValue: 1, units: 'm<sup>2</sup>', min: 0.5, max: 25, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Współczynnik wypływu', initialValue: 0.01, units: '', min: 0.01, max: 5, interval: 0.01 },         //Beta - współczynnik wypływu?
    { name: 'Natężenie dopływu', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 5, interval: 0.01 },                  //Qd 
   // { name: 'Ciśnienie wypływu', initialValue: 0, units: 'm3' },               //Q0 - nieużywane 
    { name: 'Aktualny poziom cieczy', initialValue: 1, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //h
    { name: 'Maksymalny poziom cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //hMax
    { name: 'Próbkowanie', initialValue: 1, units: '', min: 0.1, max: 10, data: [0.01, 0.1, 1] },                  //Tp - próbkowanie
    { name: 'Częstotliwość próbkowania', initialValue: 1, units: 'h', min: 0.25, max: 24, interval: 0.25 },                 //SimulationLength - czas symulacji w godzinach
  ],
  WaterContainer2: [
    { name: 'Objętość zbiornika', initialValue: 1, units: 'm<sup>2</sup>', min: 0.5, max: 10, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Stężenie substancji', initialValue: 0.1, units: '%', min: 0.1, max: 1, interval: 0.01 },         //c
    { name: 'Natężenie dopływu składnika 1', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 10, interval: 0.1 },                  //Q1 
    { name: 'Natężenie dopływu składnika 2', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 10, interval: 0.1},        //Qd2
    { name: 'Natężenie wypływu', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 20, interval: 0.1 },        //Qo
    { name: 'Stężenie składnika 1', initialValue: 0.1, units: '%', min: 0.1, max: 1, interval: 0.01 },        //c1
    { name: 'Stężenie składnika 2', initialValue: 0.1, units: '%', min: 0.1, max: 1, interval: 0.01 },    //c2
    { name: 'Częstotliwość próbkowania', initialValue: 1, units: '', min: 0.1, max: 10, data: [0.01, 0.1, 1] },                  //Tp - próbkowanie
    { name: 'Czas symulacji', initialValue: 1, units: 'h', min: 0.25, max: 24, interval: 0.25 },                 //SimulationLength - czas symulacji w godzinach
  ],
  WaterContainer3: [
    { name: 'Pow. przekroju poprz. zbiornika', initialValue: 1, units: 'm<sup>2</sup>', min: 0.5, max: 25, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Współczynnik wypływu', initialValue: 0.01, units: '', min: 0.01, max: 5, interval: 0.01 },         //Beta - współczynnik wypływu?
    { name: 'Natężenie dopływu', initialValue: 0.01, units: 'm<sup>3</sup>/s', min: 0, max: 5, interval: 0.01 },                  //Qd 
    { name: 'Aktualna wysokość poziomu wody', initialValue: 1, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //h
    { name: 'Maksymalny poziom cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //target_level
    
    // for recheck
    { name: 'Zadany poziom cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //target_level
    { name: 'Maksymalne natężenie dopływu', initialValue: 0.1, units: '', min: 0.1, max: 5, interval: 0.1 },         //max
    { name: 'Część proporcjonalna PID-1', initialValue: 0.1, units: '', min: 0.1, max: 10, interval: 0.1 },    //P1
    { name: 'Część całkująca PID-1', initialValue: 0.1, units: '', min: 0.1, max: 100, interval: 0.1 },    //I1
    { name: 'Część różniczkująca PID-1', initialValue: 0.1, units: '', min: 0.01, max: 1, interval: 0.01 },    //D1
    //
    { name: 'Częstotliwość próbkowania', initialValue: 1, units: '', min: 0.1, max: 10, data: [0.01, 0.1, 1] },                  //Tp - próbkowanie
    { name: 'Czas symulacji', initialValue: 1, units: 'h', min: 0.25, max: 24, interval: 0.25 },                 //SimulationLength - czas symulacji w godzinach
  ],
  WaterContainer3_1: [
    { name: 'Pow. przekroju poprz. zbiornika', initialValue: 1, units: 'm<sup>2</sup>', min: 0.5, max: 25, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Współczynnik wypływu', initialValue: 0.01, units: '', min: 0.01, max: 5, interval: 0.01 },         //Beta - współczynnik wypływu?
    { name: 'Natężenie dopływu', initialValue: 0.01, units: 'm<sup>3</sup>/s', min: 0, max: 5, interval: 0.01 },                  //Qd 
    { name: 'Aktualna wysokość poziomu wody', initialValue: 1, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //h
    { name: 'Maksymalny poziom cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //target_level
    
    // for recheck
    { name: 'Zadany poziom cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //target_level
    { name: 'Maksymalne natężenie dopływu', initialValue: 0.1, units: '', min: 0.1, max: 5, interval: 0.1 },         //max         //max
    { name: 'Wersja AI', units: '', initialValue: 0, data: {0:'Regresja', 1:'Genetyczna'} },                  //version
    //
    { name: 'Częstotliwość próbkowania', initialValue: 1, units: '', min: 0.1, max: 10, data: [0.01, 0.1, 1] },                  //Tp - próbkowanie
    { name: 'Czas symulacji', initialValue: 1, units: 'h', min: 0.25, max: 24, interval: 0.25 },                 //SimulationLength - czas symulacji w godzinach
  ],
  WaterContainer4: [
    { name: 'Pow. przekroju poprz. zbiornika', initialValue: 1, units: 'm<sup>2</sup>', min: 0.5, max: 10, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Stężenie substancji', initialValue: 0.1, units: '%', min: 0.1, max: 1, interval: 0.01 },         //c
    { name: 'Natężenie dopływu składnika 1', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 10, interval: 0.1 },                  //Q1 
    { name: 'Natężenie wpływu składnika 2', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 10, interval: 0.1},        //Qd2
    { name: 'Natężenie wypływu', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 20, interval: 0.1 },        //Qo
    { name: 'Stężenie składnika 1', initialValue: 0.1, units: '%', min: 0.1, max: 1, interval: 0.01 },        //c1
    { name: 'Stężenie składnika 2', initialValue: 0.1, units: '%', min: 0.1, max: 1, interval: 0.01 },    //c2
    { name: 'Zadane stężenie', initialValue: 0.1, units: '%', min: 0, max: 1, interval: 0.01 },    //target_c
    { name: 'Część proporcjonalna PID-1', initialValue: 0.1, units: '', min: 0.1, max: 10, interval: 0.1 },    //P1
    { name: 'Część całkująca PID-1', initialValue: 0.1, units: '', min: 0.1, max: 100, interval: 0.1 },    //I1
    { name: 'Część różniczkująca PID-1', initialValue: 0.1, units: '', min: 0.01, max: 1, interval: 0.01 },    //D1

    { name: 'Maksymalne natężenie dopływu', initialValue: 0.1, units: '', min: 0.1, max: 5, interval: 0.1 },    //maxinput
    { name: 'Wysokość maksymalna cieczy', initialValue: 0.1, units: '', min: 0.1, max: 20, interval: 0.1 },    //vMax

    { name: 'Część proporcjonalna PID-2', initialValue: 0.1, units: '', min: 0.1, max: 100, interval: 0.1 },    //P2
    { name: 'Część całkująca PID-2', initialValue: 0.1, units: '', min: 0.1, max: 100, interval: 0.1 },    //I2
    { name: 'Część różniczkująca PID-2', initialValue: 0.1, units: '', min: 0.1, max: 100, interval: 0.1 },    //D2
    { name: 'Częstotliwość próbkowania', initialValue: 1, units: '', min: 0.1, max: 10, data: [0.01, 0.1, 1] },                  //Tp - próbkowanie
    { name: 'Czas symulacji', initialValue: 1, units: 'h', min: 0.25, max: 24, interval: 0.25 },                 //SimulationLength - czas symulacji w godzinach
  ],
  WaterContainer5: [
    { name: 'Pow. przekroju poprz. zbiornika', initialValue: 1, units: 'm<sup>2</sup>', min: 0.5, max: 10, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Współczynnik wypływu', initialValue: 0.01, units: '', min: 0.01, max: 0.5, interval: 0.01 },         //Beta - współczynnik wypływu?
    { name: 'Maksymalne natężenie dopływu', initialValue: 0.01, units: 'm<sup>3</sup>/s', min: 0.1, max: 5, interval: 0.1 },                  //Qd 
    { name: 'Aktualny poziom cieczy', initialValue: 1, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //h
    { name: 'Maksymalna wysokość cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //hMax
    { name: 'Zadany poziom cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //hMax
    { name: 'Częstotliwość próbkowania', initialValue: 1, units: '', data: [0.01, 0.1, 1] },                  //Tp - próbkowanie
    { name: 'Czas symulacji', initialValue: 1, units: 'h', min: 0.25, max: 24, interval: 0.25 },                 //SimulationLength - czas symulacji w godzinach
  ]

};
//A, Beta, Qd, H, Tp, SimulationLength, hMax
export const CHARTS_SETTINGS = {
    1: {
        labels: [1, 2, 3, 4, 5, 4],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [1, 10, 1, 24, 25, 34, 34, 34,35]
          },
        ], 
    },
    2: {
        labels: [1, 10, 20, 30, 40, 50],
        datasets: [
          {
            label: 'Data Two',
            backgroundColor: '#f836a2',
            data: [1, 10, 177, 245, 251, 362]
          },
        ],
    }
};
