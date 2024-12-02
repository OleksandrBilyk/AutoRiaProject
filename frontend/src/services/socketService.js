import {authService} from "./authService";
import {w3cwebsocket as W3cWebsocket} from 'websocket';
// import {socketBaseURL} from "../constants/urls";
const baseURL = 'ws://test-my-project.eu-north-1.elasticbeanstalk.com/api'
const socketService = async ()=>{
    const {data:{token}} = await authService.getSocketToken();
    return {
        chat:(room)=>new W3cWebsocket(`${baseURL}/chat/${room}/?token=${token}`),
        cars: ()=>new W3cWebsocket(`${baseURL}/cars/?token=${token}`)
    }
}

export {
    socketService
}