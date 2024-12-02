const baseURL = '/api'
const socketBaseURL = 'ws://test-my-project.eu-north-1.elasticbeanstalk.com/api'
const auth = '/auth'
const cars = '/cars'
const urls = {
    auth:{
        login:auth,
        socket: `${auth}/socket`
    },
    cars
}

export {
    baseURL,
    socketBaseURL,
    urls
}