export const SETTINGS_FIELDS = [
    { name: 'Wysokość', value: 10, units: 'm' },
    { name: 'Szybkość', value: 20, units: 's' },
    { name: 'Objętość', value: 0, units: 'm3' },
];

export const CHARTS_SETTINGS = {
    1: {
        labels: [1, 2, 3, 4, 5],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [1, 10, 1, 24, 25]
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
