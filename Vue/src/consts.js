export const SETTINGS_FIELDS = { 
  WaterContainer1: [
    { name: 'Pow. przekroju poprz. zbiornika', initialValue: 1, units: 'm<sup>2</sup>', min: 0.5, max: 25, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Współczynnik wypływu', initialValue: 0.01, units: 'm<sup>5/2</sup>/s', min: 0.01, max: 0.25, interval: 0.01 },         //Beta - współczynnik odpływu?
    { name: 'Natężenie dopływu', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 0.5, interval: 0.01 },                  //Qd 
   // { name: 'Ciśnienie odpływu', initialValue: 0, units: 'm3' },               //Q0 - nieużywane 
    { name: 'Aktualny poziom cieczy', initialValue: 1, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //h
    { name: 'Maksymalny poziom cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //hMax
    { name: 'Okres próbkowania', initialValue: 1, units: 's', min: 0.1, max: 10, data: [0.01, 0.1, 1, 10] },                  //Tp - próbkowanie
    { name: 'Długość symulacji', initialValue: 1, units: 'h', min: 0.25, max: 24, interval: 0.25 },                 //SimulationLength - czas symulacji w godzinach
  ],
  WaterContainer2: [
    { name: 'Objętość zbiornika', initialValue: 1, units: 'm<sup>3</sup>', min: 0.5, max: 10, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Stężenie substancji', initialValue: 0, units: '%', min: 0.1, max: 100, interval: 0.1 },         //c
    { name: 'Natężenie dopływu składnika 1', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 0.5, interval: 0.01 },                  //Q1 
    { name: 'Natężenie dopływu składnika 2', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 0.5, interval: 0.01},        //Qd2
    { name: 'Natężenie odpływu', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 0.5, interval: 0.01 },        //Qo
    { name: 'Stężenie składnika 1', initialValue: 0, units: '%', min: 0, max: 100, interval: 0.1 },        //c1
    { name: 'Stężenie składnika 2', initialValue: 0, units: '%', min: 0, max: 100, interval: 0.1 },    //c2
    { name: 'Okres próbkowania', initialValue: 1, units: 's', min: 0.1, max: 10, data: [0.01, 0.1, 1, 10] },                  //Tp - próbkowanie
    { name: 'Długość symulacji', initialValue: 1, units: 'h', min: 0.25, max: 24, interval: 0.25 },                 //SimulationLength - czas symulacji w godzinach
  ],
  WaterContainer3: [
    { name: 'Pow. przekroju poprz. zbiornika', initialValue: 1, units: 'm<sup>2</sup>', min: 0.5, max: 25, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Współczynnik wypływu', initialValue: 0.01, units: 'm<sup>5/2</sup>/s', min: 0.01, max: 0.25, interval: 0.01 },         //Beta - współczynnik wypływu?
    { name: 'Aktualna wysokość poziomu wody', initialValue: 1, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //h
    { name: 'Maksymalny poziom cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //target_level
    
    // for recheck
    { name: 'Zadany poziom cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //target_level
    { name: 'Maksymalne natężenie dopływu', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 0.5, interval: 0.01 },         //max
    { name: 'Wzmocnienie regulatora', initialValue: 0.1, units: '', min: 0.1, max: 10, interval: 0.1 },    //P1
    { name: 'Czas zdwojenia regulatora', initialValue: 0.1, units: 's', min: 0.1, max: 100, interval: 0.1 },    //I1
    { name: 'Czas wyprzedzenia regulatora', initialValue: 0, units: 's', min: 0, max: 1, interval: 0.01 },    //D1
    //
    { name: 'Okres próbkowania', initialValue: 1, units: 's', min: 0.1, max: 10, data: [0.01, 0.1, 1, 10] },                  //Tp - próbkowanie
    { name: 'Długość symulacji', initialValue: 1, units: 'h', min: 0.25, max: 24, interval: 0.25 },                 //SimulationLength - czas symulacji w godzinach
  ],
  WaterContainer3_1: [
    { name: 'Pow. przekroju poprz. zbiornika', initialValue: 1, units: 'm<sup>2</sup>', min: 0.5, max: 25, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Współczynnik wypływu', initialValue: 0.01, units: 'm<sup>5/2</sup>/s', min: 0.01, max: 0.5, interval: 0.01 },         //Beta - współczynnik wypływu?
    { name: 'Aktualna wysokość poziomu wody', initialValue: 1, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //h
    { name: 'Maksymalny poziom cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //target_level
    
    // for recheck
    { name: 'Zadany poziom cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //target_level
    { name: 'Maksymalne natężenie dopływu', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 1, interval: 0.1 },         //max         //max
    { name: 'Wersja AI', units: '', initialValue: 0, data: {0:'Regresja', 1:'Genetyczna'} },                  //version
    //
    { name: 'Okres próbkowania', initialValue: 1, units: 's', min: 0.1, max: 10, data: [0.01, 0.1, 1, 10] },                  //Tp - próbkowanie
    { name: 'Długość symulacji', initialValue: 1, units: 'h', min: 0.25, max: 24, interval: 0.25 },                 //SimulationLength - czas symulacji w godzinach
  ],
  WaterContainer4: [
    { name: 'Objętość zbiornika', initialValue: 1, units: 'm<sup>3</sup>', min: 0.5, max: 10, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Początkowe stężenie substancji', initialValue: 0, units: '%', min: 0, max: 100, interval: 0.01 },         //c
    { name: 'Natężenie wpływu składnika 2', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 0.5, interval: 0.01},        //Qd2
    { name: 'Stężenie składnika 1', initialValue: 0, units: '%', min: 0, max: 100, interval: 0.1 },        //c1
    { name: 'Stężenie składnika 2', initialValue: 0, units: '%', min: 0, max: 100, interval: 0.1 },    //c2
    { name: 'Zadane stężenie', initialValue: 0.1, units: '%', min: 0, max: 100, interval: 0.1 },    //target_c
    { name: 'Wzmocnienie reg. dopł. strum. 1', initialValue: 0.1, units: '', min: 0.1, max: 10, interval: 0.1 },    //P1
    { name: 'Czas zdwojenia reg. dopł. strum. 1', initialValue: 0.1, units: 's', min: 0.1, max: 100, interval: 0.1 },    //I1
    { name: 'Czas wyprzedzenia reg. dopł. strum. 1', initialValue: 0, units: 's', min: 0, max: 1, interval: 0.01 },    //D1

    { name: 'Maksymalne natężenie dopływu', initialValue: 0.1, units: '', min: 0.1, max: 0.5, interval: 0.01 },    //maxinput
    { name: 'Objętość maksymalna cieczy', initialValue: 0.1, units: '', min: 0.1, max: 20, interval: 0.1 },    //vMax

    { name: 'Wzmocnienie reg. poziomu cieczy', initialValue: 0.1, units: '', min: 0.1, max: 10, interval: 0.1 },    //P2
    { name: 'Czas zdwojenia reg. poziomu cieczy', initialValue: 0.1, units: 's', min: 0.1, max: 100, interval: 0.1 },    //I2
    { name: 'Czas wyprzedzenia reg. poziomu cieczy', initialValue: 0, units: 's', min: 0, max: 100, interval: 0.01 },    //D2
    { name: 'Okres próbkowania', initialValue: 1, units: 's', min: 0.1, max: 10, data: [0.01, 0.1, 1, 10] },                  //Tp - próbkowanie
    { name: 'Długość symulacji', initialValue: 1, units: 'h', min: 0.25, max: 24, interval: 0.25 },                 //SimulationLength - czas symulacji w godzinach
  ],
  WaterContainer5: [
    { name: 'Pow. przekroju poprz. zbiornika', initialValue: 1, units: 'm<sup>2</sup>', min: 0.5, max: 10, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Współczynnik wypływu', initialValue: 0.1, units: 'm<sup>5/2</sup>/s', min: 0.1, max: 0.25, interval: 0.01 },         //Beta - współczynnik wypływu?
    { name: 'Maksymalne natężenie dopływu', initialValue: 0.1, units: 'm<sup>3</sup>/s', min: 0.1, max: 0.5, interval: 0.01 },                  //Qd 
    { name: 'Aktualny poziom cieczy', initialValue: 1, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //h
    { name: 'Maksymalna wysokość cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //hMax
    { name: 'Zadany poziom cieczy', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //hMax
    { name: 'Okres próbkowania', initialValue: 1, units: 's', data: [0.01, 0.1, 1, 10] },                  //Tp - próbkowanie
    { name: 'Długość symulacji', initialValue: 1, units: 'h', min: 0.25, max: 24, interval: 0.25 },                 //SimulationLength - czas symulacji w godzinach
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
