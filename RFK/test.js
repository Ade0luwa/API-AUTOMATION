const axios = require('axios');
const { callApi, statusResponse } = require('./start_stop_api.js'); // Replace with your actual module name

jest.mock('axios');

const runTestSuiteMultipleTimes = (times, testSuite) => {
    for (let i = 0; i < times; i++) {
        describe(`Iteration ${i + 1}`, () => {
            testSuite(i + 1);
        });
    }
};

const testSuite = (iteration) => {
    const stopmain = 'http://172.16.121.166:5000/api/v1/outputs/DAN-OUT-1/stop';
    const startbackup = 'http://172.16.121.166:5000/api/v1/outputs/DAN-OUT-2/start';
    const startmain = 'http://172.16.121.166:5000/api/v1/outputs/DAN-OUT-1/start';
    const stopbackup = 'http://172.16.121.166:5000/api/v1/outputs/DAN-OUT-2/stop';
    const check_status = 'http://172.17.166.167:5000/api/v1/inputs/DAN-MPPM-IN/status';

    const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

    it(`should return true when main is on and backup is off (Iteration ${iteration})`, async () => {
        console.log(`Running test: should return true when main is on and backup is off (Iteration ${iteration})`);
        axios.post.mockResolvedValue({ data: 'Success' });
        axios.get.mockResolvedValue({ data: { statistics: { udpStatistics: { inputPresent: true } } } });

        await callApi(startmain);
        await callApi(stopbackup);
        await delay(5000); // 5-second delay
        const status = await statusResponse(check_status);
        expect(status).toBe(true);
    });

    it(`should return true when main is off and backup is on (Iteration ${iteration})`, async () => {
        console.log(`Running test: should return true when main is off and backup is on (Iteration ${iteration})`);
        axios.post.mockResolvedValue({ data: 'Success' });
        axios.get.mockResolvedValue({ data: { statistics: { udpStatistics: { inputPresent: true } } } });

        await callApi(stopmain);
        await callApi(startbackup);
        await delay(5000); // 5-second delay
        const status = await statusResponse(check_status);
        expect(status).toBe(true);
    });

    it(`should return false when both main and backup are off (Iteration ${iteration})`, async () => {
        console.log(`Running test: should return false when both main and backup are off (Iteration ${iteration})`);
        axios.post.mockResolvedValue({ data: 'Success' });
        axios.get.mockResolvedValue({ data: { statistics: { udpStatistics: { inputPresent: false } } } });

        await callApi(stopmain);
        await callApi(stopbackup);
        await delay(5000); // 5-second delay
        const status = await statusResponse(check_status);
        expect(status).toBe(false);
    });

    it(`should return true when both main and backup are on (Iteration ${iteration})`, async () => {
        console.log(`Running test: should return true when both main and backup are on (Iteration ${iteration})`);
        axios.post.mockResolvedValue({ data: 'Success' });
        axios.get.mockResolvedValue({ data: { statistics: { udpStatistics: { inputPresent: true } } } });

        await callApi(startmain);
        await callApi(startbackup);
        await delay(5000); // 5-second delay
        const status = await statusResponse(check_status);
        expect(status).toBe(true);
    });
};

jest.setTimeout(60000);
runTestSuiteMultipleTimes(10000, testSuite);
