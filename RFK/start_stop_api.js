const http = require('http');
const axios = require('axios');

async function callApi(operation) {
    try {
        const response = await axios.post(operation);
        //console.log(response.data);
    } catch (error) {
        console.log('Error: ' + error);
    }
}

async function statusResponse(operation) {
    try {
        const response = await axios.get(operation);
        const APIstatus = response.data.statistics.udpStatistics.inputPresent;
        console.log("MPPM STATUS: " + APIstatus);
        return APIstatus;
    } catch (error) {
        console.log('Error: ' + error);
        return false;
    }
}

// Export functions for testing
module.exports = { callApi, statusResponse };
