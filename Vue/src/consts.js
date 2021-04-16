export const SETTINGS_FIELDS = [
    { name: 'Powierzchnia zbiornika', value: 10, units: 'm2' },           //A
    { name: 'Współczynnik przepływu', value: 20, units: 'none' },         //Beta
    { name: 'Ciśnienie wpływu', value: 0, units: '?' },                  //Qd 
   // { name: 'Ciśnienie wypływu', value: 0, units: 'm3' },               //Q0 - nieużywane 
    { name: 'Próbkowanie', value: 0, units: 'none' },                        //Tp
    { name: 'Maksymalna wysokość zbiornika', value: 0, units: 'm' },        //hMax
    { name: 'Aktualna wysokość poziomu wody', value: 0, units: 'm' },        //hMax
    { name: 'Czas symulacji', value: 0, units: 'h' },                 //SimulationLength
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
