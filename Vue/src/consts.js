export const SETTINGS_FIELDS = [
    { name: 'Powierzchnia zbiornika', initialValue: 1, units: 'm2', min: 0.5, max: 10, interval: 0.1 },           //A - powierzchnia zbiornika
    { name: 'Współczynnik przepływu', initialValue: 0.01, units: 'none', min: 0.001, max: 0.5, interval: 0.001 },         //Beta - współczynnik wypływu?
    { name: 'Ciśnienie wpływu', initialValue: 0.01, units: 'm^3/s', min: 0.01, max: 1, interval: 0.01 },                  //Qd 
   // { name: 'Ciśnienie wypływu', initialValue: 0, units: 'm3' },               //Q0 - nieużywane 
    { name: 'Aktualna wysokość poziomu wody', initialValue: 1, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //h
    { name: 'Maksymalna wysokość zbiornika', initialValue: 5, units: 'm', min: 0.1, max: 20, interval: 0.1 },        //hMax
    { name: 'Próbkowanie', initialValue: 1, units: 'none', min: 1, max: 10, data: [0.01, 0.1, 1] },                  //Tp - próbkowanie
    { name: 'Czas symulacji', initialValue: 1, units: 'h', min: 0.5, max: 24, interval: 0.5 },                 //SimulationLength - czas symulacji w godzinach
];
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
