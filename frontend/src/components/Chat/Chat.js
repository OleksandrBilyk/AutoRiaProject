import {useEffect, useRef, useState} from "react";
import {socketService} from "../../services/socketService";
import {client} from "websocket";

const Chat = () => {
    const [room, setRoom] = useState(null)
    const [soketClient, setSoketClient] = useState(null)
    const [messages, setMessages] = useState([])
    const roomInput = useRef();

    useEffect(() => {
        if (room){
            socketInit(room).then(client=>setSoketClient(client))
        }
    }, [room]);
    const socketInit = async (room)=>{
        const {chat} = await socketService();
        const client = await chat(room);

        client.onopen = ()=>{
            console.log('Chat socket connected')
        }

        client.onmessage = ({data})=>{
            const parse = JSON.parse(data.toString());
            const {message, user} = parse;
            setMessages(prevState => [...prevState, {user, message}])

        }
        return client
    }

    const setRoomHandler = ()=>{
        setRoom(roomInput.current.value)

    }

    const handlePressEnter = (e)=>{
        if (e.key === 'Enter'){
            soketClient.send(JSON.stringify({
                data:e.target.value,
                action: 'send_message',
                request_id: new Date().getTime()
            }))
            e.target.value = ''
        }
    }

    return (
        <div>
            {
                !room?
                    <div>
                        <input type="text" ref={roomInput}/>
                        <button onClick={setRoomHandler}>set</button>
                    </div>
                    :
                    <div>
                        {
                            messages.map(message=><div>{message.user}:{message.message}</div>)
                        }
                        <input type="text" onKeyDown={handlePressEnter}/>
                    </div>
            }
        </div>
    );
};

export {Chat};